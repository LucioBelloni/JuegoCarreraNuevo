import pygame
from auxiliar import *
from autos_bots import * 

class Auto:
    def __init__(self,x,y) -> None:
        self.andar = getSupersficies("images/auto.png",1,1)
        self.paso1 = 0
        self.animacion = self.andar
        self.imagen = self.animacion[self.paso1]
        self.rect = self.imagen.get_rect()
        self.rect_1 = self.imagen.get_rect()
        self.rect.y = y
        self.rect.x = x
        self.score = 0 
        self.visible = True
        self.aceite = False

  
    def update(self):
        keys = pygame.key.get_pressed()
        if self.aceite == False:
            #cambio de pocicion del auto 
            if keys[pygame.K_a] and  self.rect.x > 135:
                self.rect.x -= 10
            if keys[pygame.K_d]and self.rect.x < 502:
                self.rect.x += 10 
        else:
            if keys[pygame.K_a] and self.rect.x < 502:
               self.rect.x += 10
            if keys[pygame.K_d]and self.rect.x > 135:
                self.rect.x -= 10


    def dibujar(self,pantalla):
        self.imagen = self.animacion[self.paso1]
        pantalla.blit(self.imagen,self.rect)
        #pygame.draw.rect(pantalla,color=(255,255,0),rect=self.rect)
        #pygame.draw.rect(pantalla,colores.RED,rect=self.rect_collition_frente)

    