import numpy as np
import random


def activation(z):
    return 1.0 / (1.0 + np.exp(-z))


def delta_activation(z):
    return activation(z) * (1 - activation(z))


def derivatives(output_actives, target):
    return output_actives - target


class Ann(object):

    def __init__(self, layers):  # here layers holds the number of neurons in each layer
        self.num_of_layers = len(layers)  # the length of the layer list denotes the number of layers
        self.layers = layers
        self.bias = [np.random.randn(l, 1) for l in layers[1:]]  # add a bias for the neurons except the input layer
        self.weights = [np.random.randn(a, b) for a, b in zip(layers[:-1], layers[1:])]  # add weights to the edges
        print('bias', self.bias)
        print('weights', self.weights)

    def feed_forward(self, a):
        for b, w in zip(self.bias, self.weights):
            a = activation(np.dot(w, a) + b)
        return a

    def train(self, training_data, epochs, batch_size, learning_rate):
        # training data is a list of tuples (x,y) where x is input/ list of inputs and y is output/ list of outputs
        # epochs is the maximum number of tries to train the network
        # batch_size is the size of mini_batches while training
        n = len(training_data)
        for j in range(epochs):
            # random.shuffle(training_data)
            mini_batches = [training_data[k:k + batch_size] for k in range(0, n, batch_size)]
            for mini_batch in mini_batches:
                self.update_mini_batch(mini_batch, learning_rate)
            print("Epoch {0} completed.".format(j))

    def update_mini_batch(self, mini_batch, learning_rate):
        del_b = [np.zeros(b.shape) for b in self.bias]
        del_w = [np.zeros(w.shape) for w in self.weights]

        for x, y in mini_batch:
            delta_b, delta_w = self.back_propagation(x, y)
            del_b = [nb + dnb for nb, dnb in zip(del_b, delta_b)]
            del_w = [nw + dnw for nw, dnw in zip(del_w, delta_w)]

            self.weights = [w - learning_rate / len(mini_batch) * nw for w, nw in zip(self.weights, del_w)]
            self.bias = [b - learning_rate / len(mini_batch) * nb for b, nb in zip(self.bias, del_b)]

    def back_propagation(self, x, y):
        del_b = [np.zeros(b.shape) for b in self.bias]
        del_w = [np.zeros(w.shape) for w in self.weights]

        # feed forward
        active = x
        actives = [x]
        zs = []

        for b, w in zip(self.bias, self.weights):
            print(w)
            print(active)
            z = np.dot(w, active) + b
            zs.append(z)
            active = activation(z)
            actives.append(active)

        # back pass
        delta = derivatives(actives[-1], y) * delta_activation(zs[-1])
        del_b[-1] = delta
        del_w[-1] = np.dot(delta, actives[-2].transpose())

        for l in range(2, self.num_of_layers):
            z = zs[-l]
            sp = delta_activation(z)
            delta = np.dot(self.weights[-l + 1].transpose(), delta) * sp
            del_b[-1] = delta
            del_w[-1] = np.dot(delta, actives[-l - 1].transpose())
        return del_b, del_w


# training = [
#     [[10, 6], [0.6]],  # first two are inputs and third is the target
#     [[10, 1], [0.1]],
#     [[10, 8], [0.8]],
#     [[10, 2.5], [0.25]]
# ]

i = [
    [10, 6],
    [10, 3],
    [20, 4],
    [10, 4]
]
o = [
    [0.6],
    [0.3],
    [0.2],
    [0.4]
]
t = (i, o)
xin = Ann([2, 3, 1])
# xin.train(t, 30, 1, .05)
print(t)
