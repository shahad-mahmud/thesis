import math


def activation(net_input):
    return 1 / (1 + math.e ** ((-1) * net_input))


step = 0

# weights
w1 = w2 = w3 = w4 = w5 = w6 = w7 = w8 = w9 = 0.1

# bias
b1 = 0.326
b2 = 0.45

# learning rate
n = 0.67

# train
training_data = [
    [10, 6, 0.6],  # first two are inputs and third is the target
    [10, 1, 0.1],
    [10, 8, 0.8],
    [10, 2.5, 0.25]
]

for inputs in training_data:
    x1 = inputs[0]
    x2 = inputs[1]
    target = inputs[2]

    out_o = 0.5

    while abs(target - out_o) >= 0.001:
        # the forward pass
        # the hidden neurons
        net_h1 = x1 * w1 + x2 * w2 + b1  # net input for h1 neuron
        net_h2 = x1 * w2 + x2 * w5 + b1
        net_h3 = x1 * w3 + x2 * w6 + b1

        out_h1 = activation(net_h1)  # output of the h1 neuron
        out_h2 = activation(net_h2)
        out_h3 = activation(net_h3)

        # the output neuron
        net_o = out_h1 * w7 + out_h2 * w8 + out_h3 * w9 + b2  # net input for the output neuron
        out_o = activation(net_o)

        print("step ", step, " target ", target, " prediction ", out_o)
        step = step + 1

        # here the loss function is used but the value is not needed directly

        # the back pass
        # the output neuron
        e_w7 = (out_o - target) * out_o * (1 - out_o) * out_h1  # effect of w7 in output
        e_w8 = (out_o - target) * out_o * (1 - out_o) * out_h2
        e_w9 = (out_o - target) * out_o * (1 - out_o) * out_h3

        w7 = w7 - (n * e_w7)
        w8 = w8 - (n * e_w8)
        w9 = w9 - (n * e_w9)

        # the hidden neurons
        temp = (out_o - target) * out_o * (1 - out_o)
        e_w1 = temp * w7 * out_h1 * (1 - out_h1) * x1
        e_w2 = temp * w8 * out_h2 * (1 - out_h2) * x1
        e_w3 = temp * w9 * out_h3 * (1 - out_h3) * x1
        e_w4 = temp * w7 * out_h1 * (1 - out_h1) * x2
        e_w5 = temp * w8 * out_h2 * (1 - out_h2) * x2
        e_w6 = temp * w9 * out_h3 * (1 - out_h3) * x2

        # print(w7, net_h1, x1)

        w1 = w1 - (n * e_w1)
        w2 = w2 - (n * e_w2)
        w3 = w3 - (n * e_w3)
        w4 = w4 - (n * e_w4)
        w5 = w5 - (n * e_w5)
        w6 = w6 - (n * e_w6)

print("Training completed")

print("w1 = ", w1)
print("w2 = ", w2)
print("w3 = ", w3)
print("w4 = ", w4)
print("w5 = ", w5)
print("w6 = ", w6)
print("w7 = ", w7)
print("w8 = ", w8)
print("w9 = ", w9)
