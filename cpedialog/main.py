
import wsgiref.handlers

from google.appengine.ext import webapp

import blog
import logging
import config


def main():

    application = webapp.WSGIApplication(
                                       [('/addBlog', blog.AddBlog),
                                        ('/viewBlog', blog.ViewBlog),
                                        ('/addBlogReaction', blog.AddBlogReaction),
                                        ('/editBlog', blog.EditBlog),
                                        ('/deleteBlog', blog.DeleteBlog),
                                        ('/editBlogReaction', blog.EditBlogReaction),
                                        ('/deleteBlogReaction', blog.DeleteBlogReaction),
                                        ('/deleteAllBlog', blog.DeleteAllBlog),
                                        ('/deleteAllBlogReaction', blog.DeleteAllBlogReaction),
                                        ('/loadBlogReactionBulk', blog.LoadBlogReactionBulk),
                                        ('/loadBlogBulk', blog.LoadBlogBulk),
                                        ('/setBlogPermalinks', blog.SetBlogPermalinks),

                                        ('/*$', blog.MainPage),
                                        ('/403.html', blog.UnauthorizedHandler),
                                        ('/404.html', blog.NotFoundHandler),
                                        ('/([12]\d\d\d)/(\d|[01]\d)/*$', blog.MonthHandler),
                                        ('/([12]\d\d\d)/(\d|[01]\d)/([-\w]+)/*$', blog.ArticleHandler),
                                       ],
                                       debug=config._DEBUG)
    wsgiref.handlers.CGIHandler().run(application)

if __name__ == "__main__":
    main()
