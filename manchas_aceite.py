import pygame
import random

class Mancha_aceite:
    def __init__(self) -> None:
        self.image_name = "images/mancha_de_aceite.png"
        self.image = pygame.image.load(self.image_name)
        self.image = pygame.transform.scale(self.image,(100,100))
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(130,520,165)  
        self.rect.y = random.randrange(-2000,0,200)     
        self.visible = True
    def update(self):
        self.rect.y += 5
        if self.rect.y > 900:
            self.rect.x = random.randrange(130,520,165)
            self.rect.y = random.randrange(-2000,0,200)    
    def dibujar(self,pantalla):
        pantalla.blit(self.image,self.rect)