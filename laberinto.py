# Importamos los módulos necesarios
import random
import sys

def ajustar_limite_recursion(ancho, alto):
    """
    Ajusta el límite de recursión basado en el tamaño del laberinto.
    """
    limite_recomendado = max(1000, ancho * alto * 4)
    sys.setrecursionlimit(limite_recomendado)

class Celda:
    """
    Representa una celda en el laberinto.
    """
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.paredes = {'N': True, 'S': True, 'E': True, 'O': True}
        self.visitada = False

class Laberinto:
    """
    Clase para generar y manejar el laberinto.
    """
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto
        ajustar_limite_recursion(ancho, alto)
        self.celdas = [[Celda(x, y) for y in range(alto)] for x in range(ancho)]
        self.entrada = None
        self.salida = None

    def generar_laberinto(self):
        """
        Genera el laberinto utilizando el algoritmo DFS recursivo.
        """
        try:
            celda_inicial = self.celdas[0][0]
            self._generar_laberinto_recursivo(celda_inicial)
        except RecursionError:
            print("Error: Se alcanzó el límite máximo de recursión. Intente con un laberinto más pequeño.")
            sys.exit(1)

    def _generar_laberinto_recursivo(self, celda_actual):
        celda_actual.visitada = True
        vecinos_no_visitados = self.obtener_vecinos_no_visitados(celda_actual)

        while vecinos_no_visitados:
            vecino = random.choice(vecinos_no_visitados)
            self.eliminar_paredes(celda_actual, vecino)
            self._generar_laberinto_recursivo(vecino)
            vecinos_no_visitados = self.obtener_vecinos_no_visitados(celda_actual)

    def obtener_vecinos_no_visitados(self, celda):
        vecinos = []

        direcciones = {
            'N': (0, -1),
            'S': (0, 1),
            'E': (1, 0),
            'O': (-1, 0)
        }

        for direccion, (dx, dy) in direcciones.items():
            nx, ny = celda.x + dx, celda.y + dy
            if 0 <= nx < self.ancho and 0 <= ny < self.alto:
                vecino = self.celdas[nx][ny]
                if not vecino.visitada:
                    vecinos.append(vecino)

        return vecinos

    def eliminar_paredes(self, celda_actual, celda_siguiente):
        dx = celda_siguiente.x - celda_actual.x
        dy = celda_siguiente.y - celda_actual.y

        if dx == 1:  # Celda siguiente está al Este
            celda_actual.paredes['E'] = False
            celda_siguiente.paredes['O'] = False
        elif dx == -1:  # Celda siguiente está al Oeste
            celda_actual.paredes['O'] = False
            celda_siguiente.paredes['E'] = False
        elif dy == 1:  # Celda siguiente está al Sur
            celda_actual.paredes['S'] = False
            celda_siguiente.paredes['N'] = False
        elif dy == -1:  # Celda siguiente está al Norte
            celda_actual.paredes['N'] = False
            celda_siguiente.paredes['S'] = False

    def establecer_entrada_salida(self):
        """
        Establece las posiciones de entrada y salida del laberinto.
        """
        self.entrada = self.celdas[0][0]
        self.entrada.paredes['O'] = False  # Abrimos la pared oeste de la entrada

        self.salida = self.celdas[self.ancho - 1][self.alto - 1]
        self.salida.paredes['E'] = False  # Abrimos la pared este de la salida