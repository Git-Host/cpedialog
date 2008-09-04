import cgi
import wsgiref.handlers
import urlparse, urllib
import os
import logging
import datetime
import Cookie
import pprint
import pickle
import hashlib

from google.appengine.api import users
from google.appengine.ext import webapp
from google.appengine.ext import db
from google.appengine.ext.webapp import template

from os import environ

from openid import fetchers
from openid.consumer.consumer import Consumer
from openid.consumer import discover

from cpedia.openid import store
from cpedia.openid.fetcher import UrlfetchFetcher

import view

from cpedia.util import sessions
 
class BaseRequestHandler(webapp.RequestHandler):
  """Supplies a common template generation function.

  When you call generate(), we augment the template variables supplied with
  the current user in the 'user' variable and the current webapp request
  in the 'request' variable.
  """
  def generate(self, template_name, template_values={}):
    values = {
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

  def args_to_dict(self):
    req = self.request
    return dict([(arg, req.get(arg)) for arg in req.arguments()])


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
      c = Consumer({},self.get_store())
      try:
        auth_request = c.begin(openid)
      except discover.DiscoveryFailure, e:
        logging.error('Error with begin on '+openid)
        logging.error(str(e))
        self.show_main_page('An error occured determining your server information.  Please try again.')
        return
      parts = list(urlparse.urlparse(self.request.uri))
      parts[2] = 'login-finish'
      parts[4] = ''
      parts[5] = ''
      return_to = urlparse.urlunparse(parts)
  
      realm = urlparse.urlunparse(parts[0:2] + [''] * 4)
  
      # save the session stuff
      self.sess = sessions.Session()
      self.sess['openid_stuff'] = pickle.dumps(c.session)

      # send the redirect!  we use a meta because appengine bombs out
      # sometimes with long redirect urls
      redirect_url = auth_request.redirectURL(realm, return_to)
      self.response.out.write("<html><head><meta http-equiv=\"refresh\" content=\"0;url=%s\"></head><body></body></html>" % (redirect_url,))


class LoginOpenIDFinish(BaseRequestHandler):
  def get(self):
    args = self.args_to_dict()
    url = 'http://'+self.request.host+'/login-finish'

    self.sess = sessions.Session()
    s = {}
    if self.sess['openid_stuff']:
      try:
        s = pickle.loads(str(self.sess['openid_stuff']))
      except:
        self.sess['openid_stuff'] = None

    c = Consumer(s, self.get_store())
    auth_response = c.complete(args, url)

    if auth_response.status == 'success':
      openid = auth_response.getDisplayIdentifier()
      users = User.all().filter('openids', openid)
      if users.count() == 0:
        user = User()
        user.openids = [db.Category(urllib.quote(openid.strip().encode('utf8')))]
        user.put()
      else:
        user = users[0]

      self.sess['user'] = user.key()
      self.sess['logged_in_person'] = user

      self.redirect('/login')

    else:
      self.show_main_page('OpenID verification failed :(')
