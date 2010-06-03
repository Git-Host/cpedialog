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

__author__ = 'Ping Chen'

import os
import re
import datetime
import calendar
import logging
import string
from google.appengine.api import users
from google.appengine.ext import db
from google.appengine.api import memcache
from google.appengine.api import urlfetch

from cpedia.pagination.GqlQueryPaginator import YUIPaginator,GqlQueryPaginator,GqlPage
from cpedia.pagination.paginator import InvalidPage,Paginator
import cpedia.sessions.sessions

from model import Counter,Archive,Weblog,WeblogReactions,\
    AuthSubStoredToken,Album,Menu,Tag,DeliciousPost,Feeds,CPediaLog,User,CSSFile
import simplejson
import cgi
import urllib, hashlib

import twitter

# Functions to generate permalinks
def get_permalink(date,title):
    return get_friendly_url(title)

# Module methods to handle incoming data
def get_datetime(time_string):
    if time_string:
        return datetime.datetime.strptime(time_string, '%Y-%m-%d %H:%M:%S')
    return datetime.datetime.now()

def get_friendly_url(title):
    return re.sub('-+', '-', re.sub('[^\w-]', '', re.sub('\s+', '-', removepunctuation(title).strip()))).lower()

def removepunctuation(str):
    punctuation = re.compile(r'[.?!,":;]')
    str = punctuation.sub("", str)
    return str

def u(s, encoding):
    if isinstance(s, unicode):
        return s
    else:
        return unicode(s, encoding)


#get the archive monthe list. Cached.
def getArchiveList():
    key_ = "blog_monthyear_key"
    try:
        monthlist = memcache.get(key_)
    except Exception:
        monthlist = None
    if monthlist is None:
        monthlist = Archive.gql('ORDER BY date desc').fetch(100)
        memcache.add(key=key_, value=monthlist, time=3600)
    else:
        getLogger(__name__).debug("getMonthYearList from cache. ")
    return monthlist



#get log images list. Cached.
def getLogoImagesList():
    key_ = "blog_logoImagesList_key"
    try:
        logoImagesList = memcache.get(key_)
    except Exception:
        logoImagesList = None
    if logoImagesList is None:
        logoImagesList = []
        directory = os.path.dirname(__file__)
        path = os.path.normpath(os.path.join(directory, 'img/logo/'))
        files = os.listdir(path)
        for file in files:
            (shortname, extension) = os.path.splitext(file)
            if extension.lower() == ".gif":
                logoImagesList.append(file)
        memcache.add(key=key_, value=logoImagesList, time=3600)
    else:
        getLogger(__name__).debug("getLogoImagesList from cache. ")
    return logoImagesList

#get recent comments. Cached.
def getRecentReactions():
    key_ = "blog_recentReactions_key"
    try:
        recentReactions = memcache.get(key_)
    except Exception:
        recentReactions = None
    if recentReactions is None:
        recentReactions = db.GqlQuery("select * from Weblog order by lastCommentedDate desc").fetch(10)
        memcache.add(key=key_, value=recentReactions, time=3600)
    else:
        getLogger(__name__).debug("getRecentReactions from cache. ")

    return recentReactions

#get recent featured article or blog. Cached.
def getRecentFeatured():
    key_ = "blog_recentFeatured_key"
    try:
        recentFeatured = memcache.get(key_)
    except Exception:
        recentFeatured = None
    if recentFeatured is None:
        recentFeatured = Weblog.all().filter('tags', "featured").order('-date').fetch(10)
        memcache.add(key=key_, value=recentFeatured, time=3600)
    else:
        getLogger(__name__).debug("getRecentFeatured from cache. ")

    return recentFeatured


#get blog pagination. Cached.
def getBlogPagination(page):
    key_ = "blog_pages_key"
    try:
        obj_pages = memcache.get(key_)
    except Exception:
        obj_pages = None
    if obj_pages is None or page not in obj_pages:
        blogs_query = Weblog.gql('WHERE entrytype=:1 ORDER BY date desc','post')
        try:
            cpedialog = getCPedialog()
            #todo:get blog count from the Counter object
            obj_page  =  YUIPaginator(blogs_query,page,cpedialog.num_post_per_page)
            if obj_pages is None:
                obj_pages = {}
            obj_pages[page] = obj_page
            memcache.add(key=key_, value=obj_pages, time=3600)
        except InvalidPage:
            return None
    else:
        getLogger(__name__).debug("getBlogPagination from cache. ")

    return obj_pages[page]

