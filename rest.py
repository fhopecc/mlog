import unittest, re

def isplural(noun):
  if re.match(r'.*s$', noun):
    return True
  else:
    return False

def route(url, method):
  m = re.match(r'(?P<resource>\w+)(/(?P<id>\w+))?', url)
  if m:
    resource = m.group('resource')
    id = m.group('id')
  else:
    raise SyntaxError("invalid url:<" + url + ">")
  
  handler = resource + "_handler"
  
  if id:
    if method == 'GET':
      method= 'show' 
    elif method == 'POST':
      method= 'update' 
    elif method == 'PUT':
      method= 'create' 
    elif method == 'DELETE':
      method= 'destroy'
    return (handler, method, int(id)) 
  else:
    if method == 'GET':
      return (handler, 'index') 

def disp(handler, method, id):
  h = __import__(handler)
  m = h.__getattribute__(method)
  if id:
    return m.__call__(id)
  else:
    return m.__call__()

class UnitTest(unittest.TestCase):
  def testIsPlural(self):
    self.assertTrue(isplural('users'))
    self.assertFalse(isplural('user'))

  def testRoute(self):
    self.assertEqual(route('mlogs', 'GET'), 
                    ('mlogs_handler', 'index'))   

    self.assertEqual(route('mlogs/11', 'GET'), 
                    ('mlogs_handler', 'show', 11))   

    self.assertEqual(route('mlogs/11', 'POST'), 
                    ('mlogs_handler', 'update', 11))   

    self.assertEqual(route('mlogs/11', 'PUT'), 
                    ('mlogs_handler', 'create', 11))

    self.assertEqual(route('mlogs/11', 'DELETE'), 
                    ('mlogs_handler', 'destroy', 11))   

  def testDisp(self):
    self.assertEqual('user 11', disp(*(route('test_users/11', 'GET'))))   
    self.assertEqual('del user 11', disp(*(route('test_users/11', 'DELETE'))))   

  def testDynamicImportHandler(self):
    h = __import__("test_users_handler")
    self.assertEqual('user 11', h.show(11))

if __name__ == "__main__":
  unittest.main()
  #route('mlogs', 'GET')
