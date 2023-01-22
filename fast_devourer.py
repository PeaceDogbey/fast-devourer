import pygame 
import time
import random

pygame.init

#game setting
white =(255, 255, 255)
black =(0, 0, 0)
red =(255, 0, 0)
orange =(255,165, 0)
width, height =600, 600

game_display = pygame.display.set_mode((width, height))
pygame.display.set_caption('Fast devourer')

clock =pygame.time.clock()

snake_size = 10
snake_speed = 20

message_font = pygame.font.sysfont('ubuntu', 40)
score_font = pygame.font.sysfont('unbutu', 30)

def print_score(score):
    text = score_font.render('score: ' + str(score), True, 'green')
    game_display.blit(text, [0, 0])

def draw_snake(snake_size, snake_pixels):
    for pixel in snake_pixels:
        pygame.draw.rect(game_display, white, [pixel[0], pixel[1], snake_size, snake_size])


def run_game():


    game_over = False

    game_close = False
    x = width / 2
    y = height / 2

    x_speed = 0
    Y_speed = 0

    snake_pixel = []
    snake_lenght = 1

    target_x = round(random.randrange(0, width-snake_size) / 10.0) * 10.0
    target_y = round(random.randrange(0, height-snake_size)/10.0)* 10.0
