import tweepy
import json
import pandas as pd
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener

#preprocessing 
consumer_key = 'YOUR-CONSUMER-KEY'
consumer_secret = 'YOUR-CONSUMER-SECRET'
access_token = 'YOUR-ACCESS-TOKEN'
access_secret = 'YOUR-ACCESS-SECRET'
 
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
 
api = tweepy.API(auth)

#streaming 
class MyListener(StreamListener):
     def on_data(self, data):
        try:
            with open('google.json', 'a') as f:
                f.write(data)
                return True
        except BaseException as e:
            print("Error on_data: %s" % str(e))
        return True

twitter_stream = Stream(auth, MyListener())
twitter_stream.filter(track=['#google'])

#loading
tweets_data = []
with open('C://Users//mac//Desktop//tweet_project//google.json', 'r') as tweets_file:
    for line in tweets_file:
        try:
            tweet = json.loads(line)
            tweets_data.append(tweet)
        except:
            continue
        
tweets = pd.DataFrame()

#output geo information
count = 0
validData = []
for i in range(len(tweets_data)):
    if (tweets_data[i]['place']!=None):
        count += 1
        validData.append(tweets_data[i]['place']['bounding_box']['coordinates'][0])

validData = pd.DataFrame(validData)
print('Number of my tweets: ',len(tweets_data))
print('Number of valid tweets: ',count)
print(\n)
print(validData)
