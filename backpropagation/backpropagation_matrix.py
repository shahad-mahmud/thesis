import numpy as np
import math


def activation(net_input):
    return 1 / (1 + math.e ** ((-1) * net_input))


def delta_activation(net_input):
    # print(net_input)
    return net_input * (1 - net_input)


def derivatives(output, target):
    # print(output)
    return output - target


class Ann(object):

    def __init__(self, layers, learning_rate):  # here layers holds the number of neurons in each layer
        self.num_of_layers = len(layers)  # the length of the layer list denotes the number of layers
        self.layers = layers
        self.learning_rate = learning_rate
        self.bias = [np.random.randn(l, 1) for l in layers[1:]]  # add a bias for the neurons except the input layer
        self.weights = [np.random.randn(a, b) for a, b in zip(layers[:-1], layers[1:])]  # add weights to the edges
        print('bias', self.bias)
        print('weights', self.weights)

        # c = np.dot(self.bias, self.weights)
        # print(c)

    def feed_forward(self, inputs_for_next_layer, target):
        tag = 'FEED_FORWARD '
        # abcdef = inputs_for_next_layer
        # print(tag, 'inputs', abcdef, 'target', target)
        for ith_layer in range(1, self.num_of_layers):  # the current layer
            no_of_neurons = self.layers[ith_layer]  # number of neurons in the current layer
            a = []  # for hold the outputs temporally
            # print(tag, 'no of neurons', no_of_neurons)
            for neuron in range(0, no_of_neurons):
                w = []
                # print(tag, "layer", ith_layer, 'neuron', neuron, len(self.weights[ith_layer-1]))
                for i in range(0, len(self.weights[ith_layer - 1])):
                    # print(tag, "layer", ith_layer, 'neuron', neuron, 'weight', self.weights[ith_layer-1][i][neuron])
                    w.append(self.weights[ith_layer - 1][i][neuron])  # get the weights for each neuron
                w.append(self.bias[ith_layer - 1][neuron][0])  # add the bias as weight also
                # print(tag, 'layer', ith_layer, inputs_for_next_layer, w)
                net_input = np.dot(inputs_for_next_layer[ith_layer - 1], w)  # get the net input for a neuron
                a.append(activation(net_input))  # smash it and get the output of the neuron
                # print('dot', net_input)
            a.append(1)  # add 1 as input for bias
            inputs_for_next_layer.append(a)

        print('prediction', inputs_for_next_layer[-1][0], 'target', target)
        self.back_pass(inputs_for_next_layer, target)
        # print('end loop', inputs_for_next_layer)

    def back_pass(self, activations, target):
        tag = 'BACK_PASS'
        # print(tag, activations)
        activations = np.asarray(activations)  # make it numPy array
        # print(tag, activations)
        del_w = [np.zeros(w.shape) for w in self.weights]

        del activations[-1][-1]  # delete the added 1 in the feed forward
        # print(tag, activations[-1])
        delta = derivatives(activations[-1][0], target) * delta_activation(
            activations[-1][0])  # find the delta for the output layer
        # print(tag, delta)
        del_w[-1] = np.dot(delta, activations[-2])  # the weight impact on the output

        for i in range(2, self.num_of_layers):  # find the delta form the last layer to the first layer
            del activations[-i][-1]
            ac = np.asarray(activations[-i])
            dp = delta_activation(ac)
            # print(dp)
            delta = np.dot(self.weights[-i + 1].transpose(), delta) * dp
            activations_temp = np.asarray(activations[-i - 1])
            del_w = np.dot(delta, activations_temp.transpose())

        self.weights = self.weights - self.learning_rate * del_w
        if abs(activations[-1][0] - target) >= 0.01:
            original_data = [activations[0]]
            self.feed_forward(original_data, target)

    def train(self, data):
        print('Training data', data)
        length = len(data)
        for a in data:
            print('\n\n******************************train*********************************\n\n')
            inp = a[0]
            inp.append(1)  # add 1 as input for the bias
            inps = [inp]
            self.feed_forward(inps, a[1][0])


training_data = [
    [[10, 6], [0.6]],  # first two are inputs and third is the target
    [[10, 1], [0.1]],
    [[10, 8], [0.8]],
    [[10, 2.5], [0.25]]
]
xin = Ann([2, 3, 1], 0.5)
xin.train(training_data)
