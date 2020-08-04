# This program reads the CSV file generated from hydrator and create
# a new CSV file with only creation time and the tweet text. It also drops
# any null entities and duplicate tweets.

import pandas as pd

SOURCE_FILE_PREFIX = 'datasets/tweets_extracted/tweets_'
FILE_POSTFIX = '.csv'
SAVE_FILE_PATH = 'datasets/tweets_extracted/shorted/tweets_'

files = [i for i in range(31, 32)]

for file in files:
    print('Processing file #{}'.format(str(file)))
    read_file = pd.read_csv('datasets/tweets_extracted/tweets_{}.csv'.format(str(file)), usecols=[1, 17])
    read_file.dropna(inplace=True)
    read_file.drop_duplicates(inplace=True, subset=['text'])
    read_file.to_csv('datasets/tweets_extracted/shorted/tweets_{}.csv'.format(str(file)), index=None)
    # print(read_file.head())
    print('Processed file #{}\n'.format(str(file)))

print('**************************************')
print('JOB DONE! CHILL!!!')
