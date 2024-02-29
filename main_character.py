from time import sleep
from typing import Any
import pygame
from pygame.sprite import Sprite
from pygame.image import load
from pygame.transform import scale

class HenrySkull(Sprite):
    image = scale(load('henry.png'), (250, 200))
    rect = image.get_rect(center=(100, 350))

    def update(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_SPACE]:
            self.pula()
        elif keys[pygame.K_LEFT]:
            self.anda_pra_esquerda()
        elif keys[pygame.K_RIGHT]:
            self.anda_pra_direita()
        else:
            self.desce()

    def anda_pra_direita(self):
        self.rect.x += 10

    def anda_pra_esquerda(self):
        self.rect.x -= 10

    def pula(self):
        self.rect.y -= 10
        # self.rect.x += 10
        print(self.rect.x)

    def desce(self):
        num_desce = 240 - self.rect.y
        self.rect.y += num_desce
        # self.rect.x += num_desce