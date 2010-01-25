#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
#    Copyright (C) 2009  pranny; pranny@gmail.com
#    
#    Initial work by JoshTheCoder 
#    at http://github.com/joshthecoder/tweepy/tree/master/examples/appengine/


import os

from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext.webapp import template, RequestHandler, WSGIApplication
from google.appengine.api import users

from models import OAuthToken
import tweepy


if os.environ.get('SERVER_SOFTWARE','').startswith('Devel'):
    CONSUMER_KEY = 'e9n31I0z64dagq3WbErGvA'
    CONSUMER_SECRET = '9hwCupdAKV8EixeNdN3xrxL9RG3X3JTXI0Q520Oyolo'
    CALLBACK = 'http://127.0.0.1:8080/oauth/callback'
else:
    CONSUMER_KEY = 'g39fJDSoHkXn1xhtquCv9g'
    CONSUMER_SECRET = 'oNTZtmTMpT8k0fRSuJbgfNv3MdTpQyzTegTh95JsVw'
    CALLBACK = 'http://www.myblive.com/oauth/callback'

class MainPage(RequestHandler):
    def get(self):
        if users.get_current_user() is None:
            self.response.out.write(template.render('templates/home.html',
                                        {"login_url": users.create_login_url('/')}))
            return
        
        request_token = OAuthToken.all().filter('user = ', users.get_current_user()).filter('access_key !=', None).get()
        if request_token is not None:
            self.redirect('/home')
            return
        
        self.response.out.write(template.render('templates/home.html', {
                        "user": users.get_current_user(),
                        "logout_url": users.create_logout_url('/')
                }))
            

class RequestAuthorization(RequestHandler):
    def get(self):
            if users.get_current_user() is None:
                self.response.out.write(template.render('templates/home.html',
                                        {"login_url": users.create_login_url('/')}))
                return
            
            request_token = OAuthToken.all().filter('user = ', users.get_current_user()).filter('access_key !=', None).get()
            if request_token is not None:
                self.redirect('/home')
                return
            
            # Build a new oauth handler and display authorization url to user.
            auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET, CALLBACK)

            auth_url = auth.get_authorization_url()

            # We must store the request token for later use in the callback page.
            request_token = OAuthToken(
                    token_key = auth.request_token.key,
                    token_secret = auth.request_token.secret,
                    user = users.get_current_user()
            )
            request_token.put()    
            self.redirect(auth_url)

# Callback page (/oauth/callback)
class CallbackPage(RequestHandler):

    def get(self):
        oauth_token = self.request.get("oauth_token", None)
        oauth_verifier = self.request.get("oauth_verifier", None)
        if oauth_token is None:
            # Invalid request!
            self.response.out.write(template.render('error.html', {
                    'message': 'Missing required parameters!'
            }))
            return

        # Lookup the request token
        request_token = OAuthToken.gql("WHERE token_key=:key", key=oauth_token).get()
        if request_token is None:
            # We do not seem to have this request token, show an error.
            self.response.out.write(template.render('error.html', {'message': 'Invalid token!'}))
            return

        # Rebuild the auth handler
        auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
        auth.set_request_token(request_token.token_key, request_token.token_secret)

        # Fetch the access token
        try:
            auth.get_access_token(oauth_verifier)
        except tweepy.TweepError, e:
            # Failed to get access token
            self.response.out.write( template.render('error.html', {'message': e}))
            return
        
        request_token.access_key = auth.access_token.key
        request_token.access_secret = auth.access_token.secret
        request_token.oauth_token = oauth_token
        request_token.oauth_verifier = oauth_verifier
        request_token.put()

        self.redirect('/home')
      
class Home(RequestHandler):
    def get(self):
        if users.get_current_user() is None:
            print "You should be logged into Google Accounts and have granted access"
            return
        dbauth = OAuthToken.all().filter('user = ', users.get_current_user()).filter('access_key !=', None).get()

        auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
        auth.set_request_token(dbauth.token_key, dbauth.token_secret)
        auth.set_access_token(dbauth.access_key, dbauth.access_secret)
        
        auth_api = tweepy.API(auth)
        friends_timeline = auth_api.friends_timeline()
        self.response.out.write(template.render('templates/twitter_home.html',
                                {'friends_timeline':friends_timeline,
                                 'user': users.get_current_user(),
                                 'logout_url': users.create_logout_url('/')}))

# Construct the WSGI application
application = WSGIApplication([

        # OAuth example
        (r'/', MainPage),
        (r'/oauth', RequestAuthorization ),
        (r'/oauth/callback', CallbackPage),
        (r'/home', Home),

], debug=True)

def main():
    run_wsgi_app(application)

# Run the WSGI application
if __name__ == '__main__':
    main()
