import requests
import pandas as pd
import numpy as np
import re
import time
import requests as rq
from bs4 import BeautifulSoup
import os
from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

def download_video():

    options = Options()
    #options.add_argument('--headless')
    options.add_argument("--dns-prefetch-disable")
    driver = webdriver.Chrome(options=options) #, executable_path="C:\\Program Files\BraveSoftware\\Brave-Browser\\Application\\brave.exe"
    driver.maximize_window()
    downloader = 'https://snaptik.app/en'
    url = "https://www.tiktok.com/@lulanotiktok/video/7037255470410665222"
    wait = WebDriverWait(driver, 80)

    try:
        driver.get(downloader)
    except TimeoutException as ex:
        print(ex)


    inputTexto = driver.find_element_by_id('url')
    inputTexto.send_keys(url)
    sleep(3)
    button = driver.find_elements_by_xpath('//*[@id="submiturl"]/span')
    button[0].click()

    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[onclick='if(!window.__cfRLUnblockHandlers)returnfalse;hiddenAlert()']"))).click()

    #TODO: capturar href, abrir e salvar
    href = driver.find_elements('a', attrs={'href': re.compile(r"/tikcdn")})
    print(href)
    r = requests.get(href)
    with open(f'testeee.mp4', "wb") as f:
        f.write(r.content)




if __name__ == "__main__":
    download_video()
