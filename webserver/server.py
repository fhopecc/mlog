from __future__ import with_statement
import sys, os
from wsgiref.simple_server import make_server

def file_app(environ,start_response):
  path = environ['PATH_INFO']
  basedir = os.path.dirname(__file__)
  path = path.replace('/', '\\')
  fpath = "%s%s" % (basedir, path)
  output = None 
  with open(fpath) as tfn:
    output = tfn.read()
  if output:
    start_response("200 OK", [('Content-Type','text/html')])
    return [output]
  else:
    start_response("410 failed", [('Content-Type','text/plain')])
    return ["no file"]


httpd = make_server('', 8000, file_app)
print "Serving HTTP on port 8000..."

# Respond to requests until process is killed
httpd.serve_forever()

# Alternative: serve one request, then exit
##httpd.handle_request()

