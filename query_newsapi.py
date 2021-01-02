from newsapi import NewsApiClient
from pandas.io.json import json_normalize
import pandas as pd
import json
from all_news import AllNews


def query_newsapi(query):
    print(query)
    # Init
    # newsapi = NewsApiClient(api_key='07c97109bbe442f9a44f30ee1ea92923')

    # newsapi.get_top_headlines(category=category,language='en', country=country)

    # /v2/everything
    # all_articles = newsapi.get_everything(q=query,
    #                                      sources='bbc-news',
    #                                      language='en',
    #                                      page=1,
    #                                      page_size=10)
    # return all_articles

    with open('data_all_news.txt') as f:
        all_articles = json.load(f)
    print(all_articles)
    d = pd.json_normalize(all_articles['articles'])
    newdf = d[["description", "title", "publishedAt", "source.id"]]
    rank = 0
    all_news_list = []
    for index, row in newdf.iterrows():
        rank = rank + 1
        all_news = AllNews(row["description"], row["title"]
                           , category=None
                           , date_time=row["publishedAt"]
                           , rank=rank
                           , src=row["source.id"])
        all_news_list.append(all_news)

    return all_news_list


if __name__ == '__main__':

    # all = query_newsapi("virus")
    # with open('data.txt', 'w') as outfile:
    #    json.dump(all, outfile)

    for x in query_newsapi('virus'):
        print(x)


