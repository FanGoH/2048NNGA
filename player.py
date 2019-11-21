import juego
import numpy as np 

class NeuralNetwork():

    def __init__(self):
        self.synaptic_weights = []
        for i in range(0, 16):
            self.synaptic_weights.append(np.random.rand(0,5))

    def sigmoid(self, x):
        return (1 / (1 + np.exp(-x)))

    def sigmoid_derivative(self, x):
        return x * (1-x)

    def train(self, t):


class Individuo():

    def __init__(self):
        self.fitness = 0
        self.pesos = []
        for i in range(0, 16):
            self.pesos.append(np.random.rand(0,5))

    def __init__(self, padres):
        self.fitness = 0
        self.pesos = []
        for i in range(0, 16):
            self.pesos.append(np.random.choice(padres))

    def jugar(self):

class Generacion():

    def __init__(self):
        self.poblacion = []
        self.seleccionados = []
        self.padres = []
        for i in range(0, 16):
            self.poblacion.append(Individuo)

    def __init__(self, ancestros):
        self.poblacion = []
        self.seleccionados = []
        self.padres = [ancestros.poblacion]

    def generar(self):

    def seleccionar(self):

    def crossover(self):
        np.random.choice(seleccionados)

        

