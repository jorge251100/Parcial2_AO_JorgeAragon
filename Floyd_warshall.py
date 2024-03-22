INF = float('inf')  # Se define un valor infinito para representar la ausencia de una arista en el grafo.

def floyd_warshall(graph):
    n = len(graph)  # Se obtiene el número de vértices en el grafo.
    dist = [[INF] * n for _ in range(n)]  # Se inicializa una matriz para almacenar las distancias mínimas entre todos los pares de vértices.
    next_vertex = [[None] * n for _ in range(n)]  # Matriz para almacenar los próximos vértices en las rutas más cortas.

    # Se copian los pesos de las aristas del grafo a la matriz de distancias.
    for i in range(n):
        for j in range(n):
            dist[i][j] = graph[i][j]
            if graph[i][j] != INF and i != j:
                next_vertex[i][j] = j

    # Algoritmo de Floyd-Warshall para encontrar las distancias mínimas y las rutas.
    for k in range(n):
        for i in range(n):
            for j in range(n):
                # Se verifica si la distancia entre los vértices i y j se puede reducir pasando por el vértice k.
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
                    next_vertex[i][j] = next_vertex[i][k]

    return dist, next_vertex  # Se retornan la matriz con las distancias mínimas y la matriz de los próximos vértices en las rutas más cortas.

# Función para reconstruir la ruta entre dos vértices.
def reconstruct_path(start, end, next_vertex):
    path = [start + 1]  # Agregar 1 para representar el nodo como se desea
    while start != end:
        start = next_vertex[start][end]
        path.append(start + 1)  # Agregar 1 para representar el nodo como se desea
    return path


# Grafo
graph = [
    [0, 3, INF, 7],
    [8, 0, 2, INF],
    [5, INF, 0, 1],
    [2, INF, INF, 0]
]

# Se ejecuta el algoritmo de Floyd-Warshall para encontrar las distancias mínimas en el grafo.
result, next_vertex = floyd_warshall(graph)

# Se imprime la matriz resultante con las distancias mínimas entre todos los pares de vértices.
print("Matriz de distancias mínimas:")
for row in result:
    print(row)

# Se imprimen las rutas más cortas entre todos los pares de vértices.
print("\nRutas más cortas:")
for i in range(len(graph)):
    for j in range(len(graph)):
        if i != j:
            print(f"Ruta desde {i + 1} hasta {j + 1}: {reconstruct_path(i, j, next_vertex)}")
