import pygame
import math

from main_character import HenrySkull
from obstaculo import Obstaculo

pygame.init()

clock = pygame.time.Clock()
FPS = 60

SCREEN_WIDTH  = 1500
SCREEN_HEIGHT = 600

#create game window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('My game')

#load image
background = pygame.transform.scale(
    pygame.image.load('fundo.jpeg'),
    (SCREEN_WIDTH, SCREEN_HEIGHT))
bg_width = background.get_width()
bg_rect = background.get_rect()

#define game variables
scroll = 0
tiles = math.ceil(SCREEN_WIDTH / bg_width) + 1


henry = HenrySkull()
henry_group = pygame.sprite.GroupSingle(henry)

obstaculo = Obstaculo()
obstaculo_group = pygame.sprite.GroupSingle(obstaculo)

#game loop
run = True
while run:

    clock.tick(FPS)

    #draw scrolling background
    for i in range(0, tiles):
        screen.blit(background, (i * bg_width + scroll, 0))

    # scroll background
    scroll -= 5

    #reset scroll
    if abs(scroll) > bg_width:
        scroll = 0

    #event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    henry_group.draw(screen)
    henry_group.update()

    obstaculo_group.draw(screen)
    obstaculo_group.update()

    pygame.display.update()
pygame.quit()