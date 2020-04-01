import pandas as pd
import requests
from bs4 import BeautifulSoup

no_of_tweets_to_extract = 50000

id_file = pd.read_csv("../../data sets/corona_tweets_01.csv", usecols=[0], nrows=no_of_tweets_to_extract)

tweet_ids = []
tweets = []
no_of_extracted_tweets = 0

for tweet_id in id_file['tweet_id']:
    print('Extracted ', no_of_extracted_tweets, ' of ', no_of_tweets_to_extract, ' tweets.\n',
          (no_of_extracted_tweets / no_of_tweets_to_extract) * 100, '% done')
    tweet_url = 'https://twitter.com/user/status/' + str(tweet_id)
    response = requests.get(tweet_url).text
    page_content = BeautifulSoup(response, 'html.parser')
    tweet = page_content.find_all('p', {'class': 'TweetTextSize TweetTextSize--jumbo js-tweet-text tweet-text'})
    # print(tweet_id, ' -> ', tweet)
    if len(tweet) > 0:
        tweet_ids.append(tweet_id)
        tweets.append(tweet[0].text)
    no_of_extracted_tweets = no_of_extracted_tweets + 1
    # print(tweet_id, " -> ", tweet[0].text)

print('Tweets extraction completed. Creating data set...')
tweet_dic = {'tweet_id': tweet_ids, 'tweet': tweets}
df = pd.DataFrame(tweet_dic)
df.to_csv('../../data sets/test.csv')
print('Data set created')
