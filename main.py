# Importa la clase Tablero desde el mismo archivo
from tablero import Tablero

def main():
    # Crea un objeto Tablero con 5 filas, 5 columnas y 5 minas
    mi_tablero = Tablero(5, 5, valor='*')
    
    # Coloca las minas en el tablero
    mi_tablero.colocar_minas(5)
    
    # Muestra el tablero
    print("Tablero con minas:")
    mi_tablero.mostrar_tablero()

if __name__ == "__main__":
    main()
