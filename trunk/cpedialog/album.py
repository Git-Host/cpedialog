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
import config
import util

import gdata.urlfetch
gdata.service.http_request_handler = gdata.urlfetch



class BaseRequestHandler(webapp.RequestHandler):
  """Supplies a common template generation function.

  When you call generate(), we augment the template variables supplied with
  the current user in the 'user' variable and the current webapp request
  in the 'request' variable.
  """
  def generate(self, template_name, template_values={}):
    administrator = False
    useremail = ""
    if users.get_current_user():
      url = users.create_logout_url(self.request.uri)
      url_linktext = 'Sign out'
      useremail = users.get_current_user().email()
      if users.is_current_user_admin():
        administrator = True
    else:
      url = users.create_login_url(self.request.uri)
      url_linktext = 'Sign in'
    values = {
      'request': self.request,
      'user': users.GetCurrentUser(),
      'url': url,
      'url_linktext': url_linktext,
      'administrator': administrator,
    }
    values.update(template_values)
    directory = os.path.dirname(__file__)
    path = os.path.join(directory, os.path.join('templates', template_name))
    view.ViewPage(cache_time=0).render(self, template_name,values)


class MainPage(BaseRequestHandler):
  def get(self):
    usernames =config.album['username']
    defaultUsername = usernames[0]
    key_ = "albums_"+defaultUsername
    feed = memcache.get(key_)
    if not feed:
        gd_client = gdata.photos.service.PhotosService()
        feed = gd_client.GetUserFeed(user=defaultUsername)
        memcache.add(key=key_, value=feed, time=3600)
    template_values = {
      'username':defaultUsername,
      'usernames':usernames,
      'albums':feed.entry,
       }
    self.generate('album_main.html',template_values)

class UserHandler(BaseRequestHandler):
  def get(self, username):
    usernames =config.album['username'] 
    key_ = "albums_"+username
    feed = memcache.get(key_)
    if not feed:
        gd_client = gdata.photos.service.PhotosService()
        feed = gd_client.GetUserFeed(user=username)
        memcache.add(key=key_, value=feed, time=3600)
    template_values = {
      'username':username,
      'usernames':usernames,
      'albums':feed.entry,
       }
    self.generate('album_main.html',template_values)


class AlbumHandler(BaseRequestHandler):
    #@authorized.authSub('albums')
    def get(self, username, album_name):
        gd_client = gdata.photos.service.PhotosService()

        key_photos = "photos_"+username+"_"+album_name
        feed_photos = memcache.get(key_photos)
        if not feed_photos:
            feed_photos = gd_client.GetFeed(
                '/data/feed/api/user/%s/album/%s?kind=photo' % (
                    username, album_name))
            memcache.add(key=key_photos, value=feed_photos, time=3600)

        key_albums = "albums_"+ username
        feed_albums = memcache.get(key_albums)
        if not feed_albums:
            feed_albums = gd_client.GetUserFeed(user=username)
            memcache.add(key=key_albums, value=feed_albums, time=3600)

        album = None
        for album_ in feed_albums.entry:
            if album_.name.text == album_name:
                album = album_
                break

        template_values = {
          'photos': feed_photos.entry,
          'album': album,
          'username':username,
          'album_name':album_name,
          }
        self.generate('album_view.html',template_values)

#deprecated
class PhotoHandler(BaseRequestHandler):
    def get(self, username, album_name, photoId):
        gd_client = gdata.photos.service.PhotosService()
        feed = gd_client.GetFeed(
            '/data/feed/api/user/%s/album/%s?kind=photo' % (
                username, album_name))
        i=0
        for photo in feed.entry:
            if photo.gphoto_id.text == photoId:
                break
            i=i+1
        cur_photo = feed.entry[i]
        if(i==0):
            next_photo = feed.entry[i+1]
            pre_photo = None
        else:
          pre_photo = feed.entry[i-1]
          if i==len(feed.entry)-1:
              next_photo = None
          else:
              next_photo = feed.entry[i+1]
            
        template_values = {
          'cur_photo': cur_photo,
          'pre_photo': pre_photo,
          'next_photo': next_photo,
          'username':username,
          'album_name':album_name,
          }
        self.generate('album_photo_view.html',template_values)
