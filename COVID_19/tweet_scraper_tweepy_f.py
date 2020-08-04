import os
import time

import pandas as pd
import tweepy

# Twitter credentials for the app
consumer_key = 'GWjJzHWaHOmNycuNtlyKI9F0U'
consumer_secret = 'SNPAyWBfjOXDAZXELy3m8CWXjzDl1NP22SIPZEbudz9A2LOrMO'
access_key = '368305011-U0G3Cs9hdu5GymkknoroHrVI5Tbywh6aSzGCqDhT'
access_secret = 'iELOscP633TfOh2DyWhlfQu4FrZoaZuMVWynpUGgSjrmg'

# pass twitter credentials to tweepy
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth)


def scrap_tweets(search_words, date_since, numTweets, numRuns):
    db_tweets = pd.DataFrame(columns=['tweet_id', 'user_name', 'user_location', 'tweet_time', 're_tweets',
                                      'tweet_text', 'hash_tags'])
    # Define a for-loop to generate tweets at regular intervals
    for i in range(0, numRuns):
        # We will time how long it takes to scrape tweets for each run:
        start_run = time.time()
        tweets = tweepy.Cursor(api.search, q=search_words, lang="en", since=date_since, tweet_mode='extended').items(
            numTweets)
        tweet_list = [tweet for tweet in tweets]

        # Obtain the following info (methods to call them out):
        # user.screen_name - twitter handle
        # user.description - description of account
        # user.location - where is he tweeting from
        # user.friends_count - no. of other users that user is following (following)
        # user.followers_count - no. of other users who are following this user (followers)
        # user.statuses_count - total tweets by user
        # user.created_at - when the user account was created
        # created_at - when the tweet was created
        # retweet_count - no. of retweets
        # (deprecated) user.favourites_count - probably total no. of tweets that is favourited by user
        # retweeted_status.full_text - full text of the tweet
        # tweet.entities['hashtags'] - hashtags in the tweet

        # Begin scraping the tweets individually:
        noTweets = 0

        for tweet in tweet_list:
            # print(tweet)

            # Pull the values
            tweet_id = tweet.id
            username = tweet.user.screen_name
            location = tweet.user.location
            tweetcreatedts = tweet.created_at
            retweetcount = tweet.retweet_count
            hashtags = tweet.entities['hashtags']

            try:
                text = tweet.retweeted_status.full_text
            except AttributeError:  # Not a Retweet
                text = tweet.full_text

            # Add the 11 variables to the empty list - ith_tweet:
            ith_tweet = [tweet_id, username, location, tweetcreatedts, retweetcount, text, hashtags]

            # Append to dataframe - db_tweets
            db_tweets.loc[len(db_tweets)] = ith_tweet

            # increase counter - noTweets
            noTweets += 1

        # Run ended:
        end_run = time.time()
        duration_run = round(end_run - start_run, 2)

        print('no. of tweets scraped for run {} is {}'.format(i, noTweets))
        print('time take for {} run to complete is {}'.format(i, duration_run))

        time.sleep(920)  # 15 minute sleep time

    # Once all runs have completed, save them to a single csv file:
    # Obtain timestamp in a readable format:
    from datetime import datetime
    to_csv_timestamp = datetime.today().strftime('%Y%m%d_%H%M%S')

    # Define working path and filename
    path = os.getcwd()
    filename = path + '/data/' + to_csv_timestamp + '_covid_19_tweets.csv'

    # Store dataframe in csv with creation date timestamp
    db_tweets.to_csv(filename, index=False)

    print('Scraping has completed!')


# Initialise these variables:
search_words = "#corona OR #covid OR #covid19 OR #COVIDー19 OR #covid-19 OR #CoronaVirus OR" \
               "#StayHome OR #StayAtHome OR #StayHomeStaySafe"
date_since = "2020-02-01"  # yyyy-mm-dd
numTweets = 2500
numRuns = 6
# Call the function scraptweets
scrap_tweets(search_words, date_since, numTweets, numRuns)
