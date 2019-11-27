import random as rd
import numpy as np

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
        self.ganado = False

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
        for i in range(0, 4):
            for j in range(0, 4):
                contador = contador + self.casillasocupadas[i][j]
                
        if contador >=16:
            self.terminado = True

        if self.actuales >= 16:
            self.terminado = True

        contador = 0
        for i in range(0,4):
            for j in range(0,4):
                if self.casillasnumero[i][j] != 0:
                    contador = contador + 1
                if self.casillasnumero[i][j] == 2048:
                    self.ganado = True

        if contador == 15:
            self.terminado = True 

        if not repetido and not self.terminado:                    
            while not valido:
                nuevo = Block([rd.choice([0,1,2,3]), rd.choice([0,1,2,3])])
                self.actuales = self.actuales +1
                if self.casillasocupadas[nuevo.posicion[1]][nuevo.posicion[0]] == 0:
                    self.bloques.append(nuevo)
                    valido = True

        self.actualizar()
        
        
def main():
    board = tablero()
    board.actualizar()

    while True:
        board.imprimir()
        opc = input("WASD: ")
        board.ciclo(opc)