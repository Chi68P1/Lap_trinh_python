#6.Game Over when Snake eat yourself

import pygame,time,sys,random

pygame.init()

screen = pygame.display.set_mode((810,630))

pygame.display.set_caption('Snake game by Nhóm 1')

WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLACK = (0,0,0)
BLUE = (0,0,255)

Running = True

foodx = round(random.randrange(1,25)) * 30.0
foody = round(random.randrange(1,19)) * 30.0

snakepos = [300,300]

snake = [[300,300]]
 
x1_change = 0       
y1_change = 0
 
clock = pygame.time.Clock()

def game_over():

    gfont = pygame.font.SysFont('consolas',40)
    gsurf = gfont.render('Game over!',True,RED)
    screen.blit(gsurf,[300,260])
    pygame.display.flip()
    time.sleep(3)

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
 
    snakepos[0] += x1_change
    snakepos[1] += y1_change

    if snakepos[0] >= 800 or snakepos[0] < 0 or snakepos[1] >= 600 or snakepos[1] < 0:
        Running = False

    for b in snake[1:]:
        if snakepos[0] == b[0] and snakepos[1] == b[1]:
            Running = False

    snake.append(list(snakepos))
    if snakepos[0] == foodx and snakepos[1] == foody:

        foodx = round(random.randrange(1,25)) * 30.0
        foody = round(random.randrange(1,19)) * 30.0
    else:
        snake.pop(0) #xóa vị trí đầu

    for i in snake:
        pygame.draw.rect(screen, BLUE, [i[0], i[1], 30, 30])

    pygame.draw.rect(screen, WHITE, [foodx, foody, 30, 30])    

    pygame.display.flip()
 
    clock.tick(10)

game_over()

pygame.quit()
sys.exit()



