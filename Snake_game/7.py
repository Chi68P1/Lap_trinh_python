#4.Game Over when Snake hits the boundaries

import pygame,time, sys 

pygame.init()

screen = pygame.display.set_mode((810,630))

pygame.display.set_caption('Snake game by Nhóm 1')

RED = (255, 0, 0)

BLACK = (0,0,0)

BLUE = (0,0,255)

Running = True
 
x1 = 300
y1 = 300
 
x1_change = 0       
y1_change = 0
 
clock = pygame.time.Clock()

def game_over():

    gfont = pygame.font.SysFont('consolas',40)
    gsurf = gfont.render('Game over!',True,RED)
    screen.blit(gsurf,[300,260])
    pygame.display.flip()
    time.sleep(2)

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

    if x1 >= 810 or x1 < 0 or y1 >= 630 or y1 < 0:
        Running = False

    pygame.draw.rect(screen, BLUE, [x1, y1, 30, 30])

    pygame.display.flip()
 
    clock.tick(15)

game_over()

pygame.quit()
sys.exit()




