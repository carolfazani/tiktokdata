from queryvalidation import QueryValidation
from selenium import webdriver
from time import sleep
from selenium.webdriver.firefox.options import Options
from selenium.common.exceptions import TimeoutException


class Requester(QueryValidation):

    def __init__(self, query, loadmore):
        super().__init__(query, loadmore)
        self.driver = None
        self.url = f"https://www.tiktok.com/search/video?q={query}"

    def get_url(self):
        options = Options()
        options.add_argument("--dns-prefetch-disable")
        self.driver = webdriver.Firefox(options=options)  # , executable_path="C:\\Program Files\BraveSoftware\\Brave-Browser\\Application\\brave.exe"
        self.driver.maximize_window()
        self.driver.implicitly_wait(20)

        try:
            self.driver.get(self.url)
            sleep(10)
            print('oi to aqui')

        except TimeoutException as ex:
            print(ex)

'''
requester = Requester("lula", 2)
requester.get_url()
'''