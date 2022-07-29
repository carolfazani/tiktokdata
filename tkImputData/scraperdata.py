from requester import Requester
from tqdm import tqdm
from selenium.webdriver.common.by import By
import json
import datetime
from time import sleep



class GeTData(Requester):
    def get_data(self):
        # Thread(target=captcha_loop).start() ---ainda não funciona

        for page in tqdm(range(1, self.loadmore + 1)):
            sleep(2)
            data_tiktok = self.driver.find_elements(By.XPATH, "//div[contains( @class ,'DivTimeTag')]")
            sleep(2)
            views_tiktok = self.driver.find_elements(By.XPATH, "//div[@data-e2e='search-card-like-container']//strong")
            sleep(2)
            url_tiktok = self.driver.find_elements(By.XPATH, "//div[@data-e2e='search_video-item']//a")
            sleep(2)
            hashtags_tiktok = self.driver.find_elements(By.XPATH, "//div[@data-e2e='search-card-video-caption']")
            sleep(2)
            channel_tiktok = self.driver.find_elements(By.XPATH, "//p[@data-e2e='search-card-user-unique-id']")
            sleep(2)
            self.driver.find_element(By.CSS_SELECTOR, 'button[data-e2e="search-load-more"]').click()

            with open(f"c:\\tiktokproject\\tkTransformData\\tiktok_video_info.json", 'w+', encoding='utf-8') as output:
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
                            data['query'] = self.query
                            data['load_more'] = self.loadmore
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


a = GeTData('lula', 1)
a.get_url()
a.get_data()
a.close_url()