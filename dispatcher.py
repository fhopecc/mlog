import sys, os, cgi, string, unittest
from google.appengine.ext import db, webapp
from google.appengine.api import users
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext.webapp import template
from mlog import *
from datetime import date, datetime
class MainPage(webapp.RequestHandler):
  def get(self):
    self.response.out.write("test")

  def post(self):
    dt = datetime.strptime(self.request.get('date'), '%Y%m%d')
    m =  Mlog(
              account = self.request.get('account'), 
              date    = date(dt.year, dt.month, dt.day), 
              value   = string.atoi(self.request.get('value')), 
              tags    = self.request.get('tags'), 
              comment = self.request.get('comment')
              )
    m.put()
    self.redirect('/mlogs')

application = webapp.WSGIApplication([(r'/.*', MainPage), 
                                      ('/mlog', MainPage)
                                     ],
                                     debug=True)
def main():
  run_wsgi_app(application)

if __name__ == "__main__":
  main()
  #unittest.main()
