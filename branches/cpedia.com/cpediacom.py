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

from model import Album

import gdata.urlfetch
gdata.service.http_request_handler = gdata.urlfetch



class BaseRequestHandler(webapp.RequestHandler):
  def generate(self, template_name, template_values={}):
    values = {
      'request': self.request,
    }
    values.update(template_values)
    directory = os.path.dirname(__file__)
    view.ViewPage(cache_time=0).render(self, template_name,values)

  def getAlbumFeedEntry(self,album_username):
      key_albums = "albums_"+ album_username
      try:
          feed = memcache.get(key_albums)
      except Exception:
          feed = None
      if not feed:
          gd_client = gdata.photos.service.PhotosService()
          try:
              feed = gd_client.GetUserFeed(user= album_username)
          except Exception:
              return None
          memcache.add(key=key_albums, value=feed, time=3600)
      return feed

  def validatorFeedAndReturnTemplate(self,feed,album_username,usernames):
      if feed == None:
          template_values ={
              'username':album_username,
              'usernames':usernames,
              'error':"Can not retrieve the picasaweb album(s) of user '"+album_username+"', please " +
              "make sure you set the correct picasaweb account."
          }
      else:
          template_values = {
            'username':album_username,
            'usernames':usernames,
            'albums':feed.entry,
             }
      return template_values

  def getPhotoFeed(self, username, album_name):
      gd_client = gdata.photos.service.PhotosService()
      key_photos = "photos_"+username+"_"+album_name
      try:
          feed_photos = memcache.get(key_photos)
      except Exception:
          feed_photos = None
      if not feed_photos:
          feed_photos = gd_client.GetFeed(
              '/data/feed/api/user/%s/album/%s?kind=photo' % (
                  username, album_name))
          memcache.add(key=key_photos, value=feed_photos, time=3600)
      return feed_photos

class MainPage(BaseRequestHandler):
  def get(self):
    self.generate('com/cpedia/main.html',{})

        
