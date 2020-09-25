import pandas as pd

SOURCE_PATH = 'datasets/emotion_trigger/tweets_with_emotion/'
DES_PATH = 'datasets/emotion_trigger/tweets_with_separate_emotion/'
FILE_NUMS = [i for i in range(25, 40) if i != 29]

emotion_tweets = [[], [], [], [], [], [], []]
emotions = ['anger', 'disgust', 'fear', 'guilt', 'joy', 'sadness', 'shame']

for file_num in FILE_NUMS:
    file = pd.read_csv(SOURCE_PATH + 'tweet_with_emo_{}.csv'.format(file_num))
    # print(file.head())
    # print(len(file['emotion_score']))
    for i in range(len(file['emotion_score'])):
        emotion_tweets[file['emotion_score'][i]].append(file['tweet'][i])

# print(emotion_tweets)
total = 0
for i in range(len(emotion_tweets)):
    length = len(emotion_tweets[i])
    total += length
    print(emotions[i], '->', len(emotion_tweets[i]))

    # print(len(emotion_tweets[i]))
    # print(len([emotions[i]] * length))
    # print(len([i] * length))
    emo_dict = {'tweet': emotion_tweets[i], 'emotion': [emotions[i]] * length, 'emotion_score': [i] * length}
    pd.DataFrame.from_dict(emo_dict).to_csv(DES_PATH + emotions[i] + '.csv')
#     print(emo[0])
