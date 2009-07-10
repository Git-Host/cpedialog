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

from xml.etree import ElementTree

from google.appengine.ext.webapp import template
from google.appengine.api import users
from google.appengine.ext import webapp
from google.appengine.ext import db
from google.appengine.api import memcache

import authorized
import view
import util

#import gdata.urlfetch
#gdata.service.http_request_handler = gdata.urlfetch

class BaseRequestHandler(webapp.RequestHandler):
    def generate(self, template_name, template_values={}):
        values = {
        'request': self.request,
        }
        values.update(template_values)
        directory = os.path.dirname(__file__)
        view.ViewPage(cache_time=0).render(self, template_name,values)

class ProfileHandler(BaseRequestHandler):
    def get(self, username):
        template_values = {
        "username":username
        }
        self.generate('google_profile.html',template_values)

class BooksHandler(BaseRequestHandler):
    def get(self, username):
        template_values = {
        "username":username
        }
        self.generate('google_books.html',template_values)


