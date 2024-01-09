from src.jugador import Jugador
from src.tablero import Tablero
import random
import os
from colorama import Fore, Style 

class Juego:
    def __init__(self, num_jugadores):
        colores = [Fore.RED, Fore.BLUE, Fore.GREEN, Fore.YELLOW] 
        self.jugadores = [Jugador(f"J{i + 1}", colores[i]) for i in range(num_jugadores)]
        self.tablero = Tablero(self.jugadores)
        self.turno_actual = 0

    def lanzar_dado(self):
        return random.randint(1, 6)

    def mostrar_estado(self):
        os.system('cls' if os.name == 'nt' else 'clear')

        print(self.tablero.dibujar_tablero())
        print(self.tablero.obtener_estado_jugadores())
        print("----------------------------------------")

    def jugar_turno(self):
        jugador_actual = self.jugadores[self.turno_actual]

        self.mostrar_estado()

        print(f"Es el turno del {jugador_actual.color}{jugador_actual}{Style.RESET_ALL}")
        input("Presiona una tecla para girar el Dado")
        print("----------------------------------------\n")

        resultado_dado = self.lanzar_dado()
        nueva_posicion = jugador_actual.posicion + resultado_dado

        print(f"Sacaste un: {resultado_dado} ! \nTe mueves hacia la casilla {nueva_posicion}")
        input("\nPresiona una tecla para moverte")
        os.system('cls' if os.name == 'nt' else 'clear')
        print("\n")
        
        jugador_actual.mover(resultado_dado, self.tablero)

        self.turno_actual = (self.turno_actual + 1) % len(self.jugadores)

    def iniciar_juego(self):
        while all(jugador.obtener_posicion() != 100 for jugador in self.jugadores):
            self.jugar_turno()

        ganador = max(self.jugadores, key=lambda x: x.obtener_posicion())
        print(f"\n¡El {ganador.color}{ganador}{Style.RESET_ALL} ha ganado el juego!\n")
        input("Presiona una tecla para presumir tu victoria!")
        print(f"{ganador} : GG Izi")

