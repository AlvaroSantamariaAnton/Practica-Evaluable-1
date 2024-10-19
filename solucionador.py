# Importamos los módulos necesarios
from collections import deque

class Solucionador:
    """
    Clase para resolver el laberinto utilizando BFS.
    """
    def __init__(self, laberinto):
        self.laberinto = laberinto
        self.camino = []

    def resolver(self):
        """
        Resuelve el laberinto y almacena el camino de solución en self.camino.
        """
        try:
            inicio = self.laberinto.entrada
            fin = self.laberinto.salida

            previos = {}
            visitados = set()
            cola = deque()
            cola.append(inicio)
            visitados.add((inicio.x, inicio.y))

            while cola:
                celda_actual = cola.popleft()

                if celda_actual == fin:
                    break

                vecinos = self.obtener_vecinos(celda_actual)
                for vecino in vecinos:
                    pos = (vecino.x, vecino.y)
                    if pos not in visitados:
                        visitados.add(pos)
                        cola.append(vecino)
                        previos[pos] = (celda_actual.x, celda_actual.y)

            self.camino = []
            celda = fin
            while celda != inicio:
                self.camino.append(celda)
                pos = (celda.x, celda.y)
                if pos in previos:
                    x_prev, y_prev = previos[pos]
                    celda = self.laberinto.celdas[x_prev][y_prev]
                else:
                    print("No se encontró un camino.")
                    self.camino = []
                    return
            self.camino.append(inicio)
            self.camino.reverse()

        except Exception as e:
            print(f"Ocurrió un error al resolver el laberinto: {e}")
            self.camino = []

    def obtener_vecinos(self, celda):
        """
        Obtiene los vecinos accesibles de una celda.
        """
        vecinos = []

        direcciones = {
            'N': (0, -1),
            'S': (0, 1),
            'E': (1, 0),
            'O': (-1, 0)
        }

        for direccion, (dx, dy) in direcciones.items():
            if not celda.paredes[direccion]:
                nx, ny = celda.x + dx, celda.y + dy
                if 0 <= nx < self.laberinto.ancho and 0 <= ny < self.laberinto.alto:
                    vecino = self.laberinto.celdas[nx][ny]
                    vecinos.append(vecino)

        return vecinos