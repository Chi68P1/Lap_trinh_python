#3.Moving the Snake

import pygame, sys 

pygame.init()

screen = pygame.display.set_mode((810,630))

pygame.display.set_caption('Snake game by Nhóm 1')

BLACK = (0,0,0)

BLUE = (0,0,255)

Running = True
 
x1 = 300
y1 = 300
 
x1_change = 0       
y1_change = 0
 
clock = pygame.time.Clock()
 
while Running:

    screen.fill(BLACK)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x1_change = -30
                y1_change = 0
            elif event.key == pygame.K_RIGHT:
                x1_change = 30
                y1_change = 0
            elif event.key == pygame.K_UP:
                y1_change = -30
                x1_change = 0
            elif event.key == pygame.K_DOWN:
                y1_change = 30
                x1_change = 0
 
    x1 += x1_change
    y1 += y1_change

    pygame.draw.rect(screen, BLUE, [x1, y1, 30, 30])

    pygame.display.flip()
 
    clock.tick(15)
 
pygame.quit()
sys.exit()
