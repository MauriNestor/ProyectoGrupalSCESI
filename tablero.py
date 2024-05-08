import random
class tablero:
    def crearTabla(filas, columnas,valor):
        
     tablero = []
     for i in range (filas):
         tablero.append([])
         for j in range (columnas):
             tablero[i].append(valor)
             return tablero

    def mostrarTablero(tablero):
        for fila in tablero:
            for elem in fila:
             print(elem, end=" ")
        print()
        
    def colocarMinas(tablero, minas,fila,columna):
        minasOcultas = []
        numero = 0
        while numero < minas:
             y = random.randint(0, fila-1)
             x = random.randint(0, columna-1)
             if tablero[y][x] != 9:
                 tablero[y][x] = 9
                 numero += 1
                 minasOcultas.append((y,x))
        return tablero, minasOcultas


