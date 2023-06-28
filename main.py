import pygame
from constantes import *
import colores 
import random
from auto import * 
from autos_bots import * 
from manchas_aceite import *
from date_base import * 

pygame.init()

screen = pygame.display.set_mode((ANCHO_VENTANA,ALTO_VENTANA))
pygame.display.set_caption("Juego Auto")

#generar auto
auto = Auto(320,760)


explocion_auto = pygame.image.load("images/explocionauto.png")
explocion_auto = pygame.transform.scale(explocion_auto, (120,150))

# imagenes jugar y score 
fondo_menu = pygame.image.load("images/fondo_pista.jpg")
fondo_menu = pygame.transform.scale(fondo_menu,(ANCHO_VENTANA,ALTO_VENTANA))

imagen_jugar = pygame.image.load("images/boton_start_game.png")
imagen_jugar = pygame.transform.scale(imagen_jugar,(100,100))

imagen_score = pygame.image.load("images/buton_score.png")
imagen_score = pygame.transform.scale(imagen_score,(100,100))

# volver al inicio 
imagen_volver_atras = pygame.image.load("images/volver_atras.png")
imagen_volver_atras = pygame.transform.scale(imagen_volver_atras,(150,150))

#game over
imagen_game_over = pygame.image.load("images/game_over_copia.png")
imagen_game_over = pygame.transform.scale(imagen_game_over, (500,500))

#fondo score 
fondo_score = pygame.image.load("images/fondo_score.jpg")
fondo_score = pygame.transform.scale(fondo_score,(ANCHO_VENTANA,ALTO_VENTANA))


#sonido nitro
pygame.mixer.init()
nitro = pygame.mixer.Sound("sound/N0S.mp3")
nitro.set_volume(0.3)

# sonido choque 

pygame.mixer.init()
choque = pygame.mixer.Sound("sound/explocion.mp3")
choque.set_volume(0.3)

# crear listas vacias 
lista_bots = []
lista_aceite = []

#crear manchas  de aceite
mancha_aceite = Mancha_aceite()
lista_aceite.append(mancha_aceite)

#crear autos bots

for i in range(5):
    auto_bots = Auto_bots()
    lista_bots.append(auto_bots)

#Titulo 

font_titulo = pygame.font.SysFont("Arial",80)
titulo = 'Juego Auto'
titulo_rect = pygame.Rect(150,20,150,40)

#ingreso de texto del usuario 

font_input = pygame.font.SysFont("Arial",30)
ingreso = ''
ingreso_rect = pygame.Rect(280,620,150,40)

# ingresar nombre

font_nombre = pygame.font.SysFont("Arial",30)
ingreso_nombre = 'Ingrese su nombre'
ingreso_nombre_rect = pygame.Rect(240,570,150,40)

# crear fila nombre

font_nombre_score = pygame.font.SysFont("Arial",30)
nombre_score = 'Player'
rect_nombre_score = pygame.Rect(130,170,150,40)

#crear fila score

font_scrore = pygame.font.SysFont("Arial",30)
score_nombre = 'Score'
rect_score = pygame.Rect(330,170,150,40)

#time
reloj = pygame.time.Clock()
clock = pygame.time.get_ticks()

#crear database
generar_db()

flag_correr = True

