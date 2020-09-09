import bs4
### Python library for pulling data out of HTML and XML file ###
from bs4 import BeautifulSoup as soup

from urllib.request import urlopen
### Open the URL  ###

import webbrowser
### The webbrowser module provides a high-level interface  ###
###  to allow displaying Web-based documents to users      ###

news_url="https://news.google.com/news/rss"
### Here 'rss' stands for Rich Site Summary   ###
### It is a standard for the syndication of web content and    ### 
### used to distribute the web contents like news feeds headlines,  ###
### event summary and forum updates in XML based format     ###

page=urlopen(news_url)
xml_page   =  page.read()
page.close()

soup_page=soup(xml_page,"xml")
###  lxml’s XML parser    ###
### The only currently supported XML parser  ###

list=soup_page.findAll("item")
### This code finds all the <item> Tags in the document ###

l1,l2,l3=[],[],[]

for i in list:
  
  ####### title  #######
  l1.append(i.title.text)
  
  #######  link  #######
  l2.append(i.link.text)
  
  #published date and time#
  l3.append(i.pubDate.text)
  
for i in range(0,len(l1)):
    print(i+1,')',l1[i])
    print(l3[i])
    print("----------------------------------------------------------------------------------------------------------------")

n=int(input("""
If you wish to read the full news
Enter the index of news headline to study:-  """))
a = n-1 if n>0 else 0

webbrowser.open(l2[a])

