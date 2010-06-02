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

from cpedia.utils import utils
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

class MainPage(BaseRequestHandler):
    def get(self):
        #perm_stem = 'gv-dialer'
        #blog = db.Query(model.Weblog).filter('permalink =',perm_stem).get()
        #reactions = db.GqlQuery("select * from WeblogReactions where weblog =:1  order by date", blog)
        template_values = {
         # 'blog': blog,
          #'reactions': reactions,
          }
        #self.generate('blog_view.html',template_values)
        self.generate('com/cpedia/main.html',template_values)



class CallGoogleVoicePage(BaseRequestHandler):
    def get(self):
        self.generate('com/cpedia/voice.html')

    def post(self):
        try:
            username = self.request.get("username")
            password = self.request.get("password")
            outgoingNumber = self.request.get("outgoingNumber")
            forwardingNumber = self.request.get("forwardingNumber")
            #phoneType = self.request.get("phoneType")
            voice = Voice()
            voice.login(username,password)
            voice.call(outgoingNumber,forwardingNumber)
            return
        except Exception , e:
            self.response.out.write(e)

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

        
    #get latest coupon code from www.retailmenot.com
class GetCouponsJob(BaseRequestHandler):
    def get(self):
    #if self.get("X-AppEngine-Cron")=="true":
        try:
            form_fields = {
              "f": "ms",
              "rf": "idx",
              "tn": "baidump3",
              "ct": "134217728",
              "lm": "0",
            }
            form_data = urllib.urlencode(form_fields)
            retailmenot_page = urlfetch.fetch(
                    url="http://mp3.baidu.com/m",
                    payload=form_data,
                    method=urlfetch.POST,
                    headers={'Content-Type': 'text/html; charset=UTF-8'}
                    )
            mp3s = []
            if retailmenot_page.status_code == 200:
                retailmenot_soap = BeautifulSoup(retailmenot_page.content)
                mp3ListTable = retailmenot_soap.find("table",id="Tbs")
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
                        
                        #coupon = models.Coupons(vendor="retailmenot.com")
                        code_ = mp3_tr.find("td",attrs={"class":"code"})
                        coupon.code = str(code_.next.contents[0])
                        discount_  = mp3_tr.find("td",attrs={"class":"discount"})
                        coupon.discount = utils.utf82uni(discount_.contents[0])
                        site_info = mp3_tr.find("span",attrs={"class":"site"}).next.contents[0]
                        coupon.site_name = utils.utf82uni(site_info.rstrip(" coupon codes"))
                        siteTools = mp3_tr.find("div",attrs={"class":"siteTools"})
                        site_img = siteTools.find("img")
                        if site_img:
                            image_url = site_img.get("src")
                            coupon.image = image_url
                            site_url = site_img.get("alt")
                            if site_url.rfind("http:")==-1:
                                site_url = "http://"+site_url
                            coupon.site_url = site_url
                        script_ = mp3_tr.find("script",attrs={"type":"data"}).contents[0]
                        couponId = "couponId"
                        siteId = "siteId"
                        dict_ = eval(script_)
                        coupon.coupon_id = dict_["couponId"]
                        coupon.site_id = dict_["siteId"]
                        mp3s+=[coupon]
            latest_coupons = []
            for coupon in mp3s:
                coupon_ = models.Coupons.gql('where coupon_id =:1 and site_id =:2',coupon.coupon_id,coupon.site_id
                        ).fetch(10
                        )
                if coupon_ and len(coupon_) > 0:
                    break
                else:
                    latest_coupons += [coupon]
            for latest_coupon in reversed(latest_coupons):
                latest_coupon.created_date = datetime.datetime.now() #unaccuracy for the auto_now_add
                latest_coupon.put()
            template_values = {
            "msg":"Generate latest coupons from retailmenot successfully.",
            }
        except Exception, exception:
            mail.send_mail(sender="cpedia Mobile <android@cpedia.net>",
                           to="Ping Chen <cpedia@gmail.com>",
                           subject="Something wrong with the Baidu MP3 Search API.",
                           body="""
Hi Ping,

Something wroing with the Baidu MP3 Search API.

Below is the detailed exception information:
%s

Please access app engine console to resolve the problem.
http://appengine.google.com/

Sent from mp3.cpedia.net
            """ % traceback.format_exc())

            template_values = {
            "msg":"Generate latest deals from dealsea.com unsuccessfully. An alert email sent out.<br>" + traceback.format_exc(),
            }

        self.generate('coupons.html',template_values)

def post(self):
    self.get()

