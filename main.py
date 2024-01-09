# Importar los objetos
from src.juego import Juego
from src.jugador import Jugador

def main():
    # Bucle para repetir juego
    while True:
        #Se ingresa número de jugadores
        num_jugadores = int(input("Ingrese el número de jugadores (1-4): "))
        #Se hace la condicion para que este en el rango de 1 a 4 se inicie el juego 
        if 1 <= num_jugadores <= 4:
            #Se envia el numero de jugadores
            juego = Juego(num_jugadores)
            juego.iniciar_juego()

           #Una vez terminado el juego, se pregunta si desean jugar de nuevo
            opcion = input("¿Desea jugar otra vez? (s/n): ").lower()
            #Se rompe el bucle en caso seleccione algo diferente de 's'
            if opcion != 's':
                break 
        else:
            print("Número de jugadores no válido. Debe ser entre 1 y 4.")

if __name__ == "__main__":
    main()