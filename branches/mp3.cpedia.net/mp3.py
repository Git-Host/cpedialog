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

class SearchBaiduMP3(webapp.RequestHandler):
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
              "word": key,
            }
            form_data = urllib.urlencode(form_fields)
            #util.getLogger(__name__).debug("http://mp3.baidu.com/m?" + str(form_data)+"&word="+key)
            baidump3_page = urlfetch.fetch(
                        url="http://221.195.40.183/m?" + str(form_data),
                        method=urlfetch.GET,
                        headers={'Content-Type': 'text/html;charset=GB18030'},
                        deadline=10
                    )
            mp3s = []
            if baidump3_page.status_code == 200:
                #htm= unicode(baidump3_page.content,'GBK','ignore').encode('utf-8','ignore')
                baidump3_soap = BeautifulSoup(baidump3_page.content)
                #util.getLogger(__name__).debug(baidump3_soap)
                mp3ListTable = baidump3_soap.find("table",id="Tbs")
                if mp3ListTable:
                    mp3_TRs = mp3ListTable.findAll("tr")
                    for mp3_tr in mp3_TRs:
                        tds = mp3_tr.findAll("td")
                        if(tds is not None and len(tds) > 0):
                            mp3={}
                            mp3["id"]= util.u(tds[0].contents[0], 'GB18030')
                            song = tds[1]
                            song_a = song.find("a")
                            if song_a:
                                title_result  = util.deltag(str(song_a))
                                mp3["title"] = util.u(title_result, 'GB18030')
                                mp3["link"] = util.u(song_a.get("href"), 'GB18030')
                            else:
                                mp3["title"] = ""
                                mp3["link"] = ""

                            singer = tds[2]
                            singer_a = singer.find("a")
                            if singer_a:
                                singer_result  = util.deltag(str(singer_a))
                                mp3["singer"] = util.u(singer_result , 'GB18030')
                                #mp3["singerlink"] = util.u(singer_a.get("href"), 'GB18030')
                            else:
                                mp3["singer"] = ""
                                #mp3["singerlink"] = ""

                            album = tds[3]
                            album_a = album.find("a")
                            if album_a:
                                album_result  = util.deltag(str(album_a))
                                mp3["album"] = util.u(album_result , 'GB18030')
                                #mp3["albumlink"] = util.u(album_a.get("href") , 'GB18030')
                            else:
                                mp3["album"] = ""
                                #mp3["albumlink"] = ""

                            mp3["size"] = util.u(tds[7].contents[0], 'GB18030')
                            mp3s+=[mp3]

            #util.getLogger(__name__).debug(mp3s)
            self.response.headers['Content-Type'] = 'text/json;charset=utf-8'
            self.response.out.write(simplejson.dumps({"source":"baidu","status":1,"mp3s":mp3s,"startIndex":int(page)*30}))
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

            self.response.out.write(simplejson.dumps({"status":0}))

    def post(self):
        key = self.request.get('key')
        page = self.request.get('page')
        self.get(key,page)


