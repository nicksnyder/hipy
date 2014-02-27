from distutils.core import setup

setup(name='HiPy',
      version=open('hipy/VERSION.txt').read(),
      description='A test python script',
      author='Nick Snyder',
      packages=['hipy'],
      package_data={'hipy': ['VERSION.txt']},
      scripts=['bin/hipyscript.py'],
      )
