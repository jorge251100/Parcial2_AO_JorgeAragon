#Probado y elaborado en visual studio code

import pygame  #Para la ejemplificación grafica
import numpy as np #Se ocupa para hacer una copia de la matriz de forma más facil
import time  #Se ocupa para tiempo de relantización para que no vaya tan rapido

pygame.init()   #Inicializamos PyGame
width, height = 600, 600  #dimensiones de la ventana
bg = 25, 25 ,25 #Color background
screen  = pygame.display.set_mode((height, width))   #Creación de la ventana con display y relleno del bg
screen.fill(bg)

# Tamaño de la matriz
rangox, rangoy = 60, 60

# Estado de las celdas. Viva = 1 / Muerta = 0
gameState = np.zeros((rangox,  rangoy))

#dimensiones de cada celda individual
ancho = width / rangox
alto = height / rangoy

#Estado inicial 1
gameState[38, 20] = 1
gameState[39, 20] = 1
gameState[40, 20] = 1

#Estado inicial 2
gameState[10,5] = 1
gameState[12,5] = 1
gameState[11,6] = 1
gameState[12,6] = 1
gameState[11,7] = 1

#Estado inicial 3
gameState[5,10] = 1
gameState[5,12] = 1
gameState[6,11] = 1
gameState[6,12] = 1
gameState[7,11] = 1

#Estado inicial 4
gameState[18,15] = 1
gameState[17,16] = 1
gameState[17,15] = 1
gameState[18,16] = 1

#Estado inicial 5
gameState[30,20] = 1
gameState[31,20] = 1
gameState[32,20] = 1
gameState[32,19] = 1
gameState[33,19] = 1
gameState[34,19] = 1

# Bucle de ejecución
running = True  # Variable para controlar el bucle principal y poder cerrar el ciclo al dar clic en la x de la ventana
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False  # Salir del bucle principal si se da clic en la x de la ventana

    # Copia de la matriz del estado anterior
    # Para representar la matriz en el nuevo estado -> esto es importante porque el estado de juego se actualizará en cada iteración y así le pasamos los cambios de estado sin afectar la copia actual en la iteracion
    newGameState = np.copy(gameState)

    #Tiempo de relantización para que no vaya tan rapido
    time.sleep(0.1)

    #Se va limpiando el screen para actualizar el color del background
    screen.fill(bg)

    for y in range(0, rangox):
        for x in range (0, rangoy):

            # Calculamos el número de vecinos cercanos.
            n_neigh =   gameState[(x - 1) % rangox, (y - 1)  % rangoy] + \
                        gameState[(x)     % rangox, (y - 1)  % rangoy] + \
                        gameState[(x + 1) % rangox, (y - 1)  % rangoy] + \
                        gameState[(x - 1) % rangox, (y)      % rangoy] + \
                        gameState[(x + 1) % rangox, (y)      % rangoy] + \
                        gameState[(x - 1) % rangox, (y + 1)  % rangoy] + \
                        gameState[(x)     % rangox, (y + 1)  % rangoy] + \
                        gameState[(x + 1) % rangox, (y + 1)  % rangoy]

            # Regla #1 : Nacimiento: Una celda muerta con exactamente 3 vecinas vivas se convierte en una celda viva.
            if gameState[x, y] == 0 and n_neigh == 3:
                newGameState[x, y] = 1

            # Regla #2 : Muerte: Una celda viva con menos de 2 vecinas vivas (soledad) o más de 3 vecinas vivas (sobrepoblación) muere.
            elif gameState[x, y] == 1 and (n_neigh < 2 or n_neigh > 3):
                newGameState[x, y] = 0

            #Regla #3 : Sobrevivencia: Una celda viva con 2 o 3 vecinas vivas sigue viva para la siguiente generación. -> no se hace nada, continua viva

            # Calculamos el polígono que forma la celda.
            poly = [((x)   * ancho, y * alto),
                    ((x+1) * ancho, y * alto),
                    ((x+1) * ancho, (y+1) * alto),
                    ((x)   * ancho, (y+1) * alto)]

            # Si la celda está muerta pintamos un recuadro con borde gris
            if newGameState[x, y] == 0:
                pygame.draw.polygon(screen, (40, 40, 40), poly, 1)
           # Si la celda está viva pintamos un recuadro relleno
            else:
                pygame.draw.polygon(screen, (200, 100, 100), poly, 0)

    # Actualizamos el estado del juego.
    gameState = np.copy(newGameState)

    # Mostramos el resultado
    pygame.display.flip()

pygame.quit()  # Salir de Pygame después de que se cierra el ciclo por dar x en la ventana
