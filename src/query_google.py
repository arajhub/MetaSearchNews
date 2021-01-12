from GoogleNews import GoogleNews
from src.all_news import AllNews


# googlenews = GoogleNews()
# googlenews = GoogleNews(lang='en')
# googlenews.get_news('virus')
# data_google = googlenews.results()
# print(all)


# def myconverter(o):
#    if isinstance(o, datetime.datetime):
#        return o.__str__()


# with open('data_google.txt', 'w') as outfile:
#    json.dump(data_google, default=myconverter, fp=outfile)


def query_google_news(query):

    googlenews = GoogleNews(lang='en')
    googlenews.get_news(query)
    res = googlenews.results()

    # with open('data_google.txt') as f:
    #     res = json.load(f)
    print(res)
    rank = 0
    all_news_list = []
    for news in res:
        rank = rank + 1
        if rank < 51:
            all_news = AllNews(news["desc"], news["title"]
                               , category=None
                               , date_time=news["datetime"]
                               , rank=rank
                               , src='google')
        else:
            break
        all_news_list.append(all_news)
    return all_news_list


if __name__ == '__main__':
    result = query_google_news('virus')
    for r in result:
        print(r)