#get blogs in some month. Cached.
def getArchiveBlog(monthyear):
    monthyear1 = re.sub( "-", "_", monthyear )
    key_= "blog_archive_"+monthyear1+"_key"
    monthyearTmp = re.sub( "-", " ", monthyear )
    try:
        blogs = memcache.get(key_)
    except Exception:
        blogs = None
    if blogs is None:
        #blogs = Weblog.all().filter('monthyear', monthyearTmp).filter('entrytype','post').order('-date')
        blogs = db.GqlQuery("select * from Weblog where monthyear=:1 and entrytype = 'post'order by date desc",monthyearTmp).fetch(100)
        memcache.add(key=key_, value=blogs, time=3600)
    else:
        getLogger(__name__).debug("getMonthBlog from cache. ")
    return blogs

#get menu list. Cached.
def getMenuList():
    key_ = "blog_menuList_key"
    try:
        menus = memcache.get(key_)
    except Exception:
        menus = None
    if menus is None:
        menus = Menu.gql('WHERE valid =:1  ORDER BY order',True).fetch(100)
        memcache.add(key=key_, value=menus, time=3600)
    else:
        getLogger(__name__).debug("getMenuList from cache. ")
    return menus

#get album list. Cached.
def getAlbumList():
    key_ = "blog_albumList_key"
    try:
        albums = memcache.get(key_)
    except Exception:
        albums = None
    if albums is None:
        albums = Album.gql('WHERE valid =:1 ORDER BY order desc',True).fetch(100)
        memcache.add(key=key_, value=albums, time=3600)
    else:
        getLogger(__name__).debug("getAlbumList from cache. ")
    return albums

#get tag list. Cached.
def getTagList():
    key_ = "blog_tagList_key"
    try:
        tags = memcache.get(key_)
    except Exception:
        tags = None
    if tags is None:
        tags = Tag.gql('WHERE valid =:1 ORDER BY tag',True).fetch(1000)
        memcache.add(key=key_, value=tags, time=3600)
    else:
        getLogger(__name__).debug("getTagList from cache. ")
    return tags


#get feed list. Cached.
def getFeedList():
    key_ = "blog_feedList_key"
    try:
        feeds = memcache.get(key_)
    except Exception:
        feeds = None
    if feeds is None:
        feeds = Feeds.gql('WHERE valid =:1 ORDER BY order',True).fetch(1000)
        memcache.add(key=key_, value=feeds, time=3600)
    else:
        getLogger(__name__).debug("getFeedList from cache. ")
    return feeds


#get cpedialog configuration. Cached.
def getCPedialog():
    key_ = "blog_cpedialog_key"
    try:
        cpedialog = memcache.get(key_)
    except Exception:
        cpedialog = None
    if cpedialog is None:
        cpedialog = CPediaLog().gql("WHERE default =:1",True).get()
        if cpedialog is None:
            cpedialog = CPediaLog()
        memcache.add(key=key_, value=cpedialog, time=36000)            
    else:
        getLogger(__name__).debug("getCPedialog from cache. ")
    return cpedialog

#get CSS links
def getCSS():
    key_ = "blog_css_key"
    try:
        css = memcache.get(key_)
    except Exception:
        css = None
    if css is None:
        css = CSSFile().all().filter("default",True).fetch(1)
        if len(css) == 0:
            css = [ {'filename' : '/stylesheets/blog.css'}]
        memcache.add(key=key_, value=css, time=36000)            
    else:
        getLogger(__name__).debug("get CSS from cache. ")
    return css



#flush tag list.
def flushCPedialog():
    memcache.delete("blog_cpedialog_key")


#flush tag list.
def flushTagList():
    memcache.delete("blog_tagList_key")


#flush album list.
def flushAlbumList():
    memcache.delete("blog_albumList_key")

#flush menu list.
def flushMenuList():
    memcache.delete("blog_menuList_key")


#flush feed list.
def flushFeedList():
    memcache.delete("blog_feedList_key")

#flush MonthYear list.
def flushArchiveList():
    memcache.delete("blog_monthyear_key")

