import pandas as pd
import tweepy as tp

pd.set_option('display.max_colwidth', None)

# Twitter credentials for the app
CONSUMER_KEY = 'GWjJzHWaHOmNycuNtlyKI9F0U'
CONSUMER_SECRET = 'SNPAyWBfjOXDAZXELy3m8CWXjzDl1NP22SIPZEbudz9A2LOrMO'
ACCESS_KEY = '368305011-U0G3Cs9hdu5GymkknoroHrVI5Tbywh6aSzGCqDhT'
ACCESS_SECRET = 'iELOscP633TfOh2DyWhlfQu4FrZoaZuMVWynpUGgSjrmg'

# pass twitter credentials to tweepy
auth = tp.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tp.API(auth)

CSV_PATH = 'datasets/corona_tweets_107.csv'

id_file = pd.read_csv(CSV_PATH, nrows=2, header=None)
id_file = id_file[0]
print(id_file)

count = 0
tweets_df = pd.DataFrame(columns=['tweet_id', 'user_name', 'tweet_location', 'tweet_time',
                                  'tweet_text'])

for tweet_id in id_file:
    tweet = api.get_status(tweet_id)

    print(tweet)

    tweet_id = tweet.id
    user_name = tweet.user.screen_name
    tweet_location = tweet.user.location
    tweet_time = tweet.created_at
    try:  # if it is a retweet
        tweet_text = tweet.retweeted_status.text
    except AttributeError:  # not a retweet
        tweet_text = tweet.text

    print('id->', tweet_id, 'status->', tweet_text)
    print(tweet_text)
