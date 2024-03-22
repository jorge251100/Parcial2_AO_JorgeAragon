class Dijkstra:  #Nombre de nuestra clase
    def __init__(self):   #Inicializa constructor
        self.grafo = {}    #Diccionario vacio en un inicio, es para las conexiones de los nodos

    def imprimir_solucion(self, distancias, ruta):   #Imprime una vez encontrado la ruta más corta
        print("Vertice \t Distancia desde el origen \t Ruta")
        for nodo in distancias:
            print(nodo, "\t\t", distancias[nodo], "\t\t\t\t", ruta[nodo])   #Los tabs para que se vea ordenado la salida

    def minima_distancia(self, distancias, conjunto): #Metodo para encontrar nodo con la distancia minima
        minimo = float('inf')
        minimo_nodo = None
        for nodo in distancias:
            if distancias[nodo] < minimo and not conjunto[nodo]:
                minimo = distancias[nodo]
                minimo_nodo = nodo
        return minimo_nodo

    def dijkstra(self, origen):   #Inicializa distancias desdel el dono de origen a todos los demás nodos con infinito exceptuando a root
        distancias = {nodo: float('inf') for nodo in self.grafo}
        distancias[origen] = 0
        conjunto = {nodo: False for nodo in self.grafo}  #Seguimiento de los nodos incluidos en el camino mas corto
        ruta = {nodo: '' for nodo in self.grafo}
        ruta[origen] = str(origen)

        for _ in range(len(self.grafo)):   #Iteraciones de comparacion de distancias
            u = self.minima_distancia(distancias, conjunto)
            conjunto[u] = True

            for v in self.grafo[u]:
                if not conjunto[v] and distancias[v] > distancias[u] + self.grafo[u][v]:
                    distancias[v] = distancias[u] + self.grafo[u][v]
                    ruta[v] = ruta[u] + " -> " + str(v)

        self.imprimir_solucion(distancias, ruta)


grafo = Dijkstra()  #Representación del grafo
grafo.grafo = {
    'a': {'b': 2, 'd': 5},  
    'b': {'e': 2, 'c': 3},
    'c': {'z': 7},
    'd': {'f': 6, 'e': 1},
    'e': {'g': 2, 'h': 5},
    'f': {},
    'g': {'z': 3},
    'h': {'i': 4},
    'i': {'z': 1},
    'z': {},
}
grafo.dijkstra('a')