while flag_correr:
    reloj.tick(FPS)        
    if JUGANDO == 0:
        screen.blit(fondo_menu,(0,0))
        jugar_rect = pygame.draw.rect(screen,colores.WHITE,(200,700,100,100))
        screen.blit(imagen_jugar,(jugar_rect.x,jugar_rect.y))

        score_rect = pygame.draw.rect(screen,colores.WHITE,(400,700,100,100))
        screen.blit(imagen_score,(score_rect.x,score_rect.y))

        font_nombre_surface = font_nombre.render(ingreso_nombre,True,colores.WHITE)
        screen.blit(font_nombre_surface,(ingreso_nombre_rect.x,ingreso_nombre_rect.y))

        font_titulo_surface = font_titulo.render(titulo,True,colores.WHITE)
        screen.blit(font_titulo_surface,(titulo_rect.x,titulo_rect.y))

        pygame.draw.rect(screen,colores.BLACK,ingreso_rect,2)
        font_input_surface = font_input.render(ingreso,True,colores.WHITE)
        screen.blit(font_input_surface,(ingreso_rect.x,ingreso_rect.y))
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                flag_correr = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if jugar_rect.collidepoint(event.pos) and ingreso[0:1]:
                    JUGANDO = 1
                    # reinicio  datos del juego
                    if auto.visible == False:
                        JUGANDO = 1
                        auto.visible = True
                        auto.score = 0
                        velocidad = 2
                        auto_bots.rect.y = 5
                        contador_vueltas_reinicio = 0
                        bandera_nitro = True
                        bandera_choque = True
                        auto = Auto(320,760)
                        mancha_aceite = Mancha_aceite()
                        lista_aceite.append(mancha_aceite)
                        for i in range(5):
                            auto_bots = Auto_bots()
                            lista_bots.append(auto_bots)

                if score_rect.collidepoint(event.pos):
                    JUGANDO = 2
                # verico si presiono backspace para volver hacia atras en el texto
                # unicode es una base de datos que tiene los datos guardados
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    ingreso = ingreso[0:-1]
                else:
                    ingreso += event.unicode
    #menu de scores           
    elif JUGANDO == 2:
        lista_scores = ordenar_datos()
        volver_atras_rect = pygame.draw.rect(screen,colores.RED,(540,100,150,130))
        screen.blit(fondo_score,(0,0))
        screen.blit(imagen_volver_atras,(volver_atras_rect.x,volver_atras_rect.y))
        font_nombre_score_surface = font_nombre_score.render(nombre_score,True,colores.BLACK)
        screen.blit(font_nombre_score_surface,(rect_nombre_score.x,rect_nombre_score.y))
    


        font_score_surface = font_scrore.render(score_nombre,True,colores.BLACK)
        screen.blit(font_score_surface,(rect_score.x,rect_score.y))
        
        i = 0
        contador = 0
        for e_lista in lista_scores:
            contador+= 1
            if contador <= 10:
                font_nombre_usurio = pygame.font.SysFont("Arial", 30)
                text_usuario = e_lista[1]
                score_menu = e_lista[2]
                texto_menu_usario = font_nombre_usurio.render("     {0}          |    {1} ".format(text_usuario,score_menu),True,(255,255,255))
                i += 45
                screen.blit(texto_menu_usario,(100,i + 170))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                flag_correr = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if volver_atras_rect.collidepoint(event.pos):
                    JUGANDO = 0
                    
    #juego 
    elif JUGANDO == 1: 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                flag_correr = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                print(event.pos)
            if auto.rect.colliderect(mancha_aceite.rect):
                auto.aceite = True
            if contador_auto % 2 == 2:
                auto.aceite = False
            auto.update()
            
                    
        for auto_bots in lista_bots:
            if auto_bots.rect.y >= ALTO_VENTANA :
                auto.score += 1
                contador_auto += 1 
                if auto.score > 10:
                    if bandera_nitro == True:
                        nitro.play()
                        bandera_nitro = False
                    velocidad = 7
                    
              

            if auto.rect.colliderect(auto_bots.rect):
                subir_data(ingreso,auto.score)
                auto.visible = False
                auto_bots.visible = False

        #dibujar la fondo 
        screen.fill(colores.GREEN)
        # dibujar camino
        rect_camino = pygame.draw.rect(screen,colores.GRIS,camino)
        #dibujar bordes del camino
        rect_borde_camino_izquierdo = pygame.draw.rect(screen,colores.RED,borde_camino_izquierdo)
        rect_borde_camino_derecho = pygame.draw.rect(screen,colores.RED,borde_camino_derecho)
        
        #dibujar carril y su movimiento 
        movimiento_de_carril_y += velocidad * 1.5
        if movimiento_de_carril_y >= tamanio_alto * 2:
            movimiento_de_carril_y = 0
        for i in range(tamanio_alto * -2, ALTO_VENTANA, tamanio_alto * 2):
            rect_carril_izquierdo = pygame.draw.rect(screen,colores.WHITE,(carril_izquierdo , i + movimiento_de_carril_y,tamanio_ancho,tamanio_alto))
            rect_carril_derecho = pygame.draw.rect(screen,colores.WHITE,(carril_derecho , i + movimiento_de_carril_y,tamanio_ancho,tamanio_alto))
                
        if auto.visible == True:
            auto.dibujar(screen)
        else:
            screen.blit(explocion_auto,(auto.rect.x -30 ,auto.rect.y -40))
            screen.blit(imagen_game_over,(100,100,300,120))
            if bandera_choque == True:
                choque.play()
                bandera_choque = False
            
            contador_vueltas_reinicio +=1
            movimiento_de_carril_y = 0
            lista_bots = []
            lista_aceite = []
            if contador_vueltas_reinicio == 90:  
                nitro.stop()
                JUGANDO = 0

        #creacion de autos_bots y mancha de aceite 
        for mancha_aceite in lista_aceite:
            mancha_aceite.update()
            mancha_aceite.dibujar(screen)

        for bots in lista_bots: 
            bots.update()
            bots.dibujar(screen)
        
        
        font = pygame.font.SysFont("Arial",25)
        texto = font.render("Score: {0} ".format(auto.score),True,colores.WHITE)
        texto_rect = (0, 827)
        screen.blit(texto,texto_rect)
    pygame.display.flip()

pygame.quit()
    