class SearchYahooMP3(webapp.RequestHandler):
    def get(self,key,page):
    #if self.get("X-AppEngine-Cron")=="true":
        try:
            form_fields = {
              "x": "mp3:alls",
              "ei": "gbk",
              "v": "music",
              "pid": "ysearch",
              "b": str(int(page)*30),
              "p": key,
            }
            form_data = urllib.urlencode(form_fields)
            #util.getLogger(__name__).debug("http://mp3.baidu.com/m?" + str(form_data)+"&word="+key)
            yahoomp3_page = urlfetch.fetch(
                        url="http://one.cn.yahoo.com/s?" + str(form_data),
                        method=urlfetch.GET,
                        headers={'Content-Type': 'text/html;charset=utf-8'},
                        deadline=10
                    )
            mp3s = []
            if yahoomp3_page.status_code == 200:
                #htm= unicode(baidump3_page.content,'GBK','ignore').encode('utf-8','ignore')
                yahoomp3_soap = BeautifulSoup(yahoomp3_page.content)
                #util.getLogger(__name__).debug(yahoomp3_soap)
                mp3_div = yahoomp3_soap.find("div",attrs={"class":"yst-music"})
                if mp3_div:
                    mp3ListTable = mp3_div.find("table")
                    if mp3ListTable:
                        mp3_TRs = mp3ListTable.findAll("tr")
                        i = 1
                        for mp3_tr in mp3_TRs:
                            tds = mp3_tr.findAll("td")
                            if(tds is not None and len(tds) > 0):
                                mp3={}
                                mp3["id"]= int(page)*30+i
                                i = i+1
                                song = tds[0]
                                song_a = song.find("a")
                                if song_a:
                                    title_result  = util.deltag(str(song_a))
                                    mp3["title"] = util.u(title_result, 'GB18030')
                                    mp3["link"] = util.u(song_a.get("href"), 'GB18030')
                                else:
                                    mp3["title"] = ""
                                    mp3["link"] = ""

                                singer = tds[1]
                                singer_a = singer.find("a")
                                if singer_a:
                                    singer_result  = util.deltag(str(singer_a))
                                    mp3["singer"] = util.u(singer_result , 'GB18030')
                                    #mp3["singerlink"] = util.u(singer_a.get("href"), 'GB18030')
                                else:
                                    mp3["singer"] = ""
                                    #mp3["singerlink"] = ""

                                album = tds[2]
                                album_a = album.find("a")
                                if album_a:
                                    album_result  = util.deltag(str(album_a))
                                    mp3["album"] = util.u(album_result , 'GB18030')
                                    #mp3["albumlink"] = util.u(album_a.get("href") , 'GB18030')
                                else:
                                    mp3["album"] = ""
                                    #mp3["albumlink"] = ""

                                mp3["size"] = util.u(tds[6].contents[0], 'GB18030')
                                mp3s+=[mp3]

            #util.getLogger(__name__).debug(mp3s)
            self.response.headers['Content-Type'] = 'text/json;charset=utf-8'
            self.response.out.write(simplejson.dumps({"source":"yahoo","status":1,"mp3s":mp3s,"startIndex":int(page)*30}))
        except Exception, exception:
            mail.send_mail(sender="cpedia Mobile: MP3 Online <cpedia@gmail.com>",
                           to="Ping Chen <cpedia@gmail.com>",
                           subject="Something wrong with the Yahoo MP3 Search API.",
                           body="""
Hi Ping,

Something wroing with the Yahoo MP3 Search API.

Below is the detailed exception information:
%s

Please access app engine console to resolve the problem.
http://appengine.google.com/

Send from mp3.cpedia.net
            """ % traceback.format_exc())

            self.response.out.write(simplejson.dumps({"status":0}))

    def post(self):
        key = self.request.get('key')
        page = self.request.get('page')
        self.get(key,page)


class SearchSOSOMP3(webapp.RequestHandler):
    def get(self,key,page):
    #if self.get("X-AppEngine-Cron")=="true":
        try:
            form_fields = {
              "t": "1",
              "source": "1",
              "p": str(int(page)*30),
              "w": key,
            }
            form_data = urllib.urlencode(form_fields)
            #util.getLogger(__name__).debug("http://mp3.baidu.com/m?" + str(form_data)+"&word="+key)
            sosomp3_page = urlfetch.fetch(
                        url="http://cgi.music.soso.com/fcgi-bin/m.q?" + str(form_data),
                        method=urlfetch.GET,
                        headers={'Content-Type': 'text/html;charset=GB18030'},
                        deadline=10
                    )
            mp3s = []
            if sosomp3_page.status_code == 200:
                #htm= unicode(baidump3_page.content,'GBK','ignore').encode('utf-8','ignore')
                sosomp3_soap = BeautifulSoup(sosomp3_page.content)
                #util.getLogger(__name__).debug(sosomp3_soap)
                mp3ListTable = sosomp3_soap.find("table",attrs={"class":"song_box"})
                if mp3ListTable:
                    mp3_TRs = mp3ListTable.findAll("tr")
                    i = 1
                    for mp3_tr in mp3_TRs:
                        tds = mp3_tr.findAll("td")
                        if(tds is not None and len(tds) > 0):
                            mp3={}
                            songdata = tds[0].contents[0]
                            songdatas = songdata.split("@@")
                            if songdatas:
                                mp3["id"]= int(page)*30+i
                                i = i+1
                                mp3["title"] = util.u(songdatas[1], 'GB18030')
                                mp3["link"] = util.u(songdatas[8], 'GB18030')
                                mp3["singer"] = util.u(songdatas[3], 'GB18030')
                                mp3["album"]  = util.u(songdatas[2], 'GB18030')
                                mp3["size"] = util.u(tds[10].contents[0], 'GB18030')
                                mp3s+=[mp3]

        #util.getLogger(__name__).debug(mp3s)
            self.response.headers['Content-Type'] = 'text/json;charset=utf-8'
            self.response.out.write(simplejson.dumps({"source":"soso","status":1,"mp3s":mp3s,"startIndex":int(page)*30}))
        except Exception, exception:
            mail.send_mail(sender="cpedia Mobile: MP3 Online <cpedia@gmail.com>",
                           to="Ping Chen <cpedia@gmail.com>",
                           subject="Something wrong with the SOSO MP3 Search API.",
                           body="""
Hi Ping,

Something wroing with the SOSO MP3 Search API.

Below is the detailed exception information:
%s

Please access app engine console to resolve the problem.
http://appengine.google.com/

Send from mp3.cpedia.net
            """ % traceback.format_exc())

            self.response.out.write(simplejson.dumps({"status":0}))

    def post(self):
        key = self.request.get('key')
        page = self.request.get('page')
        self.get(key,page)


