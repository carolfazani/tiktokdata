from search import cleandata
from dbconnector import Mydb


def tk_content():
    mydb = Mydb()
    df = cleandata()

    insert_data = f'''INSERT ignore into tk_content (query, content, fetch_date, content_date, views, hashtags, daily_views, offset_days, load_more) VALUES'''
    for index, d in df.iterrows():
        query = d['query']
        content = d['content']
        fetch_date = d['fetch_date']
        content_date = d['content_date']
        views = d['views']
        hashtags =d['hashtags']
        daily_views = d['daily_views']
        offset_days = d['offset_days']
        load_more = d['load_more']

        insert_data += f'''('{query}', '{content}', '{fetch_date}', '{content_date}', {views}, '{hashtags}', '{daily_views}', '{offset_days}', '{load_more}'), '''
        print(insert_data)
    mydb.execsql(insert_data[:insert_data.rfind(',')])


if  __name__  ==  "__main__" :
    tk_content()