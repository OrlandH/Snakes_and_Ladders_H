#Libreria que da color de texto en la consola
from colorama import Fore, Style

class Jugador:
    #Traemos nombre y color para crear los jugadores
    def __init__(self, nombre, color):
        self.nombre = nombre
        #Todos inician en la posición 1
        self.posicion = 1
        self.color = color
    #Traemos la cantidad del dado y los atributos de tablero.py
    def mover(self, cantidad, tablero):
        #Se actualiza la posicion actual del jugador sumando la cantidad del dado lanzado en juego.py
        self.posicion += cantidad
        #Se crea la condición en que se verifica si la posicion actual del jugador concuerda con alguna clave de los diccionarios de serpiente o escalera de tablero
        #Si coincide alguna clave, la posicion se actualiza al valor de esa clave. Haciendo que suba o baje de posicion y se le avisa antes de continuar
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
        #Si no esta en ninguno de los diccionarios, se condiciona que si es mayor a 100, salga el mensaje de que no debe pasarse de 100, y vuelva a su posición original para que no se mueva y se termine su turno.
        elif self.posicion > 100:
            print("----------------------------------------")
            print(f"Uy, que cerca estuviste {self.nombre}! Debes llegar al 100 exacto.")
            input("Presiona una tecla para terminar tu turno")
            self.posicion -= cantidad
        #Si no se cumple nada, entonces simplemente se actualiza su posicion.
        else:
            self.posicion = self.posicion
    #Se obtiene que color y nombre del jugador para la funcion de en tablero.py
    def obtener_celda(self):
        return f"{self.color}[{self.nombre}]{Style.RESET_ALL}"
    #Se obtiene en que posicion se encuentra actualmente el jugador 
    def obtener_posicion(self):
        return self.posicion

    def __str__(self):
        return f"[{self.nombre}]"

