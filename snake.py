high_score = 0
deaths = 0
timer1 = 0
import pygame as p
import sys
from class_snake import Board, Snake 
import random
import time
while True:
    score = 0
    board = Board((600,650), 'lightgreen')
    snake = Snake(board.size[0]//30, 'blue', [[x*board.size[0]//30, 0] for x in range(0,4)],[0, 0])
    initial_length = snake.length
    print(snake.coords)
    #import class_snake as c

    p.init()

    #board = c.Board(600, ['red','white'])
    screen = p.display.set_mode(board.size)
    dir = {
    'up' : (0,-1),
    'down' : (0,1),
    'right' : (1,0),
    'left' : (-1,0)  
    }

    direction = (0, 0)
    placed = False
    #apple_coord = [0, 0]

    myFont = p.font.SysFont("Times New Roman", 18)

    while True:
        if snake.coords[-1] in snake.coords[0:len(snake.coords)-1]:
            deaths += 1
            high_score = score if score > high_score else high_score
            timer1 = p.time.get_ticks()//1000
            break
        for event in p.event.get():
            if event.type == p.QUIT: sys.exit()
            key_input = p.key.get_pressed() 
            if key_input[p.K_LEFT] or key_input[p.K_a]:
                if direction != dir['right']:
                    direction = dir['left']
                    break        
            if key_input[p.K_UP] or key_input[p.K_w]:
                if direction != dir['down']:
                    direction = dir['up']
                    break
            if key_input[p.K_RIGHT]or key_input[p.K_d]:
                if direction != dir['left']:
                    direction = dir['right']
                    break
            if key_input[p.K_DOWN]or key_input[p.K_s]:
                if direction != dir['up']:
                    direction = dir['down']
                    break
        # this code makes sure that if snake reaches border, it 
        # teleports to the other side of the screen
        if snake.coords[-1][0] < 0:
            snake.coords[-1][0] = 580
        if snake.coords[-1][0] > 580:
            snake.coords[-1][0] = 0
        if snake.coords[-1][1] < 0:
            snake.coords[-1][1] = 580 
        if snake.coords[-1][1] > 580:
            snake.coords[-1][1] = 0    
        #print(len(snake.coords))
    #  print(snake.length)
    
        #while len(snake.coords) > snake.length:
        snake.snake_move(direction)
        
        snake.coords = snake.coords[(len(snake.coords)-snake.length):]
        screen.fill(board.color)
        
        #print(snake.coords,'snake coord')
        # error fixed, error was that apple_coord stayed as [0, 0]
        # had to return it from apple_generator function and set
        # the new value of apple_coord to that value
        placed = snake.apple_generator(p, screen, snake.apple_coord, placed)
        score = snake.length - initial_length
        #print(snake.coords)
        snake.draw_snake(p,screen)
        p.draw.rect(screen, 'lightyellow', p.Rect(0, 600, 600,100))
        disp_score = myFont.render(f"Score: {score}", 1, 'black')
        disp_deaths = myFont.render(f"Deaths: {deaths}", 1, 'black')
        disp_High = myFont.render(f"High Score: {high_score}", 1, 'black')
        disp_time = myFont.render(f'Time: {abs(timer1 - p.time.get_ticks()//1000)} s', 1, 'black')
        screen.blit(disp_score, (10, 600))
        screen.blit(disp_deaths, (10, 630))
        screen.blit(disp_High, (480, 600))
        screen.blit(disp_time, (480, 630))
        print(snake.coords)
        #print(apple_coord, 'apple coord')
        p.time.delay(70)
        #print(snake.coords)
        #print(random.randrange(20), 'random number test')
        
        #print(snake.coords)
        p.display.flip()



# -----------------------------------------------------------------------------------
    # 1. if done extremely fast snake can go from up to down without turning left or right
    # thing of a solution for that.

    # 2. place variables like score and death before the first while loop and make extra space at bottom
    # of the screen for score and deaths and maybe a timer.

