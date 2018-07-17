# File: 1_simple_NN.py
# Description: Function for modifying lists with remove and count methods
# Environment: PyCharm and Anaconda environment
#
# MIT License
# Copyright (c) 2018 Valentyn N Sichkar
# github.com/sichkar-valentyn
#
# Reference to:
# [1] Valentyn N Sichkar. Neural Networks for computer vision in autonomous vehicles and robotics // GitHub platform [Electronic resource]. URL: https://github.com/sichkar-valentyn/Neural_Networks_for_Computer_Vision (date of access: XX.XX.XXXX)




# Creating a simple NN by using mathematical 'numpy' library
# We will use several methods from the library to operate with matrices

# Importing 'numpy' library
import numpy as np


# Creating a class for Neural Network
class NN():
    def __init__(self):
        # Using 'seed' for the random generator
        # It'll return the same random numbers each time the program runs
        np.random.seed(1)

        # Modeling simple Neural Network with just one neuron
        # Neuron has three inputs and one output
        # Initializing weights to 3 by 1 matrix
        # The values of the weights are in range from -1 to 1
        self.weights_of_synapses = 2 * np.random.random((3, 1)) - 1  # 3x1 matrix of weights, 3 inputs and 1 output

    # Creating function for normalizing weights and other results by Sigmoid curve
    def normalizing_results(self, x):
        return 1 / (1 + np.exp(-x))

    # Creating function for calculating a derivative of Sigmoid function (gradient of Sigmoid curve)
    # Which is going to be used for back propagation - correction of the weights
    # This derivative shows how good is the current weight
    def derivative_of_sigmoid(self, x):
        return x * (1 - x)

    # Creating function for running NN
    def run_nn(self, set_of_inputs):
        # Giving NN the set of input matrices
        # With 'numpy' function 'dot' we multiply set of input matrices to weights
        # Result is returned in normalized form
        return self.normalizing_results(np.dot(set_of_inputs, self.weights_of_synapses))

    # Creating function for training the NN
    def training_process(self, set_of_inputs_for_training, set_of_outputs_for_training, iterations):
        # Training NN desired number of times
        for i in range(iterations):
            # Feeding our NN with training set and calculating output
            nn_output = self.run_nn(set_of_inputs_for_training)

            # Calculating an error which is the difference between desired output and obtained output
            nn_error = set_of_outputs_for_training - nn_output

            # Calculating correction values for weights
            # We multiply the error to the input set and by Gradient of Sigmoid
            # In this way, the weights that do not fit too much will be corrected more
            # If some inputs are equal to 0, that will not influence to the value of weights
            # We use here function 'T' that transpose matrix and allows to multiply matrices
            corrections = np.dot(set_of_inputs_for_training.T, nn_error * self.derivative_of_sigmoid(nn_output))

            # Implementing corrections of weights
            self.weights_of_synapses += corrections


# Creating NN by initializing instance of the class
single_neuron_neural_network = NN()

# Showing the weights of synapses initialized from the very beginning randomly
print(single_neuron_neural_network.weights_of_synapses)
print()
# [[-0.16595599]
#  [ 0.44064899]
#  [-0.99977125]]

# Creating a set of inputs and outputs for the training process
# We use here function 'array' of the 'numpy' library
input_set_for_training = np.array([[1, 1, 1], [1, 0, 1], [0, 0, 1], [0, 1, 1]])
output_set_for_training = np.array([[1, 1, 0, 0]]).T

# Starting the training process with data above and number of repetitions of 5000
single_neuron_neural_network.training_process(input_set_for_training, output_set_for_training, 5000)

# Showing the weights of synapses after training process
print(single_neuron_neural_network.weights_of_synapses)
print()
# [[ 8.95950703]
#  [-0.20975775]
#  [-4.27128529]]

# After the training process was finished we can run our NN with data for testing and obtain the result
# The data for testing is [1, 0, 0]
# The expected output is 1
print(single_neuron_neural_network.run_nn(np.array([1, 0, 0])))

# Congratulations! The output is equal to 0.99987 which is very close to 1
# [0.99987151]