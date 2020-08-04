import zipfile as zf

SOURCE_PATH = 'datasets/corona_tweets_'
FILE_EXTN = '.zip'

start = int(input('Starting range (e.g. 100): '))
end = int(input('Ending range (e.g. 109): '))

# ********************Processing zone. DO NOT ALTER**************************
files = [i for i in range(start, end + 1)]

for file in files:
    print('\nExtracting file #{}'.format(str(file)))
    file_name = SOURCE_PATH + str(file) + FILE_EXTN
    with zf.ZipFile(file_name, 'r') as ref:
        ref.extractall('datasets/')
    print('Extracted file #{}'.format(str(file)))

print('\n**************************************')
print('JOB DONE! CHILL!!!')
