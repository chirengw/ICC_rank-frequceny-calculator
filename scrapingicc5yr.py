#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 19 19:38:33 2021

@author: charan
"""
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import re
import pandas as pd
from tabulate import tabulate
import os
import datetime
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import time

datalist=[]
driver = webdriver.Chrome(executable_path="/home/charan/newwww/Untitled Folder/chromedriver")
 
start = datetime.datetime.strptime("2016-01-01", "%Y-%m-%d")
end = datetime.datetime.strptime("2021-01-01", "%Y-%m-%d")
date_array = \
    (start + datetime.timedelta(days=x) for x in range(0, (end-start).days))
l=[]
for date_object in date_array:
    l1=date_object.strftime("%Y-%m-%d")
    l.append(l1)
for j in l:
    url='https://www.icc-cricket.com/rankings/mens/player-rankings/odi/batting?at='+j
    driver.get(url)
    # driver.implicitly_wait(1)
    # WebDriverWait(driver,10).until( EC.presence_of_all_elements_located)
    driver.find_element_by_css_selector('.js-rankings-filter-button').click()
    driver.implicitly_wait(10)
    time.sleep(2)
    # WebDriverWait(driver,1).until( EC.presence_of_all_elements_located)
    # driver.find_element_by_css_selectoall-rounderr('.js-rankings-filter-button').click()
    driver.implicitly_wait(1)
    doc = BeautifulSoup(driver.page_source, 'lxml')
    table = doc.find_all('table')[0]
    df = pd.read_html(str(table),header=0)
    # time.sleep(1)
    datalist.append(df[0])
result = pd.concat([pd.DataFrame(datalist[i]) for i in range(len(datalist))],ignore_index=True)
result.to_csv('batting.csv', index=False)  
json_records = result.to_json(orient='records')
# with open("sample.json", "w") as outfile:
#     outfile.write(json_records)
# print(tabulate(result, headers=["Pos","player","Country"],tablefmt='psql'))
datalist_2=[]
for j in l:
    url='https://www.icc-cricket.com/rankings/mens/player-rankings/odi/bowling?at='+j
    driver.get(url)
    # driver.implicitly_wait(1)
    # WebDriverWait(driver,10).until( EC.presence_of_all_elements_located)
    driver.find_element_by_css_selector('.js-rankings-filter-button').click()
    driver.implicitly_wait(10)
    time.sleep(2)
    # WebDriverWait(driver,1).until( EC.presence_of_all_elements_located)
    # driver.find_element_by_css_selector('.js-rankings-filter-button').click()
    driver.implicitly_wait(1)
    doc = BeautifulSoup(driver.page_source, 'lxml')
    table = doc.find_all('table')[0]
    df = pd.read_html(str(table),header=0)
    datalist_2.append(df[0])
    # time.sleep(1)
result_2 = pd.concat([pd.DataFrame(datalist_2[i]) for i in range(len(datalist_2))],ignore_index=True)
result_2.to_csv('bowling.csv', index=False)  
# json_records = result.to_json(orient='records')

datalist_3=[]
for j in l:
    url='https://www.icc-cricket.com/rankings/mens/player-rankings/odi/all-rounder?at='+j
    driver.get(url)
    # driver.implicitly_wait(1)
    # WebDriverWait(driver,10).until( EC.presence_of_all_elements_located)
    driver.find_element_by_css_selector('.js-rankings-filter-button').click()
    driver.implicitly_wait(1)
    time.sleep(1)
    WebDriverWait(driver,1).until( EC.presence_of_all_elements_located)
    # driver.find_element_by_css_selector('.js-rankings-filter-button').click()
    driver.implicitly_wait(1)
    doc = BeautifulSoup(driver.page_source, 'lxml')
    table = doc.find_all('table')[0]
    df = pd.read_html(str(table),header=0)
    datalist_3.append(df[0])
    # time.sleep(1)
result_3 = pd.concat([pd.DataFrame(datalist_3[i]) for i in range(len(datalist_3))],ignore_index=True)
result_3.to_csv('all_round.csv', index=False)  
json_records = result.to_json(orient='records')