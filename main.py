# Importamos los módulos necesarios
from laberinto import Laberinto
from solucionador import Solucionador
from visualizacion import Visualizador

# Definimos la función principal para el programa
def main():
    print("Bienvenido al generador y solucionador de laberintos.")

    # Establecer límites para el tamaño del laberinto
    MAX_TAMAÑO = 50
    MIN_TAMAÑO = 1

    # Validación de la entrada del ancho
    while True:
        try:
            ancho = int(input(f"Ingrese el ancho del laberinto ({MIN_TAMAÑO}-{MAX_TAMAÑO}): "))
            if not (MIN_TAMAÑO <= ancho <= MAX_TAMAÑO):
                raise ValueError(f"El ancho debe estar entre {MIN_TAMAÑO} y {MAX_TAMAÑO}.")
            break
        except ValueError as e:
            print(f"Entrada inválida: {e}")

    # Validación de la entrada del alto
    while True:
        try:
            alto = int(input(f"Ingrese el alto del laberinto ({MIN_TAMAÑO}-{MAX_TAMAÑO}): "))
            if not (MIN_TAMAÑO <= alto <= MAX_TAMAÑO):
                raise ValueError(f"El alto debe estar entre {MIN_TAMAÑO} y {MAX_TAMAÑO}.")
            break
        except ValueError as e:
            print(f"Entrada inválida: {e}")

    try:
        laberinto = Laberinto(ancho, alto)
        laberinto.generar_laberinto()
        laberinto.establecer_entrada_salida()

        visualizador = Visualizador(laberinto)
        print("\nLaberinto generado:")
        visualizador.mostrar_laberinto()

        solucionador = Solucionador(laberinto)
        solucionador.resolver()

        if solucionador.camino:
            print("\nSolución encontrada:")
            visualizador.mostrar_laberinto(solucionador.camino)
        else:
            print("No se encontró una solución para el laberinto.")

    except Exception as e:
        print(f"Ocurrió un error durante la ejecución: {e}")

# Ejecutar la función principal cuando el script se ejecuta directamente
if __name__ == "__main__":
    main()