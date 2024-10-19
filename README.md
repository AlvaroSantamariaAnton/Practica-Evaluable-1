# Generador y Solucionador de Laberintos en Python

## Descripción del Proyecto

Este proyecto es una aplicación en Python que genera laberintos aleatorios y encuentra la solución más corta desde la entrada hasta la salida. Utiliza algoritmos de búsqueda en profundidad (*Depth-First Search*, DFS) para la generación del laberinto y búsqueda en anchura (*Breadth-First Search*, BFS) para la resolución. El laberinto y su solución se muestran en la consola.

## Prerrequisitos

**Python 3.x**: Asegúrate de tener instalado Python versión 3.6 o superior.

Puedes verificar la versión instalada ejecutando:

```bash
python --version
```

## Ejecución del Programa

Para ejecutar el programa, sigue estos pasos:

1. **Asegúrate de estar en el directorio del proyecto**

2. **Ejecuta el archivo principal**

    ```bash	
    python main.py
    ```	

## Uso del programa

1. Inicio

    Al ejecutar el programa, verás un mensaje de bienvenida:

    ```python
    Bienvenido al generador y solucionador de laberintos.
    ```

2. Ingresar el tamaño del laberinto

    Se te solicitará que ingreses el ancho y alto del laberinto:

    ```python
    Ingrese el ancho del laberinto (1-50):
    Ingrese el alto del laberinto (1-50):
    ```
    - Ingresa valores enteros entre 1 y 50 para ambos.
    - Si ingresas un valor inválido, el programa te lo indicará y te pedirá que lo intentes nuevamente.

3. Generación y visualización del laberinto

    El programa generará el laberinto y lo mostrará en la consola.

    Ejemplo:

    ```pyhton
    Laberinto generado:
    +---+---+---+---+---+
    | E     |           |
    +   +   +---+   +   +
    |   |   |   |   |   |
    +   +   +   +---+   +
    |   |   |       |   |
    +   +---+---+   +   +
    |   |           |   |
    +   +   +---+---+   +
    |   |   |       | S |
    +---+---+---+---+---+
    ```

    - La entrada se marca con E y la salida con S.

4. Resolución del laberinto

    El programa resolverá el laberinto y mostrará el camino de solución:

    ```python
    Solución encontrada:
    +---+---+---+---+---+
    | E *   |           |
    +   +   +---+   +   +
    |   | * |   |   |   |
    +   +   +   +---+   +
    |   | * | * * * |   |
    +   +---+---+   +   +
    |   |       *   |   |
    +   +   +---+---+   +
    |   |   |       | S |
    +---+---+---+---+---+
    ```

    - El camino de solución está marcado con *.

5. Finalización

    Después de mostrar la solución, el programa terminará. Si deseas generar y resolver otro laberinto, simplemente ejecuta el programa nuevamente.