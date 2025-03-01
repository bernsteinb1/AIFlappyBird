import numpy as np
from typing import Union
import time

INPUT_NODES = 1
HIDDEN_LAYER_NODES = [2]  # use empty list for no hidden layers
OUTPUT_NODES = 3

class NeuralNetwork:
    def __init__(self):
        """
        Initializes neural network with parameters set to the static variables declared at the top of the file
        """
        previous_layer_nodes = INPUT_NODES
        self.weights = []
        self.biases = []
        # initialize weights and biases randomly between -1 and 1 with a uniform distribution
        for i in range(len(HIDDEN_LAYER_NODES)):
            self.weights.append(np.random.uniform(-1, 1, size=(previous_layer_nodes, HIDDEN_LAYER_NODES[i])))
            self.biases.append(np.random.uniform(-1, 1, size=HIDDEN_LAYER_NODES[i]))
            previous_layer_nodes = HIDDEN_LAYER_NODES[i]
        self.weights.append(np.random.uniform(-1, 1, size=(previous_layer_nodes, OUTPUT_NODES)))
        self.biases.append(np.random.uniform(-1, 1, size=OUTPUT_NODES))

    def run(self, data: list[float]) -> Union[float, list[float]]:
        """Runs data through the neural network and returns the value in the output node(s)

        Args:
            data (list[float]): single dimension array containing each input as its own cell

        Returns:
            Union[float, list[float]]: float or array of floats representing the output value for each cell.
        """
        # run data through each layer applying ReLU at all cells except for the final cell
        for i in range(len(self.weights)):
            data = np.matmul(data, self.weights[i]) + self.biases[i]
            if i != len(self.weights) - 1:
                data = np.maximum(data, np.zeros_like(data))
        if len(data) == 1:
            return data[0]
        data = np.exp(data)
        return data / np.sum(data)


if __name__ == '__main__':
    networks = [NeuralNetwork() for _ in range(1000)]
    start = time.time()
    for i in range(1000):
        print(networks[i].run([5]))
    print()
    print(time.time() - start)