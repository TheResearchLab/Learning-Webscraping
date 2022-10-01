# -*- coding: utf-8 -*-
"""
Created on Wed Sep 28 19:15:46 2022

@author: Aaron
"""

from bs4 import BeautifulSoup
import lxml
import requests
import re


url = "https://webscraper.io/test-sites/e-commerce/allinone/phones/touch"

page = requests.get(url)
soup = BeautifulSoup(page.text,'lxml')

#find
soup.find('div',{'class':'container test-site'})
soup.find('h4',{'class':'pull-right price'})

#find all
soup.find_all('h4',{'class':'pull-right price'})[1]

soup.find_all('p',class_='pull-right')

#Find specific tags
soup.find_all(['h4','p'])

#Find all lines with id
soup.find_all(id=True)

#String find
soup.find_all(string='Iphone')

#Strings in list
soup.find_all(string= ['Nokia 123','Iphone'])

#string find using re
soup.find_all(string=re.compile('Iph'))

#pull the first 3 results
soup.find_all('p',class_ = re.compile('pull'), limit=3)

