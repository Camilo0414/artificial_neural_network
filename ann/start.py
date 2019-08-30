from neural_network import *

def main():

    ANN_object = NeuralNetwork(3,4,"tanh","binary_crossentropy","SGD_Momentum")
    print('My neural network has 3 layers and 4 neurons per each layer');
    #ANN_object.read_data()
    #layers = ANN_object.layers
    #for i in range (0, len(layers)):
    #    layers[i].init_neurons()
    #    neurons = layers[i].neurons
    #    for j in range(0, len(neurons)):
    #        neurons[j]

if __name__ == '__main__':
    main()