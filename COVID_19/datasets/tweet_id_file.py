# This program is written for creating files with tweet id only
# downloaded form IEEE data port. These id files will be used to
# feed hydrator as source file to hydrate tweets.

import pandas as pd

SOURCE_FILE_PREFIX = '../datasets/corona_tweets_'
FILE_POSTFIX = '.csv'
ID_FILE_PATH = '../datasets/tweet_id_files/ids_corona_tweets_'

start = int(input('Starting range (e.g. 100): '))
end = int(input('Ending range (e.g. 109): '))

files = [i for i in range(start, end + 1)]

for file in files:
    print('Starting process for file {}'.format(file))
    input_file = pd.read_csv(SOURCE_FILE_PREFIX + str(file) + FILE_POSTFIX, header=None, nrows=50000)
    input_file.dropna(inplace=True)
    ids = input_file[0]
    # print(ids)
    ids.to_csv(ID_FILE_PATH + str(file) + FILE_POSTFIX, index=False, header=None)
    print('End process for file {}'.format(file))

print('\n**************************************')
print('JOB DONE! CHILL!!!')
