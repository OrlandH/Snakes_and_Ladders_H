from colorama import Fore, Style

class Jugador:
    def __init__(self, nombre, color):
        self.nombre = nombre
        self.posicion = 1
        self.color = color

    def mover(self, cantidad, tablero):
        self.posicion += cantidad

        if self.posicion in tablero.serpientes:
            destino_serpiente = tablero.serpientes[self.posicion]
            print("----------------------------------------")
            print(f"\nDemonios!! Había una serpiente en la casilla {self.posicion}, te resbalaste a la casilla {destino_serpiente}!!")
            input("Presiona una tecla para moverte")
            self.posicion = destino_serpiente
        elif self.posicion in tablero.escaleras:
            destino_escalera = tablero.escaleras[self.posicion]
            print("----------------------------------------")
            print(f"\nWujuu!. Encontraste una escalera en la casilla {self.posicion}, puedes subir a la casilla {destino_escalera}!!")
            input("Presiona una tecla para moverte")
            self.posicion = destino_escalera
        elif self.posicion > 100:
            print("----------------------------------------")
            print(f"Uy, que cerca estuviste {self.nombre}! Debes llegar al 100 exacto.")
            input("Presiona una tecla para terminar tu turno")
            self.posicion -= cantidad
        else:
            self.posicion = self.posicion

    def obtener_celda(self):
        return f"{self.color}[{self.nombre}]{Style.RESET_ALL}"

    def obtener_posicion(self):
        return self.posicion

    def __str__(self):
        return f"[{self.nombre}]"

