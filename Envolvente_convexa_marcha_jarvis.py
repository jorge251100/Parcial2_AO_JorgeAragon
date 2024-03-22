def envolvente_convexa_jarvis(puntos):
    # Función para encontrar el punto más a la izquierda
    def punto_mas_izquierda(puntos):
        indice_min = 0
        for i in range(1, len(puntos)):
            # Comparar las coordenadas x primero
            if puntos[i][0] < puntos[indice_min][0]:
                indice_min = i
            # En caso de empate, comparar las coordenadas y
            elif puntos[i][0] == puntos[indice_min][0] and puntos[i][1] < puntos[indice_min][1]:
                indice_min = i
        return indice_min

    # Función para determinar si tres puntos forman un giro a la derecha
    def gira_derecha(p1, p2, p3):
        return (p2[0] - p1[0]) * (p3[1] - p1[1]) - (p2[1] - p1[1]) * (p3[0] - p1[0]) < 0

    # Comenzar desde el punto más a la izquierda
    punto_inicio = punto_mas_izquierda(puntos)
    punto_actual = punto_inicio
    envolvente = []

    # Algoritmo principal de Jarvis March
    while True:
        envolvente.append(puntos[punto_actual])
        siguiente_punto = (punto_actual + 1) % len(puntos)

        # Buscar el siguiente punto en la envolvente convexa
        for i in range(len(puntos)):
            if gira_derecha(puntos[punto_actual], puntos[i], puntos[siguiente_punto]):
                siguiente_punto = i

        punto_actual = siguiente_punto
        # Si volvemos al punto de inicio, se ha completado la envolvente convexa
        if punto_actual == punto_inicio:
            break

    return envolvente

# Ejemplo
puntos = [(0, 3), (1, 1), (2, 2), (4, 4), (0, 0), (1, 2), (3, 1), (3, 3)]
envolvente = envolvente_convexa_jarvis(puntos)
print("Envolvente convexa utilizando el algoritmo de Jarvis March:")
print(envolvente)
