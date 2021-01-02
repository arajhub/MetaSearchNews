from query_newsapi import query_newsapi
from query_google import query_google_news


def search_news():
    # print(query)
    print("Welcome to Meta News Search")
    query = input("Input your search query")
    result_from_all = query_newsapi(query) + query_google_news(query)
    for res in result_from_all:
        print(res)

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
        raise NotImplementedError

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
