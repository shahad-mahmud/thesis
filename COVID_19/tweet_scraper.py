import pandas as pd
import requests
from bs4 import BeautifulSoup
import os

no_of_tweets_to_extract = 3000
rows_to_skip = 11000

id_file = pd.read_csv("../../data sets/corona_tweets_01.csv", usecols=[0],
                      nrows=rows_to_skip + no_of_tweets_to_extract +5)
print(id_file.head(5))
tweet_ids = []
tweets = []
no_of_extracted_tweets = 0
# file = open('tweets_01.csv', 'a')

# os.remove("extracted_tweets_01.csv")

for tweet_id in id_file['tweet_id'][rows_to_skip:rows_to_skip + no_of_tweets_to_extract]:
    #     file = open('tweets_01.csv', 'a')
    print('Extracted ', no_of_extracted_tweets, ' of ', no_of_tweets_to_extract, ' tweets.\n',
          (no_of_extracted_tweets / no_of_tweets_to_extract) * 100, '% done')
    tweet_url = 'https://twitter.com/user/status/' + str(tweet_id)
    response = requests.get(tweet_url).text
    page_content = BeautifulSoup(response, 'html.parser')
    tweet = page_content.find_all('p', {'class': 'TweetTextSize TweetTextSize--jumbo js-tweet-text tweet-text'})
    # print(tweet_id, ' -> ', tweet)
    if len(tweet) > 0:
        #         s = str(tweet_id) + ',' + tweet[0].text +'\n'
        #         file.write(s)
        tweet_ids.append(tweet_id)
        tweets.append(tweet[0].text)
    if no_of_extracted_tweets % 5 == 0:
        print('Adding to data set...')
        d = {'tweet_id': tweet_ids, 'tweet': tweets}
        df = pd.DataFrame(d)
        df.to_csv('../../data sets/working/extracted_tweets_01_short.csv', mode='a', header=False, index=False)
        tweet_ids = []
        tweets = []
        print('Added to data set!\n')
    no_of_extracted_tweets = no_of_extracted_tweets + 1
    # print(tweet_id, " -> ", tweet[0].text)
#     file.close()

print('Tweets extraction completed. Completiong data set...')
tweet_dic = {'tweet_id': tweet_ids, 'tweet': tweets}
df = pd.DataFrame(tweet_dic)
df.to_csv('../../data sets/working/extracted_tweets_01_short.csv', mode='a', header=False, index=False)
# file.close()
print('Data set completed')
