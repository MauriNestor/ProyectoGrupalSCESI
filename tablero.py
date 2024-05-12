import random

class Tablero:
    def __init__(self, filas, columnas, valor=0):
        self.tablero = self.crear_tablero(filas, columnas, valor)
        self.filas = filas
        self.columnas = columnas
        self.minas_ocultas = []

    def crear_tablero(self, filas, columnas, valor):
        tablero = []
        for i in range(filas):
            tablero.append([])
            for j in range(columnas):
                tablero[i].append(valor)
        return tablero

    def mostrar_tablero(self):
        for fila in self.tablero:
            for elem in fila:
                print(elem, end=" ")
            print()

    def colocar_minas(self, minas):
        numero = 0
        while numero < minas:
            y = random.randint(0, self.filas - 1)
            x = random.randint(0, self.columnas - 1)
            if self.tablero[y][x] != 9:
                self.tablero[y][x] = 9
                numero += 1
                self.minas_ocultas.append((y, x))
        self.actualizar_numeros()

    def actualizar_numeros(self):
        for fila in range(self.filas):
            for columna in range(self.columnas):
                if self.tablero[fila][columna] == 9:
                    continue
                contador = 0
                for i in range(max(0, fila - 1), min(self.filas, fila + 2)):
                    for j in range(max(0, columna - 1), min(self.columnas, columna + 2)):
                        if self.tablero[i][j] == 9:
                            contador += 1
                self.tablero[fila][columna] = contador

    def revelar_celda(self, fila, columna):
        if self.tablero[fila][columna] == 9:
            return False
        elif self.tablero[fila][columna] == 0:
            self.revelar_celda_vacia(fila, columna)
        else:
            self.tablero[fila][columna] = ' '
        return True

    def revelar_celda_vacia(self, fila, columna):
        if fila < 0 or columna < 0 or fila >= self.filas or columna >= self.columnas:
            return
        if self.tablero[fila][columna] != 0:
            return
        if self.tablero[fila][columna] == ' ':
            return
        self.tablero[fila][columna] = ' '
        for i in range(-1, 2):
            for j in range(-1, 2):
                self.revelar_celda_vacia(fila + i, columna + j)

    def juego_terminado(self):
        for fila in range(self.filas):
            for columna in range(self.columnas):
                if self.tablero[fila][columna] != ' ' and self.tablero[fila][columna] != 9:
                    return False
        return True
