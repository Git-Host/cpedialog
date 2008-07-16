__author__ = 'Ping Chen'

import cgi
import wsgiref.handlers
import os
import re
import datetime
import calendar
import logging
import string
import urllib

from xml.etree import ElementTree

from google.appengine.ext.webapp import template
from google.appengine.api import users
from google.appengine.ext import webapp
from google.appengine.ext import db
from google.appengine.api import memcache
from google.appengine.ext import search

from cpedia.pagination.GqlQueryPaginator import GqlQueryPaginator,GqlPage
from cpedia.pagination.paginator import InvalidPage,Paginator
from cpedia.util import translate

from model import Archive,Weblog,WeblogReactions
import authorized
import view
import config
import util


class BaseRequestHandler(webapp.RequestHandler):
  """Supplies a common template generation function.

  When you call generate(), we augment the template variables supplied with
  the current user in the 'user' variable and the current webapp request
  in the 'request' variable.
  """
  def generate(self, template_name, template_values={}):
    values = {
      'archiveList': util.getArchiveList(),
    }
    values.update(template_values)
    directory = os.path.dirname(__file__)
    path = os.path.join(directory, os.path.join('templates', template_name))
    view.ViewPage(cache_time=0).render(self, template_name,values)


class NotFoundHandler(webapp.RequestHandler):
    def get(self):
        self.error(404)
        view.ViewPage(cache_time=36000).render(self)

class UnauthorizedHandler(webapp.RequestHandler):
    def get(self):
        self.error(403)
        view.ViewPage(cache_time=36000).render(self)
        
class MainPage(BaseRequestHandler):
  def get(self):
    pageStr = self.request.get('page')
    if pageStr:
        page = int(pageStr)
    else:
        page = 1;

    #get blog pagination from cache.
    obj_page = util.getBlogPagination(page)
    if obj_page is None:
        self.redirect('/')

    recentReactions = util.getRecentReactions()
    template_values = {
      'page':obj_page,
      'recentReactions':recentReactions,
      }
    self.generate('blog_main.html',template_values)


class AddBlog(BaseRequestHandler):
  @authorized.role("admin")
  def get(self):
    entrytype = self.request.get('entrytype')
    template_values = {
      'entrytype': entrytype,
      'action': "addBlog",
      }
    self.generate('blog_add.html',template_values)

  @authorized.role("admin")
  def post(self):
    preview = self.request.get('preview')
    submitted = self.request.get('submitted')
    entrytype = self.request.get('entrytype')
    user = users.get_current_user()

    blog = Weblog()
    blog.title = self.request.get('title_input')
    blog.content = self.request.get('text_input')
    blog.author = user
    blog.authorEmail = user.email()
    blog.tags_commas = self.request.get('tags')
    if entrytype == 'page':
        blog.entrytype = entrytype
    template_values = {
      'entrytype': entrytype,
      'blog': blog,
      'preview': preview,
      'submitted': submitted,
      'action': "addBlog",
      }
    if preview == '1' and submitted !='1':
        self.generate('blog_add.html',template_values)
    else:
      if submitted =='1':
        try:
            permalink =  util.get_permalink(blog.date,translate.translate('zh-CN','en', util.u(blog.title,'utf-8')))
            if not permalink:
                raise Exception
        except Exception:
            template_values.update({'error':'Generate permanent link for blog error, please retry it.'})
            self.generate('blog_add.html',template_values)
            return
        #check the permalink duplication problem.
        maxpermalinkBlog = db.GqlQuery("select * from Weblog where permalink >= :1 and permalink < :2 order by permalink desc",permalink, permalink+u"\xEF\xBF\xBD").get()
        if maxpermalinkBlog is not None:
            permalink = maxpermalinkBlog.permalink+"1"
        blog.permalink =  permalink
        blog.save()
        util.flushBlogMonthCache(blog)
        util.flushBlogPagesCache()
        self.redirect('/'+permalink)

