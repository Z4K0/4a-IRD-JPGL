def laberinto(dimension, obstaculos):
    ''' Función que construye un laberinto cuadrado de una dimensión dada poniendo.

    Parámetros requeridos:
        - dimension: cantidad de columnas y filas usaremos un unico valor que siempregenerara una matriz cuadrada
        - obstaculos: Es una lista de tuplas con posiciones donde hay obstaculos.

    Salida: 
        Una matriz que representa el laberinto. 
    '''

    # Creamos una lista vacía para añadir las filas del laberinto.
    laberinto = []
    # Bucle  para añadir las filas del laberinto.
    for i in range(dimension):
        # Creamos una lista vacía para añadir las casillas de la fila.
        fila = []
        # Bucle  para recorrer las columnas del laberinto.
        for j in range(dimension):
            # Comprobar si la tupla está en el la lista de obstaculos.
            if tuple([i, j]) in obstaculos:
                fila.append('X')
            else:
                fila.append('0')
        laberinto.append(fila)
    return laberinto

# Tupla de posisiones de las celdas con obstaculos en el laberinto
obstaculo = ((0,1), (0,2), (0,3), (0,4), (1,1), (2,1), (2,3), (3,3), (4,0), (4,1), (4,2), (4,3)) 
# Tamaño de la matriz
dimension = 5
# llamada a la funcion una vez establecidos los valores de obstaculos
lab = laberinto(dimension, obstaculo)   

# Imprimnir el laberinto
# SOLO COMO EJEMPLO
for i in lab:
    print(''.join(i))

def encontrar_camino(laberinto, inicio, objetivo):
    def es_valida(x, y):
        return 0 <= x < len(laberinto) and 0 <= y < len(laberinto[0]) and laberinto[x][y] == '0'

    def encontrar_camino_recursivo(x, y):
        if (x, y) == objetivo:
            return True
        if es_valida(x, y):
            laberinto[x][y] = 'Visitado'
            if encontrar_camino_recursivo(x - 1, y):  # Arriba
                camino.append("arriba")
                return True
            if encontrar_camino_recursivo(x + 1, y):  # Abajo
                camino.append("abajo")
                return True
            if encontrar_camino_recursivo(x, y - 1):  # Izquierda
                camino.append("izquierda")
                return True
            if encontrar_camino_recursivo(x, y + 1):  # Derecha
                camino.append("derecha")
                return True
            laberinto[x][y] = '0'
            return False

    camino = []
    encontrar_camino_recursivo(inicio[0], inicio[1])
    camino.reverse()  # Revertir el camino para obtener la solución
    return camino

# Definir las coordenadas de inicio y objetivo
inicio = (0, 0)
objetivo = (4, 4)

# Encontrar el camino en el laberinto
solucion = encontrar_camino(lab, inicio, objetivo)

if solucion:
    print("El camino hacia el objetivo es:", " -> ".join(solucion))
else:
    print("No se encontró un camino hacia el objetivo.")
# Esperamos al usuario
input("presione enter para salir")