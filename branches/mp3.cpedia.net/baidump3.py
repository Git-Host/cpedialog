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
import model

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
import traceback

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

from google.appengine.ext.webapp import template
from google.appengine.api import users
from google.appengine.ext import webapp
from google.appengine.ext import db
from google.appengine.api import memcache
from google.appengine.api import mail

import gdata.urlfetch
gdata.service.http_request_handler = gdata.urlfetch

import sys
import urllib
from google.appengine.api import urlfetch

from BeautifulSoup import BeautifulSoup

# This handler allows the functions defined in the RPCHandler class to
# be called automatically by remote code.
class RPCHandler(webapp.RequestHandler):
  #session = cpedia.sessions.sessions.Session()
  auth_api = None

  def get(self):
    action = self.request.get('action')
    arg_counter = 0;
    args = []
    while True:
      arg = self.request.get('arg' + str(arg_counter))
      arg_counter += 1
      if arg:
        args += (simplejson.loads(arg),);
      else:
        break;
    result = getattr(self, action)(*args)
    self.response.out.write(simplejson.dumps((result)))

  def post(self):
    action = self.request.get('action')
    request_ = self.request
    result = getattr(self, action)(request_)
    util.getLogger(__name__).debug('ajax action "%s"return value is %s', action,simplejson.dumps(result))
    self.response.out.write(simplejson.dumps(result))


class BaseRequestHandler(webapp.RequestHandler):
  def generate(self, template_name, template_values={}):
        values = {
        'request': self.request,
        }
        values.update(template_values)
        directory = os.path.dirname(__file__)
        view.ViewPage(cache_time=0).render(self, template_name,values)

class MainPage(BaseRequestHandler):
    def get(self):
        self.generate('com/cpedia/main.html',{})

class MP3MainPage(BaseRequestHandler):
    def get(self):
        self.generate('com/cpedia/mp3.html',{})

class SearchMP3(webapp.RequestHandler):
    def get(self,key,page):
    #if self.get("X-AppEngine-Cron")=="true":
        try:
            form_fields = {
              "f": "ms",
              "tn": "baidump3",
              "ct": "134217728",
              "lm": "0",
              "rn": "",
              "pn": str(int(page)*30),
            }
            form_data = urllib.urlencode(form_fields)
            #util.getLogger(__name__).debug("http://mp3.baidu.com/m?" + str(form_data)+"&word="+key)
            baidump3_page = urlfetch.fetch(
                        url="http://mp3.baidu.com/m?" + str(form_data)+"&word="+key,
                        method=urlfetch.GET,
                        headers={'Content-Type': 'text/html;charset=gb2312'}
                    )
            mp3s = []
            if baidump3_page.status_code == 200:
                #htm= unicode(baidump3_page.content,'GBK','ignore').encode('utf-8','ignore')
                baidump3_soap = BeautifulSoup(baidump3_page.content)
                util.getLogger(__name__).debug(baidump3_soap)
                mp3ListTable = baidump3_soap.find("table",id="Tbs")
                if mp3ListTable:
                    mp3_TRs = mp3ListTable.findAll("tr")
                    for mp3_tr in mp3_TRs:
                        tds = mp3_tr.findAll("td")
                        if(tds is not None and len(tds) > 0):
                            mp3={}
                            mp3["id"]= tds[0].contents[0]
                            song = tds[1]
                            songlink = song.find("a")
                            mp3["title"] = songlink.next.contents[0]
                            mp3["link"] = songlink.get("href")
                            singer = tds[2]
                            mp3["singer"] = singer.find("a").contents[0]
                            album = tds[3]
                            album_a = album.find("a")
                            if album_a:
                                mp3["album"] = album_a.contents[0]
                                mp3["albumlink"] = album_a.get("href")
                            else:
                                mp3["album"] = ""
                                mp3["albumlink"] = ""
                            mp3["size"] = tds[7].contents[0]
                            mp3s+=[mp3]

            self.response.out.write(simplejson.dumps({"status":1,"mp3s":mp3s,"startIndex":int(page)*30}))
        except Exception, exception:
            mail.send_mail(sender="cpedia Mobile: MP3 Online <cpedia@gmail.com>",
                           to="Ping Chen <cpedia@gmail.com>",
                           subject="Something wrong with the Baidu MP3 Search API.",
                           body="""
Hi Ping,

Something wroing with the Baidu MP3 Search API.

Below is the detailed exception information:
%s

Please access app engine console to resolve the problem.
http://appengine.google.com/

Send from mp3.cpedia.net
            """ % traceback.format_exc())

            self.response.out.write(simplejson.dumps("{status:0}"))

    def post(self):
        key = self.request.get('key')
        page = self.request.get('page')
        self.get(key,page)

