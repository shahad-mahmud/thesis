from keras.layers import Embedding, Flatten, Dense
from keras.datasets import imdb
from keras.models import Sequential
from keras import preprocessing

# create the embedding layer
embedding_layer = Embedding(1000, 64)

# loading imdb data and preprocessing
max_features = 10000
max_len = 20
(x_train, y_train), (x_test, y_test) = imdb.load_data(num_words=max_features)  # loads data
x_train = preprocessing.sequence.pad_sequences(x_train, maxlen=max_len)
x_test = preprocessing.sequence.pad_sequences(x_test, maxlen=max_len)  # 2D tensor of shape (samples, max_len)

model = Sequential()
model.add(Embedding(10000, 8, input_length=max_len))
model.add(Flatten())  # shape(samples, max_len * 8)

model.add(Dense(1, activation='sigmoid'))  # add classifier on the top
model.compile(optimizer='rmsprop', loss='binary_crossentropy', metrics=['acc'])
model.summary()

history = model.fit(x_train, y_train, epochs=10, batch_size=32, validation_split=0.2)
