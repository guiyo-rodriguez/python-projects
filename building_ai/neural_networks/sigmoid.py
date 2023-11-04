import math
import numpy as np

x = np.array([4, 3, 0])
c1 = np.array([-.5, .1, .08])
c2 = np.array([-.2, .2, .31])
c3 = np.array([.5, -.1, 2.53])

def sigmoid(z):
    # add your implementation of the sigmoid function here
    return 1 / (1 + np.exp(-z))    

def output(x, c):
    # add your implementation of the output calculation here
    print(np.dot(x, c))
    return sigmoid(np.dot(x, c))

#output(x, c1)
#output(x, c2)
#output(x, c3)


print(output(x, c1)) # calculate the output of the sigmoid for x with all three coefficients
print(output(x, c2)) # calculate the output of the sigmoid for x with all three coefficients
print(output(x, c3))
