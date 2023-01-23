import pygame, sys
from pygame.locals import *

pygame.init ()
DISPLAYSURF  = pygame.display.set_mode((800, 800))
pygame.display.set_caption('FAST DEVOURER')
while True: #main game loop
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
