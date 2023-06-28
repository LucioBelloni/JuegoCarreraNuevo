ANCHO_VENTANA =  700
ALTO_VENTANA = 900
FPS = 100

# ajustes del juego 
juego_terminado = False
velocidad = 2.5
score = 0
JUGANDO = 0

# bordes grosor  
tamanio_ancho = 15
tamanio_alto = 50

# construccion del camino y bordes 
#(115 x ) (0 y) (450 ancho)
camino = (115,0,450,ALTO_VENTANA)
borde_camino_izquierdo = (115,0,tamanio_ancho,ALTO_VENTANA)
borde_camino_derecho = (564,0,tamanio_ancho,ALTO_VENTANA)

# x cordenadas de carriles 
carril_izquierdo = 255
carril_central = 150
carril_derecho = 420
carriles = [carril_izquierdo,carril_central,carril_derecho]

# para animar el movimiento de los marcadores de carril
movimiento_de_carril_y = 0

# contadores

contador_vueltas_reinicio = 0
contador_tiempo_aceite = 0
contador_auto = 0
aumentador_velocidad_y = 0

#bandera nitro
bandera_nitro = True
bandera_gamer_over = 0
bandera_aceite = False
bandera_jugar = False
bandera_choque = True
