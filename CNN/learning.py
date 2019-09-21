import keras as kr
import numpy as np
import matplotlib.pyplot as plt

from keras.datasets import fashion_mnist as fm
from keras.utils import to_categorical
from sklearn.model_selection import train_test_split

(train_x, train_y), (test_x, test_y) = fm.load_data()

print('Training data shape: ', train_x.shape, train_y.shape)
print('Testing data shape: ', test_x.shape, test_y.shape)

# find the unique numbers from the training labels
classes = np.unique(train_y)
nClasses = len(classes)
print('Total number of outputs : ', nClasses)
print('Output classes : ', classes)

plt.figure(figsize=[5, 5])

# # Display the first image in training data
# plt.subplot(121)
# plt.imshow(train_x[5, :, :], cmap='gray')
# # plt.show()
# plt.title("Ground Truth : {}".format(train_y[0]))
#
# # Display the first image in testing data
# plt.subplot(122)
# plt.imshow(test_x[0, :, :], cmap='gray')
# plt.show()
# plt.title("Ground Truth : {}".format(test_y[0]))

train_x = train_x.reshape(-1, 28, 28, 1)
test_x = test_x.reshape(-1, 28, 28, 1)
print('Training data shape: ', train_x.shape, train_y.shape)

train_x = train_x.astype('float32')
test_x = test_x.astype('float32')
train_x = train_x / 255
test_x = test_x / 255

# Change the labels from categorical to one-hot encoding
train_y_one_hot = to_categorical(train_y)
test_y_one_hot = to_categorical(test_y)

# Display the change for category label using one-hot encoding
print('Original label:', train_y[2])
print('After conversion to one-hot:', train_y_one_hot[2])

train_x, valid_X, train_label, valid_label = train_test_split(train_x, train_y_one_hot, test_size=0.2, random_state=13)
print(train_x.shape, valid_X.shape, train_label.shape, valid_label.shape)
