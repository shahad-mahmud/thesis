import math

w1 = w2 = w3 = w4 = b1 = b2 = 0.5
learning_rate = 0.67
count = 0

training_data = [
    [0, 0],
    [1, 1]
    # [2, 0],
    # [3, 1],
    # [4, 0],
    # [5, 1],
    # [6, 0],
    # [8, 0],
    # [10, 0]
]


def loss_function(targeted, output):
    e = targeted - output
    return e * e * 0.5


def activation(net_input):
    return 1 / (1 + math.e ** ((-1) * net_input))


for training_input in training_data:
    number = training_input[0]
    target = training_input[1]

    y = -564

    while abs(target - y) >= 0.01:
        # forward pass
        # for hidden neuron 1
        net_in1 = number * w1 + b1
        y1 = activation(net_in1)

        # for hidden neuron 2
        net_in2 = number * w2 + b2
        y2 = activation(net_in2)

        # for output neuron
        net_in_out = y1 * w3 + y2 * w4 + b1
        y = activation(net_in_out)
        error = loss_function(target, y)

        print("step:", count, " target:", target, " output:", y)
        count = count + 1

        # back pass
        pw4 = (y - target) * (y * (1 - y)) * y2
        w4 = w4 - learning_rate * pw4

        pw3 = (y - target) * (y * (1 - y)) * y1
        w3 = w3 - learning_rate * pw3

        pw1 = (y - target) * w1 * number
        w1 = w1 - learning_rate * pw1

        pw2 = (y - target) * w2 * number
        w2 = w2 - learning_rate * pw2


print("training completed")

input_num = int(input("Enter a number: "))

# for hidden neuron 1
net_in1 = input_num * w1 + b1
y1 = activation(net_in1)

# for hidden neuron 2
net_in2 = input_num * w2 + b2
y2 = activation(net_in2)

# for output neuron
net_in_out = y1 * w3 + y2 * w4 + b1
y_out = activation(net_in_out)
print(y_out)