class AddBlogReaction(BaseRequestHandler):
  def post(self):
    title_review = self.request.get('title_input')
    content_review = self.request.get('text_input')

    blogId_ = self.request.get('blogId')
    blog= Weblog.get_by_id(int(blogId_))

    if(blog is None):
        self.redirect('/')
    blogReaction = WeblogReactions()
    blogReaction.weblog = blog
    blogReaction.content = self.request.get('text_input')
    blogReaction.authorWebsite = self.request.get('website')
    
    user = users.get_current_user()
    clientIp = self.request.remote_addr

    if user is not None:
        blogReaction.author = user
        blogReaction.authorEmail = str(user.email)
        blogReaction.user = str(user.nickname)
    else:
        blogReaction.authorEmail = self.request.get('mail')
        blogReaction.user = self.request.get('name_input')
    blogReaction.userIp = clientIp
    blogReaction.save()
    util.flushRecentReactions()
    self.redirect('/'+blog.permalink)


class EditBlog(BaseRequestHandler):
    @authorized.role("admin")
    def get(self):
        blogId_ = self.request.get('blogId')
        blog = Weblog.get_by_id(int(blogId_))
        template_values = {
        'blog': blog,
        'action': "editBlog",
        }
        self.generate('blog_add.html',template_values)

    @authorized.role("admin")
    def post(self):
        blogId_ = self.request.get('blogId')
        blog= Weblog.get_by_id(int(blogId_))

        if(blog is None):
            self.redirect('/')

        blog.title = self.request.get('title_input')
        blog.content = self.request.get('text_input')
        blog.tags_commas = self.request.get('tags')
        user = users.get_current_user()
        blog.lastModifiedDate = datetime.datetime.now()
        blog.lastModifiedBy = user
        blog.put()
        util.flushBlogMonthCache(blog)
        util.flushBlogPagesCache()
        self.redirect('/'+blog.permalink)

class DeleteBlog(BaseRequestHandler):
  @authorized.role("admin")
  def get(self):
      blogId_ = self.request.get('blogId')
      blog = Weblog.get_by_id(int(blogId_))
      template_values = {
      'blog': blog,
      'action': "deleteBlog",
      }
      self.generate('blog_delete.html',template_values)

  @authorized.role("admin")
  def post(self):
    blogId_ = self.request.get('blogId')
    blog= Weblog.get_by_id(int(blogId_))
    if(blog is not None):
        blogReactions = blog.weblogreactions_set
        for reaction in blogReactions:
            reaction.delete()
        blog.delete()
        util.flushBlogMonthCache(blog)
        util.flushBlogPagesCache()
    self.redirect('/')

class EditBlogReaction(BaseRequestHandler):
    @authorized.role("user")
    def get(self):
        reactionId_ = self.request.get('reactionId')
        blogReaction = WeblogReactions.get_by_id(int(reactionId_))
        template_values = {
        'blogReaction': blogReaction,
        'action': "editBlogReaction",
        }
        self.generate('blog_add.html',template_values)

    @authorized.role("user")
    def post(self):
        blogReactionId_ = self.request.get('blogReactionId')
        blogReaction= WeblogReactions.get_by_id(int(blogReactionId_))

        if(blogReaction is None):
            self.redirect('/')

        blogReaction.content = self.request.get('text_input')
        blogReaction.authorWebsite = self.request.get('website')
        user = users.get_current_user()
        if user is not None:
            blogReaction.lastModifiedBy = user
        else:
            blogReaction.authorEmail = self.request.get('mail')
            blogReaction.user = self.request.get('name_input')

        blogReaction.lastModifiedDate = datetime.datetime.now()
        blogReaction.put()
        self.redirect('/'+blogReaction.weblog.permalink)


