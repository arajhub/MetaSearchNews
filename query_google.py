#https://github.com/googleapis/google-api-python-client/tree/master/samples

import asyncio
from GoogleNews import GoogleNews

class GoogleApi:
    def __init__(self):
        self._api = self._get_api()
def _get_news_for_word(self, word, top):
        self._api.search(word)
        text = self._api.result()
        news = list(map(lambda x: self._clean(x['title']) + ' @ (' + x['date'] + ')', text))[:top]
        return news

def _get_api(self):
        return GoogleNews(period="1w")

async def get_news_for_words(self, target_words, top=3):
        text = {}
        for word in target_words:
            ts = self._get_news_for_word(word, top)
            text[word] = ts
        return text

async def get_top_news(self):
        return self._api.top_news()
async def main():
    """
    Main method, call the appropriate methods
    :return:
    """
    google_api = GoogleApi()
    users = google_api.get_news_for_words(['bloomberg', 'cnbc'], 2)

    print('LOCATION NEWS')
    for location, news in trends_text.items():
        print(f'Location: {location}  \n {news}')
    print('\nWORD NEWS')
    for word, news in words_text.items():
        print(f'Word: {word}  \n {news}')
    print('\nUSER NEWS')
    for user, news in news_users.items():
        print(f'User: {user}  \n {news}')
    if __name__ == "__main__":
        loop = asyncio.get_event_loop()
        loop.run_until_complete(asyncio.wait([main()]))