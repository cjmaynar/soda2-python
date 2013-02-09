__author__="Corey Maynard"
__date__ ="$Feb 9, 2013 5:06:00 PM$"

from setuptools import setup,find_packages

setup (
  name = 'SocrataPython2.0',
  version = '0.1',
  packages = find_packages(),
  install_requires=['requests'],
  author = 'Corey Maynard',
  author_email = 'me@coreymaynard.com',
  url = 'http://www.coreymaynard.com',
  license = '',
  long_description= 'A native Python implementation of Socrata\'s SODA 2.0 REST API, using JSON'
)
