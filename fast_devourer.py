import pygame
import time
import random
import sys

pygame.init()

#colors
white = (255, 255, 255)
yellow = (255, 255, 0)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)
maroon = (128, 0, 0)
teal = ( 0, 128, 128)

happy_face = pygame.image.load('happy.jpeg')
happy_face_rect = happy_face.get_rect(center= (0, 0))

#the length of each side of the window
displayed_window_width = 600
displayed_window_height = 400

display_window = pygame.display.set_mode((displayed_window_width, displayed_window_height))
pygame.display.set_caption('FAST DEVOURER')

clock = pygame.time.Clock()

snake_head = 10
snake_speed = 15 

font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 20)

def Your_score(score):
    value = score_font.render("Your Score: " + str(score), True, black)
    display_window.blit(value, [0, 0]) #where [0, 0] is the position for the score

def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.ellipse(display_window, maroon, [x[0], x[1], snake_block, snake_block])

def message(msg, color):
    mesg = font_style.render(msg, True, color)
    display_window.blit(mesg, [displayed_window_width / 6, displayed_window_height / 3])

def gameLoop(): #main game
    game_over = False
    game_close = False

    x1 = displayed_window_width / 2
    y1 = displayed_window_height / 2

    x1_change = 0
    y1_change = 0

    snake_List = []
    Length_of_snake = 1

    foodx = round(random.randrange(0, displayed_window_width - snake_head) / 10.0) * 10.0
    foody = round(random.randrange(0, displayed_window_height- snake_head) / 10.0) * 10.0

    while not game_over:

        while game_close == True:
            display_window.fill(white)

            message("You Lost! Press C-Play Again or Q-Quit", red)
            Your_score(Length_of_snake - 1)
            pygame.display.update()
            

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()
                    
                    

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_head
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_head
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_head
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_head
                    x1_change = 0

        if x1 >= displayed_window_width or x1 < 0 or y1 >= displayed_window_height or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        display_window.fill(white)
        pygame.draw.rect(display_window, red, [foodx, foody, snake_head, snake_head])
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        our_snake(snake_head, snake_List)
        Your_score(Length_of_snake - 1)

        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, displayed_window_width - snake_head) / 10.0) * 10.0
            foody = round(random.randrange(0, displayed_window_height - snake_head) / 10.0) * 10.0
            Length_of_snake += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()

gameLoop()