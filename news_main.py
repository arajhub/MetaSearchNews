from all_news import AllNews
from query_newsapi import query_newsapi
from query_google import query_google_news
import pandas as pd
import News_Api_2


def search_news():
    # print(query)
    print("Welcome to Meta News Search")
    query = input("Input your search query")
    result_from_all = query_newsapi(query) + query_google_news(query)
    # result_from_all = News_Api_2.search_news_google() + News_Api_2.search_news_times_of_india()
    # for res in result_from_all:
    #     print(res)
    best_rank(result_from_all)
    # TODO:

    '''
    Task
    3: Ranking
    a) Approach
    1: (Best Rank approach)
    This approach, place a URL at the best rank it gets in any of the search engine rankings.
    That is,
    MetaRank (x) = Min(Rankof searchengine1(x),Rankof searchengine2(x))
    // MetaRank refers rank assigned by meta Search engine
    
    '''


def best_rank(all_search_result):
    df = pd.DataFrame([t.__dict__ for t in all_search_result])
    grouped_by_title = df.groupby('title')
    all_news_ranked = []
    for key, values in grouped_by_title:
        all_news_ranked.append(dict(type=key, items=min(values['rank'])))
    ranked_news = pd.DataFrame([t for t in all_news_ranked])
    print('After ranking')
    print(ranked_news.sort_values(by='items'))

    '''
    b) Approach 2:
    Propose your own method for ranking the news documents from the Aggregated News
    Collection (Taks2)
    Write the results in the document named ResultantRanks_A2.txt
    '''


def custom_rank(all_search_result):
    raise NotImplementedError


if __name__ == '__main__':
    search_news()
