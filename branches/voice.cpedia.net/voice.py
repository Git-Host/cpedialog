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

# -*- coding: utf-8 -*-

__author__ = 'Ping Chen'


import gdata.photos.service
import gdata.media
import gdata.geo
import atom

import cgi
import wsgiref.handlers
import os
import re
import datetime
import calendar
import logging
import string
import simplejson

from xml.etree import ElementTree

from google.appengine.ext.webapp import template
from google.appengine.api import users
from google.appengine.ext import webapp
from google.appengine.ext import db
from google.appengine.api import memcache

import authorized
import view
import util
import twitter

from googlevoice import Voice
from googlevoice.util import input


import gdata.urlfetch
gdata.service.http_request_handler = gdata.urlfetch

class BaseRequestHandler(webapp.RequestHandler):
  def generate(self, template_name, template_values={}):
        google_login_url = users.create_login_url(self.request.uri)
        google_logout_url = users.create_logout_url(self.request.uri)
        values = {
        "google_login_status":users.get_current_user(),
        "google_login_url":google_login_url,
        "google_logout_url":google_logout_url,
        'request': self.request,
        }
        values.update(template_values)
        directory = os.path.dirname(__file__)
        view.ViewPage(cache_time=0).render(self, template_name,values)


class CallGoogleVoicePage(BaseRequestHandler):
    def get(self):
        self.generate('com/cpedia/voice.html')

    def post(self):
        username = self.request.get("username")
        password = self.request.get("password")
        outgoingNumber = self.request.get("outgoingNumber")
        forwardingNumber = self.request.get("forwardingNumber")
        voice = Voice()
        voice.login(username,password)
        voice.call(outgoingNumber,forwardingNumber)
        return


class GoogleVoiceAccountPage(BaseRequestHandler):
    def get(self):
        self.generate('com/cpedia/voice.html')

    def post(self):
        username = self.request.get("username")
        password = self.request.get("password")
        voice = Voice()
        voice.login(username,password)
        settings = voice.settings
        phones = voice.phones
        phones_=[]
        for phone in phones:
            phone_ = {}
            phone_['name'] = phone.name
            phone_['phoneNumber'] = phone.phoneNumber
            phones_+=[phone_]
        returnValue = {"phones":phones_,"google_voice_number":settings['primaryDid']}
        self.response.out.write(simplejson.dumps((returnValue)))



        