#flush MonthYear list.
def flushArchiveBlog(monthyear):
    monthyear1 = re.sub( "-", "_", monthyear )
    key_= "blog_archive_"+monthyear1+"_key"
    memcache.delete(key_)

#flush recent comments.
def flushRecentReactions():
    memcache.delete("blog_recentReactions_key")

#flush recent featured.
def flushRecentFeatured():
    memcache.delete("blog_recentFeatured_key")

#flush blog pagination.
def flushBlogPagesCache():
    memcache.delete("blog_pages_key")

#flush month-cached blog.
def flushBlogMonthCache(blog):
    if blog.date is None:
        blog.date = datetime.datetime.now()
    year_ =  blog.date.year
    month_ =  blog.date.month
    key= "blog_year_month_"+str(year_)+"_"+str(month_)+"_key"
    memcache.delete(key)

#flush del.icio.us tag.
def flushDeliciousTag():
    memcache.delete("blog_deliciousList_key")

#flush list of CSS files
def flushCSS():
    memcache.delete("blog_css_key")

def getDeliciousTag(username):
    key_ = "blog_deliciousList_key"
    try:
        tags = memcache.get(key_)
    except Exception:
        tags = None
    if tags is None:
        try:
            url = "http://feeds.delicious.com/v2/json/tags/%s" % username
            result = urlfetch.fetch(url,
                        method=urlfetch.GET,
                        headers={'Content-Type': 'application/json'})
            #getLogger(__name__).debug("delicious content: %s" % result.content)
            tags = []
            if result.status_code == 200:
                objs = eval(result.content)
                for obj in objs:
                    tags.append(Tag(tag=obj,entrycount = int(objs[obj])))
            memcache.add(key=key_, value=tags, time=3600)
        except Exception:
            pass
    else:
        getLogger(__name__).debug("getDeliciousTag from cache. ")
    return tags


def getDeliciousPost(username,tag):
    key_ = "blog_deliciousList_"+tag+"_key"
    try:
        posts = memcache.get(key_)
    except Exception:
        posts = None
    if posts is None:
        url = "http://feeds.delicious.com/v2/json/%s/%s" % (username, tag)
        result = urlfetch.fetch(url,
                        method=urlfetch.GET,
                        headers={'Content-Type': 'application/json'})
        posts = []
        if result.status_code == 200:
            posts = map(DeliciousPost,simplejson.loads(result.content))
        memcache.add(key=key_, value=posts, time=3600)
    else:
        getLogger(__name__).debug("getDeliciousPost from cache. ")
    return posts

def getGravatarUrlByUser(user):
    default = "/img/anonymous.jpg"
    if user is not None:
        try:
            email = user.email()
        except Exception:
            email = user.email
        return getGravatarUrl(email)
    else:
        return default

def getGravatarUrl(email):
    cpedialog = getCPedialog()
    default = cpedialog.root_url+"/img/anonymous.jpg"
    size = 48
    gravatar_url = "http://www.gravatar.com/avatar.php?"
    gravatar_url += urllib.urlencode({'gravatar_id':hashlib.md5(str(email)).hexdigest(),
        'default':default, 'size':str(size)})
    return gravatar_url

def getUserNickname(user):
    default = "anonymous"
    if user:
        try:
            email = user.email()
        except Exception:
            email = user.email
        if user.nickname:
            return user.nickname
        elif email:
            return email.split("@")[0]
    else:
        return default

def getLogger(loggerName):
    """get logger to use in every model"""
    #create a logger to use
    logger = logging.getLogger(loggerName)
    logger.setLevel(logging.DEBUG)
    return logger

def getUser():
    #get user from session
    session = cpedia.sessions.sessions.Session()
    return session.get_current_user()

def getTwitterUser():
    key_ = "twitter_user_key"
    try:
        twitter_user = memcache.get(key_)
    except Exception:
        twitter_user = None
    if twitter_user is None:
        try:
            cpedialog = getCPedialog()
            api = twitter.Api()
            twitter_user = api.GetUser("cpedia")
            memcache.add(key=key_, value=twitter_user, time=36000)
        except Exception:
            pass
            #twitter_user = None
    else:
        getLogger(__name__).debug("getTwitterUser from cache. ")
    return twitter_user

def deltag(arg):
        result = re.sub('<(.|\n)+?>','',arg)
        return re.sub('&nbsp;','',result)
