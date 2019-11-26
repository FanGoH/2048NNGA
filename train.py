import neat
import pickle
import os
import random as rd
import numpy as np
import copy
from math import log

class Block:
    def __init__(self, pos):
        self.posicion = [pos[0], pos[1]]
        self.numero = rd.choice([2, 4])
    
    def __repr__(self):
        return str(self.numero)

class tablero:
    bloques = []
    casillas = []
    score = 0
    def __init__(self):
        self.casillas = [[0,0,0,0],[0,0,0,0], [0,0,0,0], [0,0,0,0]] 
        self.casillasocupadas = [[0,0,0,0],[0,0,0,0], [0,0,0,0], [0,0,0,0]] 
        self.casillasnumero = [[0,0,0,0],[0,0,0,0], [0,0,0,0], [0,0,0,0]]
        self.bloques.append(Block([rd.choice([0, 1, 2, 3]), rd.choice([0, 1, 2, 3])]))
        self.terminado = False
        self.actuales = 1
        self.moved = False

    def actualizar(self):
        self.casillasocupadas = [[0,0,0,0],[0,0,0,0], [0,0,0,0], [0,0,0,0]] 
        self.casillas = [[0,0,0,0],[0,0,0,0], [0,0,0,0], [0,0,0,0]] 
        for bloque in self.bloques:
            self.casillas[bloque.posicion[1]][bloque.posicion[0]] = bloque
            self.casillasnumero[bloque.posicion[1]][bloque.posicion[0]] = bloque.numero
            self.casillasocupadas[bloque.posicion[1]][bloque.posicion[0]] = 1

    def imprimir(self):
        print(self.casillas[0])
        print(self.casillas[1])
        print(self.casillas[2])
        print(self.casillas[3])
        print("Score : " + str(self.score))

    def movement(self, direccion):
        if direccion[0] == 1:
            stack = sorted(self.bloques, key=lambda x: x.posicion[0], reverse=True)
        elif direccion[0] == -1:
            stack = sorted(self.bloques, key=lambda x: x.posicion[0], reverse=False)
        elif direccion[1] == -1:
            stack = sorted(self.bloques, key=lambda x: x.posicion[1], reverse=True)
        elif direccion[1] == 1:
            stack = sorted(self.bloques, key=lambda x: x.posicion[1], reverse=False)

        n = len(stack)
        m = 0

        if direccion[0] == -1:
            for bloque in stack:
                m = m + 1
                cantidad = 0
                indice = bloque.posicion[0] - 1
                combinar = False
                while indice >= 0:
                    if self.casillasocupadas[bloque.posicion[1]][indice] == 1:
                        if cantidad == 0 and self.casillas[bloque.posicion[1]][indice].numero == bloque.numero:
                            combinar = True
                            self.moved = True
                            bloque2 = self.casillas[bloque.posicion[1]][indice]
                        cantidad = cantidad + 1
                    indice = indice - 1
                bloque.posicion[0] = 0 + cantidad
                if combinar:
                    self.merge(direccion, bloque.posicion[0], bloque, bloque2)
        
        if direccion[0] == 1:
            for bloque in stack:
                m = m + 1
                cantidad = 0
                indice = bloque.posicion[0] + 1
                combinar = False
                while indice < 4:
                    if self.casillasocupadas[bloque.posicion[1]][indice] == 1:
                        if cantidad == 0 and self.casillas[bloque.posicion[1]][indice].numero == bloque.numero:
                            combinar = True
                            self.moved = True
                            bloque2 = self.casillas[bloque.posicion[1]][indice]
                        cantidad = cantidad + 1
                    indice = indice + 1
                bloque.posicion[0] = 3 - cantidad
                if combinar:
                    self.merge(direccion, bloque.posicion[0], bloque, bloque2)

        if direccion[1] == -1:
            for bloque in stack:
                m = m + 1
                cantidad = 0
                indice = bloque.posicion[1] + 1
                combinar = False
                while indice < 4:
                    if self.casillasocupadas[indice][bloque.posicion[0]] == 1:
                        if cantidad == 0 and self.casillas[indice][bloque.posicion[0]].numero == bloque.numero:
                            combinar = True
                            self.moved = True
                            bloque2 = self.casillas[indice][bloque.posicion[0]]
                        cantidad = cantidad + 1
                    indice = indice + 1
                bloque.posicion[1] = 3 - cantidad
                if combinar:
                    self.merge(direccion, bloque.posicion[1], bloque, bloque2)

        if direccion[1] == 1:
            for bloque in stack:
                m = m + 1
                cantidad = 0
                indice = bloque.posicion[1] - 1
                combinar = False
                while indice >= 0:
                    if self.casillasocupadas[indice][bloque.posicion[0]] == 1:
                        if cantidad == 0 and self.casillas[indice][bloque.posicion[0]].numero == bloque.numero:
                            combinar = True
                            self.moved = True
                            bloque2 = self.casillas[indice][bloque.posicion[0]]
                        cantidad = cantidad + 1
                    indice = indice - 1
                bloque.posicion[1] = 0 + cantidad
                if combinar:
                    self.merge(direccion, bloque.posicion[1], bloque, bloque2)
        
        if (m < n):
            self.moved = True

    def merge(self, direccion, hilera, bloque, bloque2):
        self.actualizar()
        bloque2.numero = bloque2.numero + bloque.numero
        eje = [bloque.posicion[1] + direccion[1], bloque.posicion[0] - direccion[0]]
        temp = []
        while eje[0] >= 0 and eje[0] < 4 and eje[1] >= 0 and eje[1] < 4:
            if(self.casillasocupadas[eje[0]][eje[1]] == 1):
                temp.append(self.casillas[eje[0]][eje[1]])
            eje[0] = eje[0] + direccion[1]
            eje[1] = eje[1] - direccion[0]

        self.bloques.remove(bloque)
        
        for bloque in temp:

            if direccion[0] == -1:
                cantidad = 0
                indice = bloque.posicion[0] - 1
                while indice >= 0:
                    if self.casillasocupadas[bloque.posicion[1]][indice] == 1:
                        cantidad = cantidad + 1
                    indice = indice - 1
                bloque.posicion[0] = 0 + cantidad
            
            if direccion[0] == 1:
                cantidad = 0
                indice = bloque.posicion[0] + 1
                while indice < 4:
                    if self.casillasocupadas[bloque.posicion[1]][indice] == 1:
                        cantidad = cantidad + 1
                    indice = indice + 1
                bloque.posicion[0] = 3 - cantidad
            
            if direccion[1] == -1:
                cantidad = 0
                indice = bloque.posicion[1] + 1
                while indice < 4:
                    if self.casillasocupadas[indice][bloque.posicion[0]] == 1:
                        cantidad = cantidad + 1
                    indice = indice + 1
                bloque.posicion[1] = 3 - cantidad

            if direccion[1] == 1:
                cantidad = 0
                indice = bloque.posicion[1] - 1
                while indice >= 0:
                    if self.casillasocupadas[indice][bloque.posicion[0]] == 1:
                        cantidad = cantidad + 1
                    indice = indice - 1
                bloque.posicion[1] = 0 + cantidad

        self.actuales = self.actuales - 1
        self.score = self.score + bloque2.numero
        self.actualizar()

    def ciclo(self, opcion):
        #self.bloquesbefore = np.matrix.copy(self.casillasnumero)
        #for bloque in self.bloques:
        #    self.bloquesbefore.append(Block(bloque.posicion))
        
        opc = opcion
        opc = opc.capitalize()
        if opc == 'W':
            self.movement([0,1])
        elif opc == 'A':
            self.movement([-1, 0])
        elif opc == 'S':
            self.movement([0,-1])
        elif opc == 'D':
            self.movement([1, 0])
        valido = False
        self.actualizar()
        repetido = False
        '''for i in range(0,3):
            for bloque in self.: 
                if(bloque not numero):
                    repetido = False'''

        contador = 0
        for bloque in self.bloques:
            bloque1 = bloque
            contador = contador +1
            if bloque.numero == 2048:
                self.terminado == True

        if contador <= 15:
            self.terminado = True

        contador = 0
        for i in range(0, 3):
            for j in range(0, 3):
                contador = contador + self.casillasocupadas[i][j]
                
        if contador >=14:
            self.terminado = True

        if self.actuales >= 15:
            self.terminado = True

        if not repetido and not self.terminado:                    
            while not valido:
                nuevo = Block([rd.choice([0,1,2,3]), rd.choice([0,1,2,3])])
                self.actuales = self.actuales +1
                if self.casillasocupadas[nuevo.posicion[1]][nuevo.posicion[0]] == 0:
                    self.bloques.append(nuevo)
                    valido = True

        self.actualizar()
        
