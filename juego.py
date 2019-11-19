import random as rd

pot2 = [2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8182, 16364]

class Block:
    def __init__(self, pos):
        self.posicion = [pos[0], pos[1]]
        self.numero = rd.choice([2, 4])
    
    def __repr__(self):
        return str(self.numero)

class tablero:
    bloques = []
    casillas = []
    def __init__(self):
        self.casillas = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
        self.casillasocupadas = self.casillas
        self.bloques.append(Block([rd.choice([0, 1, 2, 3]), rd.choice([0, 1, 2, 3])]))

    def actualizar(self):
        self.casillasocupadas = [[0,0,0,0],[0,0,0,0], [0,0,0,0], [0,0,0,0]] 
        self.casillas = [[0,0,0,0],[0,0,0,0], [0,0,0,0], [0,0,0,0]] 
        for bloque in self.bloques:
            self.casillas[bloque.posicion[1]][bloque.posicion[0]] = bloque
            self.casillasocupadas[bloque.posicion[1]][bloque.posicion[0]] = 1

    def imprimir(self):
        print(self.casillas[0])
        print(self.casillas[1])
        print(self.casillas[2])
        print(self.casillas[3])

    def movement(self, direccion):
        if direccion[0] == -1:
            for bloque in self.bloques:
                cantidad = 0
                indice = bloque.posicion[0] - 1
                while indice >= 0:
                    if self.casillasocupadas[bloque.posicion[1]][indice] == 1:
                        cantidad = cantidad + 1
                    indice = indice - 1
                bloque.posicion[0] = 0 + cantidad

        
        if direccion[0] == 1:
            for bloque in self.bloques:
                cantidad = 0
                indice = bloque.posicion[0] + 1
                while indice < 4:
                    if self.casillasocupadas[bloque.posicion[1]][indice] == 1:
                        cantidad = cantidad + 1
                    indice = indice + 1
                bloque.posicion[0] = 3 - cantidad

        if direccion[1] == -1:
            for bloque in self.bloques:
                cantidad = 0
                indice = bloque.posicion[1] + 1
                while indice < 4:
                    if self.casillasocupadas[indice][bloque.posicion[0]] == 1:
                        cantidad = cantidad + 1
                    indice = indice + 1
                bloque.posicion[1] = 3 - cantidad

        if direccion[1] == 1:
            for bloque in self.bloques:
                cantidad = 0
                indice = bloque.posicion[1] - 1
                while indice >= 0:
                    if self.casillasocupadas[indice][bloque.posicion[0]] == 1:
                        cantidad = cantidad + 1
                    indice = indice - 1
                bloque.posicion[1] = 0 + cantidad

    #def merge(self, direccion):
    #    for bloque in self.bloques:
    #        if(bloque.)


    def ciclo(self):
        opc = input("W = Up, A = Left, S = Down, D = Right: ")
        if opc == 'W':
            self.movement([0,1])
        elif opc == 'A':
            self.movement([-1, 0])
        elif opc == 'S':
            self.movement([0,-1])
        elif opc == 'D':
            self.movement([1, 0])
        valido = False
        while not valido:
            nuevo = Block([rd.choice([0,1,2,3]), rd.choice([0,1,2,3])])
            if self.casillasocupadas[nuevo.posicion[1]][nuevo.posicion[0]] == 0:
                self.bloques.append(nuevo)
                valido = True
        self.actualizar()
        
board = tablero()
board.actualizar()

while True:
    board.imprimir()
    board.ciclo()