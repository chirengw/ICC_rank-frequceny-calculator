#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 21 12:36:25 2021

@author: charan
"""
from selenium import webdriver
import streamlit as st
import pandas as pd
import base64
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import time
import datetime
import base64

 # background: #ff0099; 
 #  background: -webkit-linear-gradient(to right, #ff0099, #493240); 
 #  background: linear-gradient(to right, #ff0099, #493240);"

st.markdown("""
<style>
body {
  background: #ff0099; 
  background: -webkit-linear-gradient(to right, #ff0099, #493240); 
  background: linear-gradient(to right, #ff0099, #493240); 
}
</style>
    """, unsafe_allow_html=True)

# @st.cache(allow_output_mutation=True)
# def get_base64_of_bin_file(bin_file):
#     with open(bin_file, 'rb') as f:
#         data = f.read()
#     return base64.b64encode(data).decode()

# def set_png_as_page_bg(png_file):
#     bin_str = get_base64_of_bin_file(png_file)
#     page_bg_img = '''
#     <style>
#     body {
#     background-image: url("data:image/png;base64,%s");
#     background-size: cover;
#     }
#     </style>
#     ''' % bin_str
    
#     st.markdown(page_bg_img, unsafe_allow_html=True)
#     return
# set_png_as_page_bg('/home/charan/icc_try/backround.png')


start = datetime.datetime.strptime("2016-01-01", "%Y-%m-%d")
end = datetime.datetime.strptime("2021-01-01", "%Y-%m-%d")
date_array = \
    (start + datetime.timedelta(days=x) for x in range(0, (end-start).days))
l=[]


for date_object in date_array:
    l1=date_object.strftime("%Y-%m-%d")
    l.append(l1)






st.write("""
# THIS IS REPORT ON ICC CRICKET DATA OF LAST FIVE YEAR 

***
  this report says the frequcency of occurence of player(how many days he stayed in that position) at any postionin total five years
  that is from 2016 to 2020
***
""")



import sqlite3
conn = sqlite3.connect('/home/charan/icc_try/icc_5yr_odi.db')
c = conn.cursor()


pos=st.sidebar.selectbox('Rank', list(range(1,101)))

dates=st.sidebar.slider('stat-end',start,end,(start,end))



top_1_bowler=pd.read_sql_query("select Player,count(Player) frequency,Team from bowler where position=? and date between ? and ? group by Player order by frequency desc",conn,params=[pos,dates[0].strftime("%Y-%m-%d"),dates[1].strftime("%Y-%m-%d")])
top_1_batting=pd.read_sql_query("select Player,count(player) frequency,Team from batsmen where position=? and date between ? and ? group by Player order by frequency desc",conn,params=[pos,dates[0].strftime("%Y-%m-%d"),dates[1].strftime("%Y-%m-%d")])
top_1_allround=pd.read_sql_query("select Player,count(player) frequency,Team from all_rounder where position=? and date between ? and ? group by Player order by frequency desc",conn,params=[pos,dates[0].strftime("%Y-%m-%d"),dates[1].strftime("%Y-%m-%d")])
st.write("Bowlers")
#st.write(top_1_bowler)
st.dataframe(data=top_1_bowler, width=1024, height=1024)
st.write("Batsmen")
#st.write(top_1_batting)
st.dataframe(data=top_1_batting, width=1024, height=1024)
st.write("All Rounders")
#st.write(top_1_allround)
st.dataframe(data=top_1_allround, width=1024, height=1024)

