#Se importan objetos necesarios
from src.jugador import Jugador
from src.tablero import Tablero
#Librerias necesarias. Colorama para dar color al texto en consola. 
import random
import os
from colorama import Fore, Style 

class Juego:
    #Recibimos el numero de jugadores de main.py
    def __init__(self, num_jugadores):
        #Creamos los jugadores, dandole a cada uno un color gracias a la propiedad Fore poniendolos en un arreglo.
        colores = [Fore.RED, Fore.BLUE, Fore.GREEN, Fore.YELLOW] 
        self.jugadores = [Jugador(f"J{i + 1}", colores[i]) for i in range(num_jugadores)]
        self.tablero = Tablero(self.jugadores)
        #Creamos un turno 0, para que se inicie desde el jugador 1
        self.turno_actual = 0
    #Funcion que lanza el dado, y da un numero aleatorio entre 1 y 6
    def lanzar_dado(self):
        return random.randint(1, 6)

    #Aqui se muestra los textos en consola por los métodos que se encuentran en tablero.py, limpiando la consola para que no se vean multiples estados o multiples tableros
    def mostrar_estado(self):
        os.system('cls' if os.name == 'nt' else 'clear')

        print(self.tablero.dibujar_tablero())
        print(self.tablero.obtener_estado_jugadores())
        print("----------------------------------------")
    
    def jugar_turno(self):
        #Creamos que jugador_actual tenga los turnos actualizandose de acuerdo al jugador
        jugador_actual = self.jugadores[self.turno_actual]

        self.mostrar_estado()
        #Se da a conocer de quien es el turno con color y texto, y da la instruccion de teclear para continuar
        print(f"Es el turno del {jugador_actual.color}{jugador_actual}{Style.RESET_ALL}")
        input("Presiona una tecla para girar el Dado")
        print("----------------------------------------\n")
        #Se guarda en resultado_dado el resultado del dado aleatorio
        resultado_dado = self.lanzar_dado()
        #Se actualiza la posición del jugador sumando su posicion actual con la del dado
        nueva_posicion = jugador_actual.posicion + resultado_dado

        #Da a conocer cuanto saco, y a donde se movera.
        print(f"Sacaste un: {resultado_dado} ! \nTe mueves hacia la casilla {nueva_posicion}")
        input("\nPresiona una tecla para moverte")
        os.system('cls' if os.name == 'nt' else 'clear')
        print("\n")
        #Se activa la funcion mover de jugador.py
        jugador_actual.mover(resultado_dado, self.tablero)
        #Se cambia el turno, hasta llegar al tope para luego reiniciarse cuando esto ocurra
        self.turno_actual = (self.turno_actual + 1) % len(self.jugadores)

    def iniciar_juego(self):
        #Se crea un bucle de que el juego siga hasta que alguien llegue exactamente a la posicion 100
        while all(jugador.obtener_posicion() != 100 for jugador in self.jugadores):
            self.jugar_turno()
        #Se termina el bucle y declara al ganador que haya llegado al 100 como ganador. Se realiza viendo quien tiene la mayor posicion
        ganador = max(self.jugadores, key=lambda x: x.obtener_posicion())
        #Se anuncia el ganador, y un pequeño gesto para que presuma.
        print(f"\n¡El {ganador.color}{ganador}{Style.RESET_ALL} ha ganado el juego!\n")
        input("Presiona una tecla para presumir tu victoria!")
        print(f"{ganador} : GG Izi")

