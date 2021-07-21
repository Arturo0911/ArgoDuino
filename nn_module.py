
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from tesorflow.keras import (
    layers,
    models,
    optimizers
)
import matplotlib.pyplot as plt



class NeuralNet:
    
    def __init__(self, num_epochs, learning_rate = 0.001):

        self.num_epochs = num_epochs
        self.learning = learning_rate

    def model_creation(self, size_layers: int, input_data: int):

        model = models.Sequential()
        model.add(layers.Dense(size_layers, activation = "relu", input_shape = (input_data)))
        model.add(layers.Dense(size_layers, activation = "relu"))
        model.add(layers.Dense(1))

        model.compile(optimizers = optimizers.RMSprop(learning_rate = self.learning),
                loss = "mse", metrics = ["mae"])

        return model



nn = NeuralNet(num_epochs=80)
