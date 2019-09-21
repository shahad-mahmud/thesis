import numpy as np

time_steps = 100  # number of time steps in the input sequence
input_features = 32
output_features = 64

input_sequence = np.random.random((time_steps, input_features))  # random inputs. A time_steps * input_features matrix
state_t = np.zeros((output_features,))  # the output of the previous loop. Initially a 'all zero' vector

# weight matrices
W = np.random.random((output_features, input_features))
U = np.random.random((output_features, output_features))
b = np.random.random((output_features,))

successive_outputs = []

# print(state_t)
epoch = 0
for input_t in input_sequence:  # input_t is a vector of shape(input_sequence)
    output_t = np.tanh(np.dot(W, input_t) + np.dot(U, state_t) + b)  # obtain the current output
    successive_outputs.append(output_t)  # store the output int the list
    state_t = output_t  # update the state of the RNN for the next input
    print('\n\nEpoch: ', epoch, '\nInputs: ', input_t, '\nOutputs: ', output_t)
    epoch = epoch + 1

final_output_sequence = np.concatenate(successive_outputs, axis=0)  # final output is the 2D tensor

print('Final output sequence: ', final_output_sequence)
