import math
import csv
from numpy import random


class NeuralNetwork():
    
    def __init__(self, amount_layers, amount_neurons, activation_fun, loss_fun, optimizer, layers=None):
        random.seed(4)

        self.amount_layers = amount_layers
        self.amount_neurons = amount_neurons
        self.activation_fun = activation_fun
        self.loss_fun = loss_fun
        self.optimizer = optimizer
        self.layers = layers if layers is not None else []

    def read_data(self, input_data_path, neuron, position):
        with open(input_data_path) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            first_line = 0
            amount_neurons = 0
            for row in csv_reader:
                amount_neurons+=5
                if first_line != 0:
                    for i in range(1, len(row)):
                        neuron.read_data(position, row[i])
    
    def init_layers(self):
        for i in range (1, self.amount_layers+1):
            self.layers.append(Layer(self.amount_neurons, self.activation_fun))

   



        
                 
    

class Layer():
    def __init__(self, amount_neurons, activation_fun, neurons=None):
        random.seed(4)

        self.amount_neurons = amount_neurons
        self.activation_fun = activation_fun
        self.neurons = neurons if neurons is not None else []
    
    def init_neurons(self):
        for i in range (1, self.amount_neurons+1):
            self.neurons.append(Neuron(self.activation_fun))


class Neuron():
    def __init__(self, input_data=None, weight=None, activation_fun='', bias=None):
        self.input_data = input_data if input_data is not None else []
        self.weight = weight if weight is not None else []
        self.activation_fun = activation_fun
        self.bias = bias if bias is not None else []

    def read_data(self, index, data):
       self.input_data.insert(index, data)

    def put_data(self, data):
       self.input_data = data
       
    def init_weight(self):
        self.weight = random.random_sample((self.input_data.size))

    def init_bias(self):
        self.bias = random.random_sample((len(self.weight)))

    def fire_neuron(self):
        for i in range(0,len(self.input_data)):
            for j in range(0, len(self.input_data[i])):
                value = self.input_data[i][j] * self.weight[j] + self.bias[j]
        
        return self.activate_fun(value, activation_fun)
    
    def activate_fun(self, x_value, activation_fun):
        if activation_fun == "sigmoid":
            y_value = 1 / (1 + math.exp(-x_value))
        elif activation_fun == "tanh":
            y_value = (1 - math.exp(-2 * x_value)) / (1 + math.exp( -2 * x_value))
        elif activation_fun == "ReLu":
            if x_value < 0:
                y_value = 0
            else:
                y_value = x_value
        return y_value