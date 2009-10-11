import sys, os, cgi, string
from google.appengine.ext import db, webapp
from google.appengine.api import users
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext.webapp import template
from lib import rest

class MainPage(webapp.RequestHandler):
    def get(self):
        rest.route(self.request.path, 'GET', self.request, self.response)

application = webapp.WSGIApplication([('.*', MainPage)],debug=True)

def main(): run_wsgi_app(application)

if __name__ == "__main__":
    main()