'''

/Users/aaraj/.local/share/virtualenvs/MetaSearchNews-xss2mOSH/bin/python /Users/aaraj/PycharmProjects/MetaSearchNews/query_newsapi.py
{'status': 'ok', 'totalResults': 535, 'articles': [{'source': {'id': 'bbc-news', 'name': 'BBC News'}, 'author': 'https://www.facebook.com/bbcnews', 'title': 'Covid: Pandemic dampens New Year celebrations around the world', 'description': 'As the virus continues to spread in many countries, governments are set to crack down on revellers.', 'url': 'https://www.bbc.co.uk/news/world-55496464', 'urlToImage': 'https://ichef.bbci.co.uk/news/1024/branded_news/378D/production/_116312241_065009246.jpg', 'publishedAt': '2020-12-31T10:52:05Z', 'content': 'image captionWhat a difference a year makes: Sydney harbour on 31 December 2019 and 31 December 2020\\r\\nRestrictions are being placed on New Year festivities around the world as many countries struggle… [+3792 chars]'}, {'source': {'id': 'bbc-news', 'name': 'BBC News'}, 'author': 'https://www.facebook.com/bbcnews', 'title': 'Coronavirus spreads to Antarctic research station', 'description': 'The virus reaches all seven continents after 36 people test positive at a Chilean research station.', 'url': 'https://www.bbc.co.uk/news/world-latin-america-55410065', 'urlToImage': 'https://ichef.bbci.co.uk/news/1024/branded_news/7E73/production/_116217323_gettyimages-1204285729.jpg', 'publishedAt': '2020-12-22T15:20:36Z', 'content': 'image copyrightGetty Images\\r\\nimage captionThere have now been Covid cases on all seven continents\\r\\nCoronavirus has reached the Antarctic continent, which had so far been free of Covid-19.\\r\\nThe Chilea… [+1233 chars]'}, {'source': {'id': 'bbc-news', 'name': 'BBC News'}, 'author': 'https://www.facebook.com/bbcnews', 'title': 'Dr Deborah Birx: White House virus expert quits over holiday travel', 'description': 'Dr Deborah Birx says the criticism she has faced for a family get-together is "very difficult".', 'url': 'https://www.bbc.co.uk/news/world-us-canada-55419954', 'urlToImage': 'https://ichef.bbci.co.uk/news/1024/branded_news/B48E/production/_116222264_gettyimages-1226471390.jpg', 'publishedAt': '2020-12-22T23:37:47Z', 'content': 'image copyrightGetty Images\\r\\nA top public health official on the White House coronavirus task force has said she will retire after it emerged she hosted a holiday gathering.\\r\\nDr Deborah Birx, who is … [+2296 chars]'}, {'source': {'id': 'bbc-news', 'name': 'BBC News'}, 'author': 'https://www.facebook.com/bbcnews', 'title': 'China Covid-19: Nearly 500,000 in Wuhan may have had virus, says study', 'description': 'The study by Chinese officials suggests there were more positive cases in Wuhan than official figures suggest.', 'url': 'https://www.bbc.co.uk/news/world-asia-china-55481397', 'urlToImage': 'https://ichef.bbci.co.uk/news/1024/branded_news/A9E1/production/_116298434_gettyimages-1228264198.jpg', 'publishedAt': '2020-12-30T03:50:40Z', 'content': "image copyrightGetty Images\\r\\nimage captionThe study suggests that almost 5% of Wuhan's population might have been infected\\r\\nAlmost 5% of the people in the Chinese city of Wuhan may have been infected… [+1821 chars]"}, {'source': {'id': 'bbc-news', 'name': 'BBC News'}, 'author': 'https://www.facebook.com/bbcnews', 'title': 'Coronavirus updates: New virus variant continues to spread globally - BBC News', 'description': '<ol><li>Coronavirus updates: New virus variant continues to spread globally\xa0\xa0BBC News\\r\\n</li><li>UK Covid variant spreads more easily but does not lead to more severe disease, analysis confirms\xa0\xa0Telegraph.co.uk\\r\\n</li><li>S Africa tightens curfew, Spain COVID d…', 'url': 'https://www.bbc.co.uk/news/live/world-55473196', 'urlToImage': 'https://m.files.bbci.co.uk/modules/bbc-morph-news-waf-page-meta/5.1.0/bbc_news_logo.png', 'publishedAt': '2020-12-29T09:12:40Z', 'content': 'Yesterday, a health official warned that England\'s "very high" coronavirus infection level was a "growing concern" as the NHS continues to struggle to cope with rising patient numbers.\\r\\nThe number of… [+963 chars]'}, {'source': {'id': 'bbc-news', 'name': 'BBC News'}, 'author': 'https://www.facebook.com/bbcnews', 'title': 'Covid-19: Millions move into tier 3 of virus rules in England - BBC News', 'description': '<ol><li>Covid-19: Millions move into tier 3 of virus rules in England\xa0\xa0BBC News\\r\\n</li><li>Covid: Areas in England await Covid tier changes @BBC News live - BBC\xa0\xa0BBC\\r\\n</li><li>Toughest COVID-19 rules extended to much of south England\xa0\xa0The Associated Press\\r\\n</l…', 'url': 'https://www.bbc.co.uk/news/live/world-55345020', 'urlToImage': 'https://m.files.bbci.co.uk/modules/bbc-morph-news-waf-page-meta/5.1.0/bbc_news_logo.png', 'publishedAt': '2020-12-17T15:15:10Z', 'content': '"This storm feels different because the city was already slower paced because of Covid"Image caption: "This storm feels different because the city was already slower paced because of Covid"\\r\\nFor Nick… [+1242 chars]'}, {'source': {'id': 'bbc-news', 'name': 'BBC News'}, 'author': 'https://www.facebook.com/bbcnews', 'title': 'Coronavirus: Swiss count cost of surge in deaths', 'description': 'Swiss leaders decide on Friday whether to impose tougher measures, as deaths reach 100 a day.', 'url': 'https://www.bbc.co.uk/news/world-europe-55350118', 'urlToImage': 'https://ichef.bbci.co.uk/news/1024/branded_news/66A2/production/_116147262_hi064687611.jpg', 'publishedAt': '2020-12-18T00:07:19Z', 'content': 'By Imogen FoulkesBBC News, Bern\\r\\nimage captionAnother 102 deaths were announced on Thursday: here activists in Bern light candles for the thousands who have died\\r\\n"Not every death is a catastrophe." … [+4485 chars]'}, {'source': {'id': 'bbc-news', 'name': 'BBC News'}, 'author': 'https://www.facebook.com/bbcnews', 'title': "Sinovac: What do we know about China's Covid-19 vaccine?", 'description': 'The Sinovac vaccine is yet to finish late-stage trials, but is already being shipped to other countries.', 'url': 'https://www.bbc.co.uk/news/world-asia-china-55212787', 'urlToImage': 'https://ichef.bbci.co.uk/news/1024/branded_news/69A6/production/_115864072_gettyimages-1229946482.jpg', 'publishedAt': '2020-12-09T00:02:42Z', 'content': 'image copyrightGetty Images\\r\\nimage captionSinovac is a Beijing-based pharmaceutical company\\r\\nAs the global race to produce a Covid-19 vaccine continues, China appears to have made huge strides, with … [+5609 chars]'}, {'source': {'id': 'bbc-news', 'name': 'BBC News'}, 'author': 'https://www.facebook.com/bbcnews', 'title': 'Sydney Covid cases drop amid record testing', 'description': "Australia's largest city has recorded its fewest number of new coronavirus cases in several days.", 'url': 'https://www.bbc.co.uk/news/world-australia-55406969', 'urlToImage': 'https://ichef.bbci.co.uk/news/1024/branded_news/CED6/production/_116205925_gettyimages-1292424859.jpg', 'publishedAt': '2020-12-22T02:57:52Z', 'content': 'image captionMore than 44,000 people were tested in a single day, officials said\\r\\nSydney has recorded its fewest number of new coronavirus cases in several days, raising hopes the Australian city may… [+3247 chars]'}, {'source': {'id': 'bbc-news', 'name': 'BBC News'}, 'author': 'https://www.facebook.com/bbcnews', 'title': 'Covid: Thailand tests thousands after virus outbreak in seafood market', 'description': "Tens of thousands will be tested after hundreds of cases linked to Thailand's biggest seafood market.", 'url': 'https://www.bbc.co.uk/news/world-asia-55391417', 'urlToImage': 'https://ichef.bbci.co.uk/news/1024/branded_news/B6ED/production/_116192864_gettyimages-1230204366.jpg', 'publishedAt': '2020-12-21T04:46:44Z', 'content': "image captionThe outbreak has largely impacted the Myanmar migrant workers who toil in Thailand's seafood industry\\r\\nAfter months of avoiding the surge in cases seen by its neighbours, Thailand has be… [+3092 chars]"}]}

Process finished with exit code 0


'''
