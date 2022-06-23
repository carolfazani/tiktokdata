import pandas as pd
import numpy as np
import re
import time
import requests as rq
from bs4 import BeautifulSoup
from tqdm import tqdm
import glob
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.firefox.options import Options
#from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException
import time
from captcha import *
from threading import Thread
import json
import datetime


def searchtiktok():
    options = Options()
    #options.add_argument('--headless')
    options.add_argument("--dns-prefetch-disable")
    driver = webdriver.Firefox(options=options) #, executable_path="C:\\Program Files\BraveSoftware\\Brave-Browser\\Application\\brave.exe"
    driver.maximize_window()
    driver.implicitly_wait(20)
    query = 'lula'

    tiktok = f"https://www.tiktok.com/search/video?q={query}"
    load_more = 2


    try:
        driver.get(tiktok)
        sleep(10)
    except TimeoutException as ex:
        print(ex)

    #Thread(target=captcha_loop).start() ---ainda não funciona

    for page in tqdm(range(1, load_more + 1)):
        time.sleep(2)
        data_tiktok = driver.find_elements(By.XPATH, "//div[contains( @class ,'DivTimeTag')]")
        time.sleep(2)
        views_tiktok= driver.find_elements(By.XPATH, "//div[@data-e2e='search-card-like-container']//strong")
        time.sleep(2)
        url_tiktok= driver.find_elements(By.XPATH, "//div[@data-e2e='search_video-item']//a")
        time.sleep(2)
        hashtags_tiktok = driver.find_elements(By.XPATH, "//div[@data-e2e='search-card-video-caption']")
        time.sleep(2)
        channel_tiktok = driver.find_elements(By.XPATH, "//p[@data-e2e='search-card-user-unique-id']")
        time.sleep(2)
        driver.find_element(By.CSS_SELECTOR, 'button[data-e2e="search-load-more"]').click()


        with open(f"tiktok_video_info.json", 'w+', encoding='utf-8') as output:
            data = dict()
            if len(data_tiktok) ==  len(views_tiktok) == len(url_tiktok): # == len(hashtag_tiktok)
                for idx in range(len(url_tiktok)):
                    for e in url_tiktok:
                        data['content'] = url_tiktok[idx].get_attribute("href")
                    for e in views_tiktok:
                        data['views'] = views_tiktok[idx].text
                    for e in data_tiktok:
                        data['fetch_date'] = str(datetime.date.today())
                        data['content_date']= data_tiktok[idx].text
                        data['query'] = query
                        data['load_more'] = load_more
                    for e in hashtags_tiktok:
                        data['hashtags']= hashtags_tiktok[idx].text
                    for e in channel_tiktok:
                        data['channel'] = channel_tiktok[idx].text
                    output.write("{}\n".format(json.dumps(data,ensure_ascii=False)))
    driver.close()


def cleandata():
    df = pd.read_json("tiktok_video_info.json", lines=True)
    date = datetime.date.today()
    year = date.strftime("%Y")
    df['content'] = df['content']
    df['views'] = df['views'].replace({"K": "*1e3", "M": "*1e6"}, regex=True).map(pd.eval).astype(int)
    df['content_date'] = [year + "-" + d if len(d) <= 5 else d for d in df['content_date']]
    df['content_date'] = pd.to_datetime(df['content_date'], yearfirst= True, format= '%Y-%m-%d')
    df['fetch_date'] = pd.to_datetime(df['fetch_date'], yearfirst= True, format= '%Y-%m-%d')
    df['offset_days']= df['fetch_date'] - df['content_date']
    df['offset_days'] = df['offset_days'].dt.days.astype('int16')
    df['daily_views'] = round(df['views'] // df['offset_days'])
    df.to_json("tiktok_video_clean.json", orient='records', lines=True, force_ascii=False)
    df.to_csv(r'tiktok_video_clean.csv', index=None)



'''
    >> metodo replace (~) para substituir K e M por * 1e3 e * 1e6 , respectivamente
    >>regex = True é necessário se quisermos que a string da chave seja substituída por uma string de valor 
    (por exemplo, K substituído por "* 1e3" neste caso) 
    >>1e3 é a notação científica de 1000 
    >> (pd.eval) : avalia matematicamente cada valor usando map 
    >>  método Series ' map (~) aplica o método pd.eval (~) a cada um dos valores.
    >> astype (int) : converte todos os valores em inteiros
    
'''




if  __name__  ==  "__main__" :
    searchtiktok()
    #cleandata()
