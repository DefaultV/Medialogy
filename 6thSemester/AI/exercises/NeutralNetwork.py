import numpy as np
import math
import cv2

def sigmoid(x):
  return 1 / (1 + np.exp(-x))

def sigmoid_derivative(x):
    x = sigmoid(x)
    return x * (1 - x)

class NeuralNetwork:
    def __init__(self, x, y):
        self.input      = x
        self.weights1   = np.random.rand(self.input.shape[1],4)
        self.weights2   = np.random.rand(4,1)
        self.y          = y
        self.output     = np.zeros(self.y.shape)

    def feedforward(self):
        self.layer1 = sigmoid(np.dot(self.input, self.weights1))
        self.output = sigmoid(np.dot(self.layer1, self.weights2))

    def backprop(self):
        # application of the chain rule to find derivative of the loss function with respect to weights2 and weights1
        d_weights2 = np.dot(self.layer1.T, (2*(self.y - self.output) * sigmoid_derivative(self.output)))
        d_weights1 = np.dot(self.input.T,  (np.dot(2*(self.y - self.output) * sigmoid_derivative(self.output), self.weights2.T) * sigmoid_derivative(self.layer1)))

        # update the weights with the derivative (slope) of the loss function
        self.weights1 += d_weights1
        self.weights2 += d_weights2

xx = np.array([ [0, 0, 2] ])
yy = np.array([ [0, 0, 0] ]).T

var = NeuralNetwork(xx,yy)
for i in range(100):
    var.feedforward()
#var.backprop()
print(var.output)

img = cv2.imread("images/h/0001.png", cv2.IMREAD_GRAYSCALE)
print(img[1][0])


class node:
    def __init__(self, input, weight, output):
        self.input = input
        self.weight = weight
        self.output = output

ilayer = []
hlayer = []
h0layer = []
h1layer = []
olayer = []

for i in range(9):
    ilayer.append(1)

variable = node(10, 5, 2)
print("hello! %d" % variable.input);
