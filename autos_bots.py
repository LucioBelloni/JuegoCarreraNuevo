import random
import pygame
from constantes import *


class Auto_bots:
    def __init__(self) -> None:
        self.image = pygame.image.load("images/auto_bot{0}.png".format(random.randint(1,3)))
        self.image = pygame.transform.scale(self.image,(100,100))
        self.rect = self.image.get_rect()
        self.rect.x =  random.randrange(130,520,165)
        self.rect.y =  random.randrange(-3000,-150,200) 
        self.visible = True
        self.velocidad = 5
        self.bandera = True
        
        


    def update(self):
        self.rect.y += self.velocidad
        if self.rect.y > 900:
            self.rect.x = random.randrange(130,520,165)
            self.rect.y = random.randrange(-3000,-150,200) 
        #preguntar
        if self.bandera == True:
            pass

        if self.rect.y > 0 and self.rect.x >= carril_izquierdo and self.rect.x <= carril_derecho:
            self.rect.x += random.randrange(-100,10,159)

    def dibujar(self,pantalla):
        pantalla.blit(self.image,self.rect)

    # def reiniciar_posicion(self):
    #     self.rect.x = random.randrange(130,520,165)
    #     self.rect.y = random.randrange(-3000,-150,200) 

