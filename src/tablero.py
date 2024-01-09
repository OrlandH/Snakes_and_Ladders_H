from colorama import Fore, Style
class Tablero:
    def __init__(self, jugadores):
        self.jugadores = jugadores
        self.serpientes = {16:6, 46:25, 49: 11, 62:19, 64:60, 74:53, 89:68, 92:88, 95:75, 99:80}
        self.escaleras = {2:38, 7:14, 8:31, 15:26, 21:42, 28:84, 36:44, 51:67, 71:91, 78:98, 87:94}

    def dibujar_tablero(self):
        tablero = "\n"
        rangopos = [100,80,60,40,20]
        rangoneg = [81,61,41,21,1]

        for contador in range(0,5):
            fila_tablero = ""

            for i in range(rangopos[contador], rangopos[contador]-10, -1):
                if i in self.serpientes:
                    fila_tablero += f"S{i}     |"
                elif i in self.escaleras:
                    fila_tablero += f"E{i}     |"
                else:
                    fila_tablero += self.obtener_celda(i)

            tablero += f"{fila_tablero}\n\n"  
            fila_tablero = ""

            for i in range(rangoneg[contador], rangoneg[contador]+10):
                if i in self.serpientes:
                    fila_tablero += f"S{i}     |"
                elif i in self.escaleras:
                    fila_tablero += f"E{i}     |"
                else:
                    fila_tablero += self.obtener_celda(i)

            tablero += f"{fila_tablero}\n\n"

        return tablero

    def obtener_celda(self, posicion):
        jugadores_en_posicion = [jugador for jugador in self.jugadores if jugador.obtener_posicion() == posicion]

        if jugadores_en_posicion:
            jugadores_coloreados = [f"{jugador.color}[{jugador.nombre}]{Style.RESET_ALL}" for jugador in jugadores_en_posicion]
            return " | ".join(jugadores_coloreados) + " | "
        else:
            return f"{posicion}      |"

    def obtener_estado_jugadores(self):
        estado_jugadores = [f"{jugador.color}Jugador {i + 1}:{Style.RESET_ALL} Estas en la casilla {jugador.obtener_posicion()}\n" for i, jugador in enumerate(self.jugadores)]
        return "\n".join(estado_jugadores)
