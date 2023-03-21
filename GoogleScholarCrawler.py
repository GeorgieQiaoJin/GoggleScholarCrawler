#!/usr/bin/env python
# coding: utf-8

# In[1]:


# -*- coding: utf-8 -*- 
from bs4 import BeautifulSoup 
from lxml import etree
import requests 
import csv
import xlwt
import pandas as pd


headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.11 (KHTML, like Gecko) Version/9.0.2 Safari/601.3.9'} 
URL = "http://api.proxiesapi.com"
auth_key = "cbfa2f6aee327ad5e7c8ff0c65b30dbc_sr98766_ooPq87"

fileHeader = ["Number","Title", "Link", "Publisher", "Abstract"]
csvFile = open("/Users/georgieqiaojin/Desktop/instance.csv", "w")
writer = csv.writer(csvFile)
writer.writerow(fileHeader)

i = 0
j = 0
for z in range (0, 120, 10):
    i = i+1
    print('i:', i)
    url = 'https://scholar.google.com/scholar?start='+str(z)+'&q=(videochat+OR+%22video+conferencing%22+OR+%E2%80%9Cvideo+chat%E2%80%9D)+AND+((family+OR+families)+AND+home)&hl=en&as_sdt=0,5'
#url = 'https://scholar.google.com/scholar?start=0&q=(videochat+OR+%22video+conferencing%22+OR+%E2%80%9Cvideo+chat%E2%80%9D)+AND+((family+OR+families)+AND+home)&hl=en&as_sdt=0,5' 
    print(url)
    PARAMS = {'auth_key':auth_key, 'url':url} 
    #r = requests.get(url = URL, params = PARAMS) 
    #response=requests.get(url,headers=headers) 
    response=requests.get(url = URL, params = PARAMS) 
    soup=BeautifulSoup(response.content,'lxml') 

    #print(soup.select('[data-lid]')) 
    
    for item in soup.select('[data-lid]'): 
        j = j+1
        print('j:', j)
        try: 
            #print('----------------------------------------') 
            #print(item) 
            #print(item.select('h3')[0].get_text()) 
            #print(item.select('a')[0]['href']) 
            #print(item.select('.gs_a')[0].get_text()) 
            #print(item.select('.gs_rs')[0].get_text()) 
            #print('----------------------------------------') 
            result_item = [j, item.select('h3')[0].get_text(),item.select('a')[0]['href'],item.select('.gs_a')[0].get_text(),item.select('.gs_rs')[0].get_text() ]
            writer.writerow(result_item)
        except Exception as e: #raise e 
            print('fail')
            result_item = [j,'fail','fail','fail','fail']
            writer.writerow(result_item)
         
csv = pd.read_csv('/Users/georgieqiaojin/Desktop/instance.csv', encoding='utf-8')
csv.to_excel('/Users/georgieqiaojin/Desktop/paperlist.xlsx', sheet_name='data')

