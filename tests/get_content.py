#!/usr/bin/python

import urllib2

response = urllib2.urlopen('http://192.168.1.21:3333')
html = response.read()
print html
