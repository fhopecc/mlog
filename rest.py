import unittest, re

def isplural(noun):
  if re.match(r'.*s$', noun):
    return True
  else:
    return False

class UnitTest(unittest.TestCase):
  def testIsPlural(self):
    self.assertTrue(isplural('users'))
    self.assertFalse(isplural('user'))

  def testURL(self):
    self.assertEqual('a', 'a')   

  def testDynamicImportHandler(self):
    h = __import__("user_handler")
    self.assertEqual('user handler', h.me())

if __name__ == "__main__":
  unittest.main()
