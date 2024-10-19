# Importamos los módulos necesarios
class Visualizador:
    """
    Clase para visualizar el laberinto y su solución.
    """
    def __init__(self, laberinto):
        self.laberinto = laberinto

    def mostrar_laberinto(self, camino=None):
        """
        Muestra el laberinto en la consola. Si se proporciona un camino, lo muestra resaltado.
        """
        try:
            lab = self.laberinto
            ancho = lab.ancho
            alto = lab.alto
            lineas = []

            posiciones_camino = set()
            if camino:
                posiciones_camino = {(celda.x, celda.y) for celda in camino}

            # Línea superior
            linea_superior = ''
            for x in range(ancho):
                linea_superior += '+---'
            linea_superior += '+'
            lineas.append(linea_superior)

            # Filas intermedias
            for y in range(alto):
                linea_celdas = ''
                linea_paredes = ''
                for x in range(ancho):
                    celda = lab.celdas[x][y]

                    # Pared izquierda de la celda
                    if celda.paredes['O']:
                        linea_celdas += '|'
                    else:
                        linea_celdas += ' '

                    # Contenido de la celda
                    if (x, y) == (lab.entrada.x, lab.entrada.y):
                        linea_celdas += ' E '
                    elif (x, y) == (lab.salida.x, lab.salida.y):
                        linea_celdas += ' S '
                    elif (x, y) in posiciones_camino:
                        linea_celdas += ' * '
                    else:
                        linea_celdas += '   '

                    # Pared inferior de la celda
                    if celda.paredes['S']:
                        linea_paredes += '+---'
                    else:
                        linea_paredes += '+   '

                # Pared derecha de la última celda
                if lab.celdas[ancho - 1][y].paredes['E']:
                    linea_celdas += '|'
                else:
                    linea_celdas += ' '
                lineas.append(linea_celdas)

                # Línea inferior
                linea_paredes += '+'
                lineas.append(linea_paredes)

            # Imprimir el laberinto
            for linea in lineas:
                print(linea)
        except Exception as e:
            print(f"Ocurrió un error al mostrar el laberinto: {e}")