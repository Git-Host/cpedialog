## Introduction ##
We will use this page to describe how to start to develop with cpedialog.

## Jion Project ##
  * you should have a google account to use google code.
  * send an email to [project owner](mailto:cpedia@gmail.com) to request as a member.
## Download Resources ##
  * [Python2.5](http://www.python.org/download/)
  * [Google App Engine](http://code.google.com/appengine/downloads.html)
## Learning Resources ##
before you start cpedia, you should be familiar with python, and Google App Engine
  * it is recommanded to read [Dive into Python](http://diveintopython.org/) to start python study, it has been translated into several languages.
  * it is recommanded to read [GAE Getting Started Guide](http://code.google.com/appengine/docs/gettingstarted/) to get a brief understand for Google App Engine
  * it is recommanded to read [Google App Engine Articles](http://code.google.com/appengine/articles/) to get some best practise for GAE.
## Check out Source Code ##
Use a svn client to checkout source code from google code
  * for windows user, it is recommanded to use tortoiseSVN, you can download tortoiseSVN [here](http://tortoisesvn.net/downloads)
  * for linux user, it is recommanded to use svn command line.
  * check out cpedialog source code to local directory
## IDEs ##
  * [PyDev plugin for eclipse](http://code.google.com/appengine/articles/eclipse.html)
  * [WingIDE](http://wingware.com/doc/howtos/google-app-engine)
  * [Komodo IDE](http://www.activestate.com/Products/komodo_ide/index.mhtml)
  * More refer to: http://wiki.python.org/moin/IntegratedDevelopmentEnvironments

## Cpedialog Tech Stack ##
  * Python
  * Google App Engine
  * Django
  * YUI
## Cpedialog Project Stucture ##
| **File** | **Usage** |
|:---------|:----------|
| /admin.py | for the system configuration module |
| /album.py | for integration with [picasaweb albums](http://code.google.com/apis/picasaweb/overview.html)|
| /authorized.py | Decorator method for authenticate/authorization and google authsub. Refer to: [Python Decorators for Functions and Methods](http://www.python.org/dev/peps/pep-0318/)  [AuthSub Authentication for Web Applications](http://code.google.com/apis/accounts/docs/AuthSub.html)|
| /BeautifulSoup.py | Beautiful Soup parses a XML or HTML document into a tree representation. See: http://www.crummy.com/software/BeautifulSoup/  |
| /blog.py | Classes for blog operation and releated resource access.|
| /main.py | Main routine that runs the WSGIApplication using a CGI adaptor |
| /model.py | The entity model of cpedialog.|
| /rpc.py  | Remote Procedure Call for ajax.|
| /util.py | Helper class. Most methods are used for getting cached object from memcache and flushing cache at proper time. |
| /view.py | Django template render base class.|
| /atom, /gdata  | [Google Data APIs](http://code.google.com/apis/gdata/) |
| /img     | Images resource. |
| /recaptcha | [A plugin for reCAPTCHA and reCAPTCHA Mailhide](http://pypi.python.org/pypi/recaptcha-client) reCAPTCHA is used for anti-spam of the blog comments.|
| /simplejson | A simple, fast, extensible JSON encoder and decoder. http://undefined.org/python/#simplejson |
| /stylesheets | CSS style files. |
| /templates | Django templates files. |
| /cpedia  | Common library of cpedialog. |
| /cpedia/filter | Filter classes for Django. |
| /cpedia/pagination| Gql pagination encapsulate class. |
| /cpedia/util| Common util package of cpedialog. |
| /jscripts | Javascript files. |
| /locale  | locale files. |

# Run Cpedialog in your laptop #
  * dev\_appserver.py cpedialog