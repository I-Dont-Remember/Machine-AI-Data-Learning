#! /usr/bin/env python

"""perceptron.py: perceptron to learn boolean functions.

        Bias is considered a third weight rather than a threshold and always receives +1 as input.  This makes the threshold 0.

        T: expected Output
        O: Output

        Input file should be specifed as x1,x2,T for each possible combination
        e.g.   0,0,0
               0,1,1
               1,0,1
               1,1,1

"""
from random import randint
import collections
import sys

# Learning rate, constant between 0 and 1: eventually try with many alphas
alpha = 0.2
Output = collections.namedtuple('Output', ['T', 'O'])

# Initialize set of weights, make final (bias) negative
def initialize_weights(weights):
    for i in range(3):
        weights.append(get_random_weight())
    length = len(weights)
    weights[length-1] = weights[length-1] * -1

# Get random weight between 0.0 and 0.9
def get_random_weight():
    return randint(0,9) / float(10.0)

# Change for a given wi
def delta_wi(xi, T, O):
    return alpha * xi * (T - O)

# Update weights
def update_weights(weights,x1,x2,output):
    delta_w1 = delta_wi(x1,output.T, output.O)
    delta_w2 = delta_wi(x2,output.T, output.O)
    delta_bias = delta_wi(1,output.T,output.O)
    weights[0] += delta_w1
    weights[1] += delta_w2
    weights[2] += delta_bias
    return delta_w1, delta_w2


# Figure out how current input is handled, return T and O
def analyze_input(x1, x2, weights, T):
    weighted_sum = weights[0]*x1 + weights[1]*x2 + weights[2]*1
    O = 1 if (weighted_sum >= 0) else 0
    return Output(T,O)



############ MAIN ##############
outputs = []
weights = []
initialize_weights(weights)

if len(sys.argv) != 2:
    print "Usage: perceptron.py input.txt"
    sys.exit(0)

# With open recommended in python docs http://docs.python.org/tutorial/inputoutput.html
training_set = []
with open(sys.argv[1], "r") as input_file:
    for line in input_file:
        # Makes a sub-list of the ints given in each line
        training_set.append([int(k) for k in line.strip().split(',')])

# Skip line if doesn't have all necessary compononents
# TODO: This block seems too big, should probably be a function or two
run_count = 1
two_sets = 0
quit = False
while two_sets <= 1 and not quit:
    num_correct = 0
    print("Run#: " + str(run_count))
    for test in training_set:
        try:
            x1,x2,T = test[0],test[1],test[2]
        except IndexError:
            print "A line doesn't have all the necessary entries."
            print "This one-> " + test
        else:
            curr_output = analyze_input(x1,x2,weights,T)
            outputs.append(curr_output)
            print("Input:({0},{1}) T:{2.T} O:{2.O} w1: {3[0]} w2: {3[1]} bias: {3[2]}".format(x1,x2,curr_output,weights))
            dw1,dw2 = update_weights(weights,x1,x2,curr_output)
            if curr_output.T == curr_output.O:
                num_correct += 1
    print("correct: " + str(num_correct) + "/4\n")
    if num_correct == 4:
        two_sets +=1
    run_count += 1
    if (run_count > 30):
        print("Probably reached an infinite loop, killing training.")
        quit = True
