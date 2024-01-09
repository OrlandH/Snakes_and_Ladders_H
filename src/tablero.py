#Libreria para insertar color en la consola
from colorama import Fore, Style

class Tablero:
    #Recibimos los jugadores y sus atributos
    def __init__(self, jugadores):
        self.jugadores = jugadores
        #Se crean diccionarios de serpientes y escaleras, donde la clave es el inicio del evento, y el valor es a donde se mueven cuando llegan a la clave.
        self.serpientes = {16:6, 46:25, 49: 11, 62:19, 64:60, 74:53, 89:68, 92:88, 95:75, 99:80}
        self.escaleras = {2:38, 7:14, 8:31, 15:26, 21:42, 28:84, 36:44, 51:67, 71:91, 78:98, 87:94}
    

    def dibujar_tablero(self):
        #Se inicia un texto tablero vacio para que cada que se reinicie el dibujo, no se sobreponga, o se vean multiples tableros.
        tablero = "\n"
        #Creamos dos arreglos, ya que el tablero va en forma de zigzag, vamos a hacer lineas que sumen y otros que resten para que se dibujen en un orden correcto.
        rangopos = [100,80,60,40,20]
        rangoneg = [81,61,41,21,1]

        #Contador que recorrera los arreglos rangopos y rangoneg
        for contador in range(0,5):
            #Auxiliar para crear las filas, debe estar vacio para que no se sobreponga cuando inicia de nuevo el bucle
            fila_tablero = ""

            #Estos son los valores que iremos restando, por ejemplo que se imprima 100,99,98,97...91. En lugar de 91,92,93,94...100 y funcione correctamente el zigzag
            for i in range(rangopos[contador], rangopos[contador]-10, -1):
                #Creamos condiciones en que si 'i' toma el valor de alguna clave de los diccionarios, se agregue S o E dependiendo el caso al valor que se agrega al auxiliar fila_tablero
                if i in self.serpientes:
                    fila_tablero += f"S{i}     |"
                elif i in self.escaleras:
                    fila_tablero += f"E{i}     |"
                #De lo contrario, se agrega al auxiliar el resultado de obtener_celda
                else:
                    fila_tablero += self.obtener_celda(i)
            #Se añade la fila al texto, junto con 2 saltos de linea
            tablero += f"{fila_tablero}\n\n"  
            #Se vuelve a vaciar el auxiliar para el siguiente bucle
            fila_tablero = ""
            #Similar al anterior bucle, pero en positivo, aqui si ira por ejemplo 81,82,83,84...90 y se imprimira debajo del bucle de arriba
            for i in range(rangoneg[contador], rangoneg[contador]+10):
                if i in self.serpientes:
                    fila_tablero += f"S{i}     |"
                elif i in self.escaleras:
                    fila_tablero += f"E{i}     |"
                else:
                    fila_tablero += self.obtener_celda(i)

            tablero += f"{fila_tablero}\n\n"
        #Una vez terminado el bucle, se devuelve todo el texto tablero que se imprimira como una especie de matriz
        return tablero
    #Aqui condicionamos la posicion de los jugadores para que se vea en consola
    def obtener_celda(self, posicion):
        jugadores_en_posicion = [jugador for jugador in self.jugadores if jugador.obtener_posicion() == posicion]
        #Mientras escribe cada una de las filas en los bucles de arriba, aqui se condiciona en que si algun número concuerda con la posición de algun jugador, se remplace ese número por los jugadores que esten en dicha posición junto a su color correspondiente
        if jugadores_en_posicion:
            jugadores_coloreados = [f"{jugador.color}[{jugador.nombre}]{Style.RESET_ALL}" for jugador in jugadores_en_posicion]
            return " | ".join(jugadores_coloreados) + " | "
        #De lo contrario se dibuja el numero en la fila normalmente
        else:
            return f"{posicion}      |"
    #Aqui hacemos una representación escrita de consola sobre en que posicion se encuentra el jugador con sus respectivos colores igualmente para que sea amigable a la vista
    def obtener_estado_jugadores(self):
        estado_jugadores = [f"{jugador.color}Jugador {i + 1}:{Style.RESET_ALL} Estas en la casilla {jugador.obtener_posicion()}\n" for i, jugador in enumerate(self.jugadores)]
        return "\n".join(estado_jugadores)
