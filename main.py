from src.juego import Juego
from src.jugador import Jugador
from colorama import Fore

def main():
    while True:
        num_jugadores = int(input("Ingrese el número de jugadores (1-4): "))

        if 1 <= num_jugadores <= 4:
            colores = [Fore.RED, Fore.BLUE, Fore.GREEN, Fore.YELLOW]
            jugadores = [Jugador(f"J{i + 1}", colores[i]) for i in range(num_jugadores)]

            juego = Juego(num_jugadores)
            juego.iniciar_juego()

           
            opcion = input("¿Desea jugar otra vez? (s/n): ").lower()
            if opcion != 's':
                break 
        else:
            print("Número de jugadores no válido. Debe ser entre 1 y 4.")

if __name__ == "__main__":
    main()