class DeleteBlogReaction(BaseRequestHandler):
  @authorized.role("admin")
  def get(self):
      reactionId_ = self.request.get('reactionId')
      blogReaction = WeblogReactions.get_by_id(int(reactionId_))
      template_values = {
      'reaction': blogReaction,
      'action': "deleteBlogReaction",
      }
      self.generate('blog_delete.html',template_values)

  @authorized.role("admin")
  def post(self):
    blogReactionId_ = self.request.get('blogReactionId')
    blogReaction= WeblogReactions.get_by_id(int(blogReactionId_))

    if(blogReaction is not None):
        db.delete(blogReaction)
        util.flushRecentReactions()
    self.redirect('/'+blogReaction.weblog.permalink)


#for the data migration.
class ViewBlog(BaseRequestHandler):
  def get(self):
    blogId_ = self.request.get('blogId')
    blog= Weblog.get_by_id(int(blogId_))

    if(blog is None):
        self.redirect('/')
    permalink = ""
    if not blog.permalink:
          permalink =  util.get_permalink(blog.date,translate.translate('zh-CN','en', util.u(blog.title,'utf-8')))
          blog.permalink =  permalink.lower()
          blog.save()

    reactions = db.GqlQuery("select * from WeblogReactions where weblog =:1  order by date", blog) 
    template_values = {
      'blog': blog,
      'reactions': reactions,
      'permalink': permalink,
      }
    self.generate('blog_view.html',template_values)

class ArchiveHandler(BaseRequestHandler):
    def get(self, monthyear): 
        #get blogs in month from cache.        
        blogs = util.getArchiveBlog(monthyear)
        recentReactions = util.getRecentReactions()
        template_values = {
          'blogs':blogs,
          'recentReactions':recentReactions,
          }
        self.generate('blog_main_month.html',template_values)


class ArticleHandler(BaseRequestHandler):
    def get(self, year, month, perm_stem):
        blog = db.Query(Weblog).filter('permalink =', year + '/' + month + '/' + perm_stem).get()
        if(blog is None):
            self.redirect('/')
        reactions = db.GqlQuery("select * from WeblogReactions where weblog =:1  order by date", blog)
        template_values = {
          'blog': blog,
          'reactions': reactions,
          }
        self.generate('blog_view.html',template_values)

        
class TagHandler(BaseRequestHandler):
    def get(self, encoded_tag):
        tag =  re.sub('(%25|%)(\d\d)', lambda cmatch: chr(string.atoi(cmatch.group(2), 16)), encoded_tag)   # No urllib.unquote in AppEngine?
        blogs = Weblog.all().filter('tags', tag).order('-date')
        recentReactions = util.getRecentReactions()
        template_values = {
          'blogs':blogs,
          'tag':tag,
          'recentReactions':recentReactions,
          }
        self.generate('tag.html',template_values)


class FeedHandler(BaseRequestHandler):
    def get(self,tags=None):
        blogs = Weblog.all().filter('entrytype =','post').order('-date').fetch(10)
        last_updated = datetime.datetime.now()
        if blogs and blogs[0]:
            last_updated = blogs[0].date
            last_updated = last_updated.strftime("%Y-%m-%dT%H:%M:%SZ")
        for blog in blogs:
            blog.formatted_date = blog.date.strftime("%Y-%m-%dT%H:%M:%SZ")
        self.response.headers['Content-Type'] = 'application/atom+xml'
        self.generate('atom.xml',{'blogs':blogs,'last_updated':last_updated})
    

class SearchHandler(BaseRequestHandler):
    def get(self):
        pageStr = self.request.get('page')
        if pageStr:
            page = int(pageStr)
        else:
            page = 1;
        search_term = self.request.get("q")
        query = search.SearchableQuery('Weblog')
        query.Search(search_term)
        result = query.Run()
        try:
            obj_page  =  Paginator(result,config._NUM_PER_PAGE)
        except InvalidPage:
            self.redirect('/')

        recentReactions = util.getRecentReactions()
        template_values = {
          'page':obj_page,
          'recentReactions':recentReactions,
          }
        self.generate('blog_main.html',template_values)