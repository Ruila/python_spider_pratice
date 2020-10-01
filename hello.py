
# !/usr/bin/python
# coding:utf-8

import requests as rq
from bs4 import BeautifulSoup
import io
import time
from selenium import webdriver
# import lxml
 
tStart = time.time()
fp = io.open("marryData-List.txt", mode="w")
i = 1
# nextlink = "https://www.marry.com.tw/venue-shop-kwbt2004mmir0mmpg1mm"
# nl_response = rq.get(nextlink) 
# soup = BeautifulSoup(nl_response.text, "html.parser")
# print(soup.prettify())

# 使用 Chrome 的 WebDriver
browser = webdriver.Chrome('./chromedriver')
browser.maximize_window()

while (i<=1):
    # nextlink = "https://www.marry.com.tw/venue-shop-kwbt2004mmir0mmpg1mm"
    # nl_response = rq.get(nextlink) 
    browser.get("https://www.marry.com.tw/venue-shop-kwbt2004mmir0mmpg1mm")
    time.sleep(5)
    soup = BeautifulSoup(browser.page_source, "lxml")

    fp.write(soup.prettify()) 
    # print(soup.find_all("a", class_="shop_name"))
    for url in soup.find_all('a', {'class': 'shop_name'}):
        print(url.string)
        # fp.write(url.string + "\n") 
        # response = rq.get(url.get('href'))
        # print(url.get('href'))
        # html_doc = response.text
        # soup = BeautifulSoup(response.text, "html.parser") 
        # if soup.select('h1') != []:
        #     company = soup.select('h1')[0].find('a').text
            
        #     if company != '' :
                
        #         pid = soup.findAll('li', {'class': 'icon-check'})
        #         Con = ",".join([p.text.strip()  for p in pid])
                
        #         address = soup.findAll('ul', {'class': 'contacts_list'})[0].find('span', {'class': 'contacts_info'}).text
        #         fp.write(company.encode('utf-8') + '='.encode('utf-8'))  
        #         fp.write(Con.encode('utf-8')+ '?'.encode('utf-8')+address.encode('utf-8') +'\n'.encode('utf-8')) 
        #         time.sleep(sleeptime(0,1,0))
    i = i + 1
tEnd = time.time()
fp.close()
print ("It cost %f sec" % (tEnd - tStart))