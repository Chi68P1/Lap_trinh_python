#2.Create the Snake

import pygame, sys 

pygame.init()

screen = pygame.display.set_mode((810,630))

pygame.display.set_caption('Snake game by Nhóm 1')

BLACK = (0,0,0)

BLUE = (0,0,255)

Running = True
while Running:

    screen.fill(BLACK)
    
    for event in pygame.event.get(): 
        if event.type==pygame.QUIT:
            Running = False

    pygame.draw.rect(screen, BLUE ,[300,300,30,30])


    pygame.display.flip()

pygame.quit()
sys.exit()



