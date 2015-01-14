#!/usr/bin/env python

from bs4 import BeautifulSoup
import requests
import urllib.request
import re
mp3url=[400]
mp3title=[400]


def get_links():
    url='http://www.allamaiqbal.com/works/poetry/urdu/bang/audio/index.html'
    source_code=requests.get(url)
    plain_text=source_code.text
    soup=BeautifulSoup(plain_text)
    for link in soup.find_all('a'):
        href = "http://www.allamaiqbal.com/works/poetry/urdu/bang/audio/" +link.get('href')
        title=link.string
        mp3url.append(href)
        mp3title.append(title)
        #print(title,href)
      #  url['title']="href"
    s3=[mp3title,mp3url]
    n=len(s3[0])
    x=76
    while(x<n):
        if(re.search('[a-zA-Z]', str(s3[0][x]))):
            print("Downloading....")
            print(x, s3[0][x], s3[1][x])
            new_url=urllib.request.urlopen(s3[1][x])
            new_read=new_url.read()
            #print new_read
            new_f=open(s3[0][x] +".mp3","wb")
            new_f.write(new_read)
            new_f.close()
        x=x+1

get_links()
