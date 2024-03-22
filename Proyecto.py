import folium  #Libreria de mapas interactivos
from scipy.spatial import Voronoi   #Librería para mapeo de areas de voronoi
import numpy as np  #Facilita el trabajo con matrices

#Coordenadas de las estaciones de bomberos y ubicación de un usuario
coordenadas_estaciones = [(17.110379025972755,-96.76052392391475),####
                          (17.093271951192623,-96.7130889901932), #### ESTAS SON LAS
                          (17.06012990712256,-96.6827062751867),  #### COORDENADAS DE
                          (17.049631554086798,-96.7153840221419), #### LAS ESTACIONES
                          ############################################################################################
                          (17.05286452507558, -96.58988476804771),
                          (17.005921968390876, -96.6331434333437),
                          #(17.050323824758504, -96.6319061724386),   #ESTAS SON
                          (17.157895970498462, -96.68417450176743),   #LAS COORDENADAS DE
                          (17.11506729035093, -96.8120384245724),     #LOS NODOS FRONTERA
                          (17.034850757713517, -96.7841625131224),
                          (17.00727488074701, -96.7072582192629),
                          (17.173291253652735, -96.7886632348041)]
#####################################################################################################################
coordenadas_usuario = (17.070963339727946, -96.70427614340011)   #lAS COORDENADAS DEL USUARIO

#Para que pueda enfocar en la posición del usuario, en 12 se pueden apreciar bien las regiones, aunque como es interactivo el mapa, se puede aumentar o reducir manualmente
mapa = folium.Map(location=coordenadas_usuario, zoom_start=12)

#Marcadores para las estaciones de bomberos y la posición del usuario
for estacion in coordenadas_estaciones[:4]:  #Para que no marque los nodos frontera, solo los que nos importan que son las estaciones
    folium.Marker(location=estacion, popup='Estación de Bomberos', icon=folium.Icon(color='red')).add_to(mapa)   #Marcador rojo para las estaciones de bomberos
    folium.Marker(location=coordenadas_usuario, popup='Tu posición', icon=folium.Icon(color='blue')).add_to(mapa)    #Marcador azul para la posición del usuario

#Calcula las regiones de Voronoi
vor = Voronoi(coordenadas_estaciones)

#Distancia mínimas entre el usuario y las estaciones de bomberos
distancias = [np.linalg.norm(np.array(coordenadas_usuario) - estacion) for estacion in coordenadas_estaciones]

# Estación de bomberos más cercana al usuario
estacion_cercana = coordenadas_estaciones[np.argmin(distancias)] #Mediante argmin

# Agrega marcador para la estación de bomberos más cercana
folium.Marker(location=estacion_cercana, popup='Estación más cercana', icon=folium.Icon(color='green')).add_to(mapa)  #Marcador verde

# Dibuja las líneas de Voronoi
for mediatriz in vor.ridge_vertices:  #Atributo propio de voronoi para el calculo
    if -1 not in mediatriz:   #No pueden pasar las crestas no validas, en voronoi se le llaman puntos degenerados
        line = [vor.vertices[mediatriz[0]], vor.vertices[mediatriz[1]]]   #Genera la mediatriz basados en los puntos actuales e iterando en los siguientes posteiormente
        folium.PolyLine(line, color='blue', weight=2).add_to(mapa)   #Para marcar las lineas en folium

# Mostrar el mapa
mapa