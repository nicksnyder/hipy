import os

def say(thing):
  print thing
  return thing

def command():
  print "this is the command"

def version():
  f = os.path.join(os.path.dirname(__file__), 'VERSION.txt')
  return open(f).read()
