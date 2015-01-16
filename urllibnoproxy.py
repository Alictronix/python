#!/usr/bin/python

import urllib2
 
user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
headers={'User-Agent':user_agent}
 
def request(url):
    
    request=urllib2.Request(url, None, headers)
    return urllib2.urlopen(request).read()
 
print request("http://icanhazip.com/")
