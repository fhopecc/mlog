import datetime
from google.appengine.ext import db
class Mlog(db.Model):
  account = db.StringProperty()
  date    = db.DateProperty()
  value   = db.IntegerProperty()
  tags    = db.StringProperty()
  comment = db.TextProperty()
