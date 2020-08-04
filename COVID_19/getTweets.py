import os
import time
from datetime import date, datetime

import pandas as pd
import tweepy as tp

# Twitter credentials for the app
CONSUMER_KEY = 'GWjJzHWaHOmNycuNtlyKI9F0U'
CONSUMER_SECRET = 'SNPAyWBfjOXDAZXELy3m8CWXjzDl1NP22SIPZEbudz9A2LOrMO'
ACCESS_KEY = '368305011-U0G3Cs9hdu5GymkknoroHrVI5Tbywh6aSzGCqDhT'
ACCESS_SECRET = 'iELOscP633TfOh2DyWhlfQu4FrZoaZuMVWynpUGgSjrmg'

# pass twitter credentials to tweepy
auth = tp.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tp.API(auth)


def get_tweets(search_keys, num_tweets_per_run, date_since, date_till=date.today(), num_runs=1):
    tweets_df = pd.DataFrame(columns=['tweet_id', 'user_name', 'tweet_location', 'tweet_time',
                                      'tweet_text'])

    # for 'num_runs' iterations
    for i in range(num_runs):
        start_time = time.time()
        df_len = 0

        print('Getting tweets from tweeter on run #{}'.format(i + 1))
        tweets = tp.Cursor(
            api.search,
            q=search_keys,
            lang='en',
            since=date_since,
            until=date_till,
            tweet_mode='extended'
        ).items(num_tweets_per_run)
        print('Got tweets. Now processing on run #{}'.format(i + 1))
        tweet_list = [tweet for tweet in tweets]

        # print(tweet_list[0])
        for tweet in tweet_list:
            p_time_start = time.time()
            tweet_id = tweet.id
            user_name = tweet.user.screen_name
            tweet_location = tweet.user.location
            tweet_time = tweet.created_at
            try:  # if it is a retweet
                tweet_text = tweet.retweeted_status.full_text
            except AttributeError:  # not a retweet
                tweet_text = tweet.full_text

            tweets_df.loc[df_len] = [tweet_id, user_name, tweet_location, tweet_time, tweet_text]
            df_len += 1
            p_time_end = time.time()
            p_duration = round(p_time_end - p_time_start, 2)
            if df_len % 100 == 0:
                print('Processed {} tweets of {} tweets in {} seconds.'.
                      format(df_len, num_tweets_per_run, p_duration))
        end_time = time.time()
        duration = round(end_time - start_time, 2)
        print('Run #{} complete. TIme taken {}s.\nSaving the data frame to .csv...'.format(i + 1, duration))
        timestamp = datetime.today().strftime('%Y_%m_%d__%H%M%S')
        path = os.getcwd()
        filename = path + '/data/' + timestamp + '_covid_19_tweets.csv'
        tweets_df.to_csv(filename, index=False)
        print('Data frame saved for run #{}'.format(i + 1))
        print('***********************************\nGoing to Sleep for 15 minutes\n')
        time.sleep(910)


# Initialise these variables:
search_words = "corona OR covid OR covid19 OR COVIDー19 OR covid-19 OR CoronaVirus OR" \
               "StayHome OR StayAtHome OR StayHomeStaySafe -filter:retweets"
date_from = "2020-06-03"
numTweets = 2500
numRuns = 3
# Call the function
get_tweets(search_words, numTweets, date_from, num_runs=numRuns)
