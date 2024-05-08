class tablero:
    def crearTabla(self, filas, columnas):
        self.filas = filas
        self.columnas = columnas
        self.tablero = [[' ' for _ in range(columnas)] for _ in range(filas)]

    def mostrar_tablero(self):
        for fila in self.tablero:
            print(" ".join(map(str, fila)))


