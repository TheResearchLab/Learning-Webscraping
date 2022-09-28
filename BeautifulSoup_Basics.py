# -*- coding: utf-8 -*-
"""
Created on Tue Sep 27 19:59:03 2022

@author: Aaron
"""

from bs4 import BeautifulSoup #scraper
import lxml #parse html
import requests #request page

url = "https://en.wikipedia.org/wiki/Lonzo_Ball"
page = requests.get(url)
#print(page.text) #raw page text

soup = BeautifulSoup(page.text,'lxml') # parsed page text

# Navigable Strings
soup.h1 #Get Header
soup.h1.string #Get just string

#attribute
tag = soup.h1.span
tag.attrs #attributes under header (dictionary object)
tag['class'] #dictionary key


