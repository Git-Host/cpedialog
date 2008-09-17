# !/usr/bin/env python
#
# Copyright 2008 CPedia.com.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

__author__ = 'Ping Chen'


import datetime
import logging
import os
import re
import sys
import urlparse
import wsgiref.handlers
import pickle

from google.appengine.api import users
from google.appengine.ext import db
from google.appengine.ext import webapp
from google.appengine.ext.webapp import template

from openid import fetchers
from openid.consumer.consumer import Consumer
from openid.consumer import discover
from openid.extensions import pape, sreg

from cpedia.openid import fetcher
from cpedia.openid import store
from cpedia.sessions import sessions

from model import User
import view
import authorized

  
class BaseRequestHandler(webapp.RequestHandler):
    consumer = None
    session = sessions.Session()
    session_args = None

    def __init__(self):
        self.session_args = {}

    def generate(self, template_name, template_values={}):
        google_login_url = users.create_login_url(self.request.uri)
        google_logout_url = users.create_logout_url(self.request.uri)
        values = {
            "google_login_status":users.get_current_user(),
            "google_login_url":google_login_url,
            "google_logout_url":google_logout_url
         }
        values.update(template_values)
        view.ViewPage(cache_time=0).render(self, template_name,values)
        
    def show_main_page(self, error_msg=None):
        """Do an internal (non-302) redirect to the front page.
      
        Preserves the user agent's requested URL.
        """
        page = LoginOpenID()
        page.request = self.request
        page.response = self.response
        page.get(error_msg)
    
    def get_store(self):
        return store.DatastoreStore()
    
    def get_consumer(self):
        """Returns a Consumer instance.
        """
        if not self.consumer:
            fetchers.setDefaultFetcher(fetcher.UrlfetchFetcher())
            self.consumer = Consumer(self.session_args, store.DatastoreStore())
      
        return self.consumer
    
    def args_to_dict(self):
        req = self.request
        return dict([(arg, req.get(arg)) for arg in req.arguments()])


class Logout(BaseRequestHandler):
    def get(self, error_msg=None):
        template_values = {
           "error": error_msg
        }
        self.session = sessions.Session()
        self.session.delete()
        if users.get_current_user():
            self.redirect(users.create_logout_url(self.request.uri))
            return
        self.redirect("/")
  

class LoginOpenID(BaseRequestHandler):
    def get(self, error_msg=None):
        template_values = {
           "error": error_msg
        }
        self.generate('login.html',template_values)

    def post(self):
        openid = self.request.get('openid_identifier')
        if not openid:
            self.show_main_page()
            return
        try:
            consumer = self.get_consumer()
            if not consumer:
                return
            auth_request = consumer.begin(openid)
        except discover.DiscoveryFailure, e:
            logging.error('Error with begin on '+openid,e)
            self.show_main_page('An error occured determining your server information.  Please try again.')
            return
        except discover.XRDSError, e:
            self.report_error('Error parsing XRDS from provider.', e)
            self.show_main_page('An error occured determining your server information.  Please try again.')
            return

        sreg_request = sreg.SRegRequest(required = sreg.data_fields.keys())
        auth_request.addExtension(sreg_request)

        parts = list(urlparse.urlparse(self.request.uri))
        parts[2] = 'login-finish'
        parts[4] = 'session_id=%s' % self.session.sid
        parts[5] = ''
        return_to = urlparse.urlunparse(parts)
        realm = urlparse.urlunparse(parts[0:2] + [''] * 4)
    
        # save the session stuff
        self.session = sessions.Session()
        self.session['openid_stuff'] = pickle.dumps(consumer.session)
  
        # send the redirect!  we use a meta because appengine bombs out
        # sometimes with long redirect urls
        redirect_url = auth_request.redirectURL(realm, return_to)
        self.response.out.write("<html><head><meta http-equiv=\"refresh\" content=\"0;url=%s\"></head><body></body></html>" % (redirect_url,))


class LoginOpenIDFinish(BaseRequestHandler):
    def get(self):
        args = self.args_to_dict()
    
        s = {}
        self.session = sessions.Session()
        if self.session['openid_stuff']:
            try:
                s = pickle.loads(str(self.session['openid_stuff']))
            except:
                pass
    
        consumer = Consumer(s, store.DatastoreStore())
        if not consumer:
            return
        fetchers.setDefaultFetcher(fetcher.UrlfetchFetcher())
        auth_response = consumer.complete(args, self.request.uri)
        if auth_response.status == 'success':
            openid = auth_response.getDisplayIdentifier()
            sreg_data = sreg.SRegResponse.fromSuccessResponse(auth_response)
            users = User.all().filter('openids', openid)
            if users.count() == 0:
                user = User()
                user.openids = [db.Category(openid.strip().encode('utf8'))]
                user.username = sreg_data["nickname"]
                user.fullname = sreg_data["fullname"]
                user.country = sreg_data["country"]
                user.birthday = datetime.datetime.strptime(sreg_data["dob"], '%Y-%m-%d')
                user.gender = sreg_data["gender"]
                user.language = sreg_data["language"]
                user.postcode = sreg_data["postcode"]
                #user.email = sreg_data["email"]
                user.put()
                self.session.login_user(user)
                self.redirect('/user/usersetting')
            else:
                user = users[0]

            self.session.login_user(user)
            self.redirect('/')
        else:
            self.show_main_page('OpenID verification failed.')

    def post(self):
        self.get()    

class EditProfile(BaseRequestHandler):
    @authorized.role("user")
    def get(self, error_msg=None):
        template_values = {
           "error": error_msg
        }
        self.generate('user_setting.html',template_values)
