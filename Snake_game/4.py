#1.Create the Screen

import pygame,sys

pygame.init()

screen = pygame.display.set_mode((810,630))

pygame.display.set_caption('Snake game by Nhóm 1')

BLACK = (0,0,0)

Running = True
while Running:
    screen.fill(BLACK)

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            Running = False

    pygame.display.flip()

pygame.quit()









