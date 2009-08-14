import fnmatch
import os

def clear_tmps(dir):
  print "c:wd is " + os.cwd()
  for f in os.listdir(dir):
    if os.path.isdir(f):
      if f == '.git':
        continue
      print 'chdir ' + f
      os.chdir(f)
      clear_tmps(f)
    elif fnmatch.fnmatch(f, '*~'):
      path = os.path.join(dir, f)
      print 'remove ' + path
      #os.remove(path)
  os.chdir('..')

clear_tmps(os.path.join(os.path.dirname(__file__), '..'))
