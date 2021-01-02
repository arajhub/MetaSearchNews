#News Search API from BING
#https://github.com/MicrosoftDocs/bing-docs/blob/master/bing-docs/bing-news-search/quickstarts/sdk/news-search-client-library-python.md


from azure.cognitiveservices.search.newssearch import NewsSearchClient
from msrest.authentication import CognitiveServicesCredentials
from all_news import AllNews


subscription_key = "YOUR-SUBSCRIPTION-KEY"
endpoint = "YOUR-ENDPOINT"






def search_bing(query):

    client = NewsSearchClient(endpoint=endpoint, credentials=CognitiveServicesCredentials(subscription_key))

    search_term = query
    news_result = client.news.search(query=search_term, count=10)
    # news_result = client.news.search(query=search_term, market="en-us", count=10)

    print(news_result)

    bing_news_list = []

    '''
    Extract only 
    1. summary/snippet 
    2. the title
    3. Category and date&time
    '''

    '''
    if news_result.value:
        first_news_result = news_result.value[0]
        print("Total estimated matches value: {}".format(
            news_result.total_estimated_matches))
        print("News result count: {}".format(len(news_result.value)))
        print("First news name: {}".format(first_news_result.name))
        print("First news url: {}".format(first_news_result.url))
        print("First news description: {}".format(first_news_result.description))
        print("First published time: {}".format(first_news_result.date_published))
        print("First news provider: {}".format(first_news_result.provider[0].name))
    else:
        print("Didn't see any news result data..")
        
    '''
    # TODO: Add category
    if news_result.value:
        rank = 0
        print("Total estimated matches value: {}".format(
            news_result.total_estimated_matches))
        for news in news_result.value:
            rank = rank + 1
            all_news =  AllNews(summary=news.description, title=news.name, category=None, date_time=news.date_published,rank=rank)
            bing_news_list.append(all_news)
    else:
        print("Didn't see any news result data..")











