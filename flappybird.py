import pygame
from pygame.locals import *

pygame.init() #initializing pygame
#creating game window 
screen_width=500
screen_height=600
screen=pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Flappy Bird')

#creating game loop
run=True
while run:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False

pygame.quit()