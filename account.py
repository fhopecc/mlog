from google.appengine.ext import db
class Account(db.Model):
  account  = db.StringProperty()
  tag_tree = db.StringProperty()
  cdate    = db.DateProperty()
