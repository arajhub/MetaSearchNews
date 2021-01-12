from src.query_newsapi import query_newsapi
from src.query_google import query_google_news
import pandas as pd
from collections import Counter
import operator
import nltk
from nltk.corpus import stopwords

from src.all_news import AllNews
from src.documents import Document
from src.documents import Non_rel_doc
from src.prox import *
from src.check import *
from src.word_set import Word_set
import News_Api_2


def stopWordElimination(all_words):
    stop_words = [line.rstrip('\n') for line in open('stop_words.txt')]
    stop_words += stopwords.words('english')
    w = [word for word in all_words if word not in stop_words if word.isalpha()]
    return w


def split(string):
    all_words = nltk.word_tokenize(string)
    aft_elimination = stopWordElimination(all_words)
    return aft_elimination


def search_news():
    while True:

        print("Welcome to Meta News Search")
        original_q = input("Input your search query")

        result = query_newsapi(original_q) + query_google_news(original_q)
        #result = News_Api_2.search_news_google() + News_Api_2.search_news_times_of_india()
        '''
        1: (Best Rank approach)
        This approach, place a URL at the best rank it gets in any of the search engine rankings.
        That is,
        MetaRank (x) = Min(Rankof searchengine1(x),Rankof searchengine2(x))
        // MetaRank refers rank assigned by meta Search engine
    
        '''
        # done use any ranking
        result = best_rank(result)
        #result = custom_rank(result)
        docs = []
        scores_all = []
        Document.count = 0
        Document.relevance_count = 0
        Rel_doc.count = 0
        Non_rel_doc.count = 0

        for x in result:
            print("\n Result :", x.rank)
            print("\nTitle: " + x.title)
            print("summary: " + x.summary)
            print("date_time: " + str(x.date_time))
            print("rank: " + str(x.rank))

            # nltk.download('punkt')
            # nltk.download('stopwords')

            # Tokenize the words
            print(nltk.word_tokenize(original_q))
            q = nltk.word_tokenize(original_q)[0]
            title = split(str(x.title.lower()))
            desc = split(str(x.summary.lower()))
            scores_all.append(proximity(title, q))
            scores_all.append(proximity(desc, q))

            tokens = split(str(x.title.lower()) + " " + str(
                x.summary.lower()))
            words = dict(Counter(tokens))

            docs.append(Document(words, 1))

        # Number of relevant documents
        relevance_count = docs.count

        finalset = list(Word_set.dict_wrd_freq.keys())

        for d in docs:
            d.wset.update_set()
            for w in Word_set.dict_wrd_freq.keys():
                d.wset.weights[w] = d.wset.dict_wrd_freq[w] * math.log(n / Word_set.dict_doc_freq[w])

        # Proximity Finalization
        for w in Word_set.dict_wrd_freq.keys():
            sc = 0
            for i in range(0, len(scores_all)):
                for j in range(0, len(scores_all[i])):
                    if scores_all[i][j][0] == w:
                        sc += scores_all[i][j][1]

            Word_set.prox[w] = sc

        top_ten = {}

        for j in range(0, 10):
            top_ten[w] = Word_set.prox[w]

        top_ten_prox_dict = sorted(top_ten.items(), key=operator.itemgetter(1), reverse=True)

        print(top_ten_prox_dict)

    # TODO:

    '''
    Task
    3: Ranking
    a) Approach
   
    '''


def best_rank(all_search_result):
    df = pd.DataFrame([t.__dict__ for t in all_search_result])
    grouped_by_title = df.groupby('title')
    all_news_ranked = []
    meta_rank = 0
    for key, values in grouped_by_title:
        all_news = AllNews(summary=values['summary'].iloc[0]
                           , title=values['title'].iloc[0]
                           , category=values['category'].iloc[0]
                           , date_time=values['date_time'].iloc[0]
                           , rank=min(values['rank'])
                           , src=values['src'].iloc[0]
                           , meta_rank=meta_rank)
        all_news_ranked.append(all_news)
    ranked_news = pd.DataFrame([t.__dict__ for t in all_news_ranked])
    ranked_news.sort_values(by='rank', inplace=True)
    ranked_news.reset_index(drop=True, inplace=True)
    all_news_list = []
    for index in range(0, len(ranked_news)):
        meta_rank = meta_rank + 1
        ranked_news.at[index, 'meta_rank'] = meta_rank
        all_news = AllNews(ranked_news._get_value(index, 'summary'), ranked_news._get_value(index, 'title')
                           , category=ranked_news._get_value(index, 'category')
                           , date_time=ranked_news._get_value(index, 'date_time')
                           , rank=ranked_news._get_value(index, 'rank')
                           , src=ranked_news._get_value(index, 'src')
                           , meta_rank=ranked_news._get_value(index, 'meta_rank'))
        all_news_list.append(all_news)
    ranked_news.to_csv(r'ResultantRanks_A1.txt', header=True, sep='\t', mode='w')
    return all_news_list

    '''
    b) Approach 2:
    Propose your own method for ranking the news documents from the Aggregated News
    Collection (Taks2)
    Write the results in the document named ResultantRanks_A2.txt
    
    Proximity based approach
    '''


def custom_rank(all_search_result):
    ranked_news = pd.DataFrame([t.__dict__ for t in all_search_result])
    ranked_news.sort_values(by='src', inplace=True)
    ranked_news.reset_index(drop=True, inplace=True)
    meta_rank = 0
    all_news_list = []
    for index in range(0, len(ranked_news)):
        meta_rank = meta_rank + 1
        ranked_news.at[index, 'meta_rank'] = meta_rank
        all_news = AllNews(ranked_news._get_value(index,'summary'), ranked_news._get_value(index,'title')
                           , category=ranked_news._get_value(index,'category')
                           , date_time=ranked_news._get_value(index,'date_time')
                           , rank=ranked_news._get_value(index,'rank')
                           , src=ranked_news._get_value(index,'src')
                           , meta_rank=ranked_news._get_value(index,'meta_rank'))
        all_news_list.append(all_news)
    ranked_news.to_csv(r'ResultantRanks_A2.txt', header=True, sep='\t', mode='w')
    return all_news_list


def Initial(augment, modified_q, curr_precision):
    print("Total no of results : ", n)
    print("Bing Search Results:")
    return


def Second(augment, modified_q, curr_precision):
    print("Current Precision   = ", curr_precision)
    print("Augmenting With     = ", augment)
    print("Modified Query = ", modified_q)
    Initial(None, None, None)
    return


def Final(augment, modified_q, curr_precision):
    print("Final Precision =", curr_precision)
    print("Final Query =", modified_q)
    print("Desired precision reached!!")
    sys.exit()


switch = {0: Initial,
          1: Second,
          2: Final
          }


def display(flag, augment=None, modified_q=None, curr_precision=None):
    print("\nParameters:")
    # print("Original Query      = ", original_q)
    print("Desired Precision   = ", Query.precision)
    switch[flag](augment, modified_q, curr_precision)
    return


if __name__ == '__main__':
    # nltk.download()
    search_news()
