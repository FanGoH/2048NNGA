#import numpy as np

pot2 = [2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8182, 16364]

class Block:
    def __init__(self):
        self.posicion = [0, 0]
        self.numero = 0

#class NeuralNetwork():

#    def __init__(self):
#        np.random.seed(1)

#        self.synaptic_weights = 2 * random.random((3, 1) - 1 )

class tablero:
    bloques = []
    casillas = []
    def __init__(self):
        self.casillas = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
        self.casillasocupadas = self.casillas

    def imprimir(self):
        print(self.casillas[0])
        print(self.casillas[1])
        print(self.casillas[2])
        print(self.casillas[3])

    def movement(self, direccion):
        if direccion[0] == -1:
            for bloque in self.bloques:
                while bloque.posicion[0] - 1 >= 0:
                    bloque.posicion[0] = bloque.posicion[0] - 1
        
        if direccion[0] == 1:
            for bloque in self.bloques:
                while bloque.posicion[0] + 1 < 4:
                    bloque.posicion[0] = bloque.posicion[0] + 1
        
        if direccion[1] == -1:
            for bloque in self.bloques:
                while bloque.posicion[1] - 1 >= 0:
                    bloque.posicion[1] = bloque.posicion[0] - 1
        
        if direccion[0] == -1:
            for bloque in self.bloques:
                while bloque.posicion[1] + 1 > 4:
                    bloque.posicion[1] = bloque.posicion[0] - 1

board = tablero()

board.imprimir()