class SearchSogouMP3(webapp.RequestHandler):
    def get(self,key,page):
    #if self.get("X-AppEngine-Cron")=="true":
        #try:
            form_fields = {
              "pf": "mp3",
              "page": str(int(page)*30),
              "query": key 
            }
            form_data = urllib.urlencode(dict([k, v.encode('utf-8')] for k, v in form_fields.items()))
            util.getLogger(__name__).debug("http://mp3.sogou.com/music.so?" + str(form_data)+"&query="+key)
            sogoump3_page = urlfetch.fetch(
                        url="http://mp3.sogou.com/music.so?" + str(form_data),
                        method=urlfetch.GET,
                        headers={'Content-Type': 'text/html;charset=GB18030'},
                        deadline=10
                    )
            mp3s = []
            if sogoump3_page.status_code == 200:
                #htm= unicode(baidump3_page.content,'GBK','ignore').encode('utf-8','ignore')
                sogoump3_soap = BeautifulSoup(sogoump3_page.content)
                util.getLogger(__name__).debug(sogoump3_soap)
                mp3ListTable = sogoump3_soap.find("table",id="songlist")
                if mp3ListTable:
                    mp3_TRs = mp3ListTable.findAll("tr")
                    i = 1
                    for mp3_tr in mp3_TRs:
                        tds = mp3_tr.findAll("td")
                        if(tds is not None and len(tds) > 0):
                            mp3={}
                            mp3["id"]= int(page)*30+i
                            i = i+1
                            song = tds[1]
                            song_sups = song.findAll("sup")
                            [sup.extract() for sup in song_sups]
                            song_result  = util.deltag(str(song))
                            mp3["title"] = util.u(song_result, 'GB18030')
                            #mp3["link"] = util.u(song_a.get("href"), 'GB18030')

                            singer = tds[2]
                            if singer:
                                singer_result  = util.deltag(str(singer))
                                mp3["singer"] = util.u(singer_result , 'GB18030')
                                #mp3["singerlink"] = util.u(singer_a.get("href"), 'GB18030')
                            else:
                                mp3["singer"] = ""
                                #mp3["singerlink"] = ""

                            album = tds[3]
                            if album:
                                album_result  = util.deltag(str(album))
                                mp3["album"] = util.u(album_result , 'GB18030')
                                #mp3["albumlink"] = util.u(album_a.get("href") , 'GB18030')
                            else:
                                mp3["album"] = ""
                                #mp3["albumlink"] = ""

                            down = tds[5]
                            down_a = down.find("a")
                            if down_a:
                                down_onclick = down_a.get("onclick")
                                mp3["link"] = util.u(down_onclick.split("'")[1] , 'GB18030')
                            else:
                                mp3["link"] = ""

                            mp3["size"] = util.u(tds[7].contents[0], 'GB18030')
                            mp3s+=[mp3]

        #util.getLogger(__name__).debug(mp3s)
            self.response.headers['Content-Type'] = 'text/json;charset=utf-8'
            self.response.out.write(simplejson.dumps({"source":"sogou","status":1,"mp3s":mp3s,"startIndex":int(page)*30}))
#        except Exception, exception:
#            mail.send_mail(sender="cpedia Mobile: MP3 Online <cpedia@gmail.com>",
#                           to="Ping Chen <cpedia@gmail.com>",
#                           subject="Something wrong with the Sogou MP3 Search API.",
#                           body="""
#Hi Ping,
#
#Something wroing with the Sogou MP3 Search API.
#
#Below is the detailed exception information:
#%s
#
#Please access app engine console to resolve the problem.
#http://appengine.google.com/
#
#Send from mp3.cpedia.net
#            """ % traceback.format_exc())
#
#            self.response.out.write(simplejson.dumps({"status":0}))

    def post(self):
        key = self.request.get('key')
        page = self.request.get('page')
        self.get(key,page)

