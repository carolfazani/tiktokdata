from tkDatabase.dbconnector import Mydb
from tkTransformData.cleandata import Cleandata
import pandas as pd

class SaveSQL():


    def __init__(self):
        self.mydb = Mydb()
        self.mydb.open()
        self.df = Cleandata()
        self.df = self.df.dataframe()

    def tk_content(self):
        insert_data = f'''INSERT ignore into tk_content (query, content, fetch_date, content_date, views, hashtags, daily_views, offset_days, load_more, channel) VALUES'''
        for index, d in self.df.iterrows():
            query = d['query']
            content = d['content']
            fetch_date = d['fetch_date']
            content_date = d['content_date']
            views = d['views']
            hashtags =d['hashtags']
            daily_views = d['daily_views']
            offset_days = d['offset_days']
            load_more = d['load_more']
            channel = d['channel']

            insert_data += f'''('{query}', '{content}', '{fetch_date}', '{content_date}', {views}, '{hashtags}', '{daily_views}', '{offset_days}', '{load_more}', '{channel}'), '''
        self.mydb.query(insert_data[:insert_data.rfind(',')], commit=True)
        self.mydb.close()

savesql = SaveSQL()
savesql.tk_content()


