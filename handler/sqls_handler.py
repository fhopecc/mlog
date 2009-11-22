# coding=utf8
import sqlite3
from webob import Request
from lib.pyratemp import Template
from lib import pyratemp
def index(environ, start_response):
    req = Request(environ)

    t = Template(filename="template\sqls.html", escape=pyratemp.HTML)

    status = '200 OK'
    response_headers = [('Content-type','text/html')]
    start_response(status, response_headers)
    return [t(result='query string %s' % req.GET['id']).encode("utf-8")]

def show(environ, start_response):
    id = environ['rest.id']
    
    conn = sqlite3.connect('d:/stxt/test.db')
    c = conn.cursor()
    rs = c.execute(id)

    t = Template(filename="template\sqls.html", escape=pyratemp.HTML)
    tab = Template(filename=r"template\table.html", escape=pyratemp.HTML) 

    status = '200 OK'
    response_headers = [('Content-type','text/html')]
    start_response(status, response_headers)
    return [t(result=tab(rows=rs), id=id).encode("utf-8")]

def destroy(request, response):
    return "del test %d" % id
