import pandas as pd
from datetime import timedelta
import datetime
import numpy as np



class Cleandata():

    def __init__(self):
        self.df = pd.read_json("c:\\tiktokproject\\tkTransformData\\tiktok_video_info.json", lines=True)
        self.content()
        self.views()
        self.fetch_date()
        self.content_date()
        self.offset_days()
        self.daily_views()



    def content(self):
        self.df['content'] = self.df['content']
        return self.df['content']

    def views(self):
        self.df['views'] = self.df['views'].replace({"K": "*1e3", "M": "*1e6"}, regex=True).map(pd.eval).astype(int)
        return self.df['views']

    def fetch_date(self):
        self.df['fetch_date'] = pd.to_datetime(self.df['fetch_date'], yearfirst=True, format='%Y-%m-%d')
        return self.df['fetch_date']

    def content_date(self):
        date = datetime.date.today()
        year = date.strftime("%Y")
        self.df['content_date'] = [year + "-" + d if len(d) <= 5 else date - timedelta(days=int(d[0])) if d[1] == 'd' else date if d[1] or d[
                2] == 'h' else date - timedelta(weeks=int(d[0])) if d[1] == 'w' else d for d in self.df['content_date']]
        self.df['content_date'] = pd.to_datetime(self.df['content_date'], yearfirst=True, format='%Y-%m-%d')
        return self.df['content_date']

    def offset_days(self):
        # tratar o zero aqui
        self.df['offset_days'] = self.df['fetch_date'] - self.df['content_date']
        self.df['offset_days'] = self.df['offset_days'].dt.days.astype('int16')
        return self.df['offset_days']

    def daily_views(self):
        self.df['daily_views'] = round(self.df['views'] / self.df['offset_days']) if self.df['offset_days'][0] != np.int64(0) else self.df['views']
        return self.df['daily_views']

    def datacsv(self):
        return self.df.to_csv(r'c:\\tiktokproject\\tkOutputData\\tiktok_video_clean.csv', index=None)

    def dataframe(self):
        return self.df







