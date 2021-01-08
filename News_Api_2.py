import requests
from bs4 import BeautifulSoup
import pprint
import pandas as pd
import numpy as np
from all_news import AllNews


def search_news_google():
    url = 'http://newsapi.org/v2/top-headlines?sources=google-news-in&apiKey=08dc63bcfab5447098da8363b8c9d802'
    response_12_20_google = requests.get(url)
    response_json_12_20_google = response_12_20_google.json()
    print('google')
    return format_news_from_api(response_json_12_20_google)


def search_news_times_of_india():
    url2 = 'http://newsapi.org/v2/top-headlines?country=in&apiKey=08dc63bcfab5447098da8363b8c9d802'
    response_12_20_time = requests.get(url2)
    response_json_12_20_time = response_12_20_time.json()
    print('Allindia')
    return format_news_from_api(response_json_12_20_time)


def format_news_from_api(all_articles):
    d = pd.json_normalize(all_articles['articles'])
    new_df = d[["description", "title", "publishedAt", "source.id"]]
    rank = 0
    all_news_list = []
    for index, row in new_df.iterrows():
        rank = rank + 1
        all_news = AllNews(row["description"], row["title"]
                           , category=None
                           , date_time=row["publishedAt"]
                           , rank=rank
                           , src=row["source.id"])
        print(all_news)
        all_news_list.append(all_news)
    return all_news_list
