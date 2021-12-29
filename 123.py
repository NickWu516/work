#網路文章樣式
import streamlit as st

import requests
from bs4 import BeautifulSoup
from datetime import datetime
import pandas as pd
import matplotlib.pyplot as plt
url = "https://rate.bot.com.tw/xrt?Lang=zh-TW"
resp = requests.get(url)
resp.encoding = 'utf-8'
html_soup = BeautifulSoup(resp.text, "lxml")
rate_table = html_soup.find('table', attrs={'title':'牌告匯率'}).find('tbody').find_all('tr')

st.title('幣值換算')
o=st.selectbox(
  '選擇幣值',
  ['美金','英鎊','歐元'])
  
if o=='美金':
  currency = rate_table[0].find('div', attrs={'class':'visible-phone print_hide'})
  st.write(currency.text.replace(" ", ""))  # 去掉所有的空白
  buyin_rate = rate_table[0].find('td', attrs={'data-table':'本行現金買入'})
  sellout_rate = rate_table[0].find('td', attrs={'data-table':'本行現金賣出'})
  st.write("即時現金買入: {}, 即時現金賣出: {}".format(buyin_rate.get_text(), sellout_rate.get_text()))
