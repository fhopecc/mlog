import sys, os, cgi, string
from google.appengine.ext import db, webapp
from google.appengine.api import users
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext.webapp import template
from mlog import *
from datetime import date, datetime
class MainPage(webapp.RequestHandler):
  def get(self):
    ms = Mlog.all()
    template_values = {
      'layout': os.path.dirname(__file__) + '/views/layout/mlog.html', 
      'ms': ms
      }
    self.response.out.write(
      template.render('views/mlogs/index.html',
      template_values))
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
class NewPage(webapp.RequestHandler):
  def get(self):
    m = Mlog(account='fhopecc', date = date.today(), value = 0)
    template_values = {
      'layout': os.path.dirname(__file__) + '/views/layout/mlog.html', 
      'm': m
      }
    self.response.out.write(
        template.render('views/mlogs/new.html',
      template_values))
application = webapp.WSGIApplication(
                                     [('/mlogs', MainPage),
                                      ('/mlogs/new', NewPage)
                                     ],
                                     debug=True)
def main():
  run_wsgi_app(application)
if __name__ == "__main__":
  main()
