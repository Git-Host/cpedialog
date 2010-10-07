# Tweepy
# Copyright 2009-2010 Joshua Roesslein
# See LICENSE for details.

"""
Tweepy Twitter API library
"""
__version__ = '1.5'
__author__ = 'Joshua Roesslein'
__license__ = 'MIT'

from sinat.models import Status, User, DirectMessage, Friendship, SavedSearch, SearchResult, ModelFactory
from sinat.error import TweepError
from sinat.api import API
from sinat.cache import Cache, MemoryCache, FileCache
from sinat.auth import BasicAuthHandler, OAuthHandler
from sinat.streaming import Stream, StreamListener
from sinat.cursor import Cursor

# Global, unauthenticated instance of API
api = API()

def debug(enable=True, level=1):

    import httplib
    httplib.HTTPConnection.debuglevel = level