def humano():
    board = tablero()
    board.actualizar()

    while True:
        board.imprimir()
        opc = input("WASD: ")
        board.ciclo(opc)

def decision(board, indice):
    if(indice == 0):
        board.ciclo("W")
    elif(indice == 1):
        board.ciclo("A")
    elif(indice == 2):
        board.ciclo("S")
    elif(indice == 3):
        board.ciclo("D")

def main(genomes, config):
    nets = []
    ge = []
        
    for _, g in genomes:
        net = neat.nn.FeedForwardNetwork.create(g, config)
        nets.append(net)
        g.fitness = 0
        ge.append(g)

    for x, individuo in enumerate(ge):
        ls = 0
        nsls = 0
        print("--------- Individuo ---------- " + str(x))   
        board = tablero()
        ge[x].fitness = ge[x].fitness + 0.1
        individuo = individuo    
        contador = 10     
        while board.terminado == False and contador >= 0:
            move = nets[x].activate((board.casillasnumero[0][0],board.casillasnumero[0][1],board.casillasnumero[0][2],board.casillasnumero[0][3],board.casillasnumero[1][0],board.casillasnumero[1][1],board.casillasnumero[1][2],board.casillasnumero[1][3],board.casillasnumero[2][0],board.casillasnumero[2][1],board.casillasnumero[2][2],board.casillasnumero[2][3],board.casillasnumero[3][0],board.casillasnumero[3][1],board.casillasnumero[3][2],board.casillasnumero[3][3]))
            #move = nets[x].activate(np.flatten(board.casillas))
            decision(board, np.argmax(move))  
            board.imprimir()
            print("Actuales ocupadas : " + str(board.actuales))
            if board.terminado == True: # or not board.moved:
                ge.pop(x)
                nets.pop(x)
                break
            if(not (board.score == 0) and not (len(board.bloques) == 0)):
                ge[x].fitness = log(board.score, 2)
                ge[x].fitness = log(ge[x].fitness, 2) + log(16,2) - log(len(board.bloques), 2)
            contador = contador - 1
            if ls == board.score:
                nsls = nsls + 1
            else:
                nsls = 0

            if nsls >= 10:
                ge.pop(x)
                nets.pop(x)
                break
            ls = board.score

def run(config_path):
    config = neat.config.Config(neat.DefaultGenome, neat.DefaultReproduction, neat.DefaultSpeciesSet, neat.DefaultStagnation, config_path)

    p = neat.Population(config)

    p.add_reporter(neat.StdOutReporter(True))
    stats = neat.StatisticsReporter()
    p.add_reporter(stats)

    # fitness function, generations
    mejor_individuo = p.run(main, 10)

    with open('IAPro.pickle', 'wb') as handle:
        pickle.dump(mejor_individuo, handle)

if __name__ == "__main__":
    local_dir = os.path.dirname(__file__)
    config_path = os.path.join(local_dir, "config-feedforward.txt")
    run(config_path)