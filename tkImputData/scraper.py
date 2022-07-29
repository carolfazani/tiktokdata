import pandas as pd
import numpy as np
import re
import requests as rq
from bs4 import BeautifulSoup
from tqdm import tqdm
import glob
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.firefox.options import Options
# from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException
from captcha import *
from threading import Thread
import json
import datetime
from datetime import date, timedelta

# TODO: REFACTORER ESSE AQUI


class Scraper:

    def __init__(self, query: str, loadmore: int) -> None:
        self.__query = query
        self.__loadmore = loadmore
        self.url = f"https://www.tiktok.com/search/video?q={self.__query}"
        self.driver = None

    def __validate_data(self, query: str, loadmore: int):
        if isinstance(query, str) and isinstance(loadmore, int):
            return query, loadmore
        else:
            print('Entradas inválidas')


    def get_url(self):
        options = Options()
        options.add_argument("--dns-prefetch-disable")
        self.driver = webdriver.Firefox(options=options)  # , executable_path="C:\\Program Files\BraveSoftware\\Brave-Browser\\Application\\brave.exe"
        self.driver.maximize_window()
        self.driver.implicitly_wait(20)

        try:
            self.driver.get(self.url)
            sleep(10)

        except TimeoutException as ex:
            print(ex)


    def get_data(self):
        # Thread(target=captcha_loop).start() ---ainda não funciona

        for page in tqdm(range(1, self.__loadmore + 1)):
            time.sleep(2)
            data_tiktok = self.driver.find_elements(By.XPATH, "//div[contains( @class ,'DivTimeTag')]")
            time.sleep(2)
            views_tiktok = self.driver.find_elements(By.XPATH, "//div[@data-e2e='search-card-like-container']//strong")
            time.sleep(2)
            url_tiktok = self.driver.find_elements(By.XPATH, "//div[@data-e2e='search_video-item']//a")
            time.sleep(2)
            hashtags_tiktok = self.driver.find_elements(By.XPATH, "//div[@data-e2e='search-card-video-caption']")
            time.sleep(2)
            channel_tiktok = self.driver.find_elements(By.XPATH, "//p[@data-e2e='search-card-user-unique-id']")
            time.sleep(2)
            self.driver.find_element(By.CSS_SELECTOR, 'button[data-e2e="search-load-more"]').click()


            with open(f"tiktok_video_info.json", 'w+', encoding='utf-8') as output:
                data = dict()
                if len(data_tiktok) == len(views_tiktok) == len(url_tiktok):
                    for idx in range(len(url_tiktok)):
                        for e in url_tiktok:
                            data['content'] = url_tiktok[idx].get_attribute("href")
                        for e in views_tiktok:
                            data['views'] = views_tiktok[idx].text
                        for e in data_tiktok:
                            data['fetch_date'] = str(datetime.date.today())
                            data['content_date'] = data_tiktok[idx].text
                            data['query'] = self.__query
                            data['load_more'] = self.__loadmore
                        for e in hashtags_tiktok:
                            data['hashtags'] = hashtags_tiktok[idx].text
                        for e in channel_tiktok:
                            data['channel'] = channel_tiktok[idx].text
                        output.write("{}\n".format(json.dumps(data, ensure_ascii=False)))
                    print('Dados extraídos com sucesso')
                else:
                    print(f'informação inconsistente: {url_tiktok}')
                    pass

    def close_url(self):
        self.driver.close()


scraper = Scraper('lula', 1)
scraper.get_url()
scraper.get_data()
scraper.close_url()










