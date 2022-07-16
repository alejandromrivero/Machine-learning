import html5lib
from bs4 import BeautifulSoup
import requests
import json
from twython import Twython
from twython import TwythonStreamer


'''url="https://www.brainyquote.com/authors/jose_marti"
soup=BeautifulSoup(requests.get(url).text,'html5lib')
seleccion=soup.find_all('div')
divisions=soup.find_all('a',{'title':'view quote'})
quotes=soup.find_all('a',  {'title':'view quote'})
print (seleccion)
print (divisions)
print(len(divisions))
print (quotes)
print (len(quotes))'''

CONSUMER_KEY = "D93dZD0IALxBvoIKOJbpZKjEE"
CONSUMER_SECRET = "Zf5QlfGrtTbnIs5nK4mNzJmMHfQ8ivrjbxIvfaouZQ91LoupPh"
ACCESS_TOKEN = "1135000261-phFHJQ5khzUcpxU98GYTmmUAAZ8lYetepGp3aVV"
ACCESS_TOKEN_SECRET = "JMNNj3xgLNfpgSST3NRbOh7TvO0Em3q9hj4lrli6BVhlV"

def call_twitter_search_api():
    twitter = Twython(CONSUMER_KEY, CONSUMER_SECRET)

    for status in twitter.search(q=['venezuela'])["statuses"]:
        user = status["user"]["screen_name"].encode('utf-8')
        text = status["text"].encode('utf-8')
        print(user, ":", text)
        print()

call_twitter_search_api()

'''
tweets = []


class MyStreamer(TwythonStreamer):
    """our own subclass of TwythonStreamer that specifies
    how to interact with the stream"""

    def on_success(self, data):
        """what do we do when twitter sends us data?
        here data will be a Python object representing a tweet"""

        # only want to collect English-language tweets
        if data['lang'] == 'en':
            tweets.append(data)

        # stop when we've collected enough
        if len(tweets) >= 10000:
            self.disconnect()

    def on_error(self, status_code, data):
        print(status_code, data)
        self.disconnect()


def call_twitter_streaming_api():
    stream = MyStreamer(CONSUMER_KEY, CONSUMER_SECRET,
                        ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

    stream.statuses.filter(track='Data')
call_twitter_streaming_api()
'''
