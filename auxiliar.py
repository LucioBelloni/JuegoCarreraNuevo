import pygame

def getSupersficies(path,filas,columnas):
    lista = []
    superficie_imagen = pygame.image.load(path)
    fotograma_ancho = int(superficie_imagen.get_width()/columnas)
    fotograma_alto = int(superficie_imagen.get_height()/filas)

    for fila in range(filas):
        for columna in range(columnas):
            x = columna * fotograma_ancho
            y = fila * fotograma_alto
            #un pedacito de la imagen del sprite osea un fotograma 
            superficie_fotograma = superficie_imagen.subsurface(x,y,fotograma_ancho,fotograma_alto)
            lista.append(superficie_fotograma)

    return lista 






        
        

