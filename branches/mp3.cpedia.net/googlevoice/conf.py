#from ConfigParser import ConfigParser, NoOptionError
import os
import settings

from google.appengine.api import memcache
from google.appengine.ext import db
from google.appengine.api import users
from google.appengine.api import datastore_types


class Config(db.Model):

    phoneType = db.StringProperty(multiline=False,default='2') # 1. Home 2. Mobile 3. Work 7. Gizmo
    forwardingNumber = db.StringProperty(multiline=False,default='')
    email = db.StringProperty(multiline=False,default='')
    password = db.StringProperty(multiline=False,default='')
    secret = db.StringProperty(multiline=False,default='')
    
config = Config()
