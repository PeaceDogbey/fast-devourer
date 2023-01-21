from tkinter import *
import random

#game setting
game_width = 700

GAME_HEIGHT =700

speed = 50
#The lower the speed the faster the snake

SPACE_SIZE = 60

BODY_PARTS = 4

SNAKE_COLOR ='orange'

FOOD_COLOR = '#000000'

BACKGROUND_COLOR = 'grey'



class snake:
    pass

class food:
    pass

def next_turn():
    pass

def change_direction(new_direction):
    pass

def check_collisions():
    pass

def game_over():
    pass


window = Tk ()
window.title('Fast devourer')
window.resizable(False, False)
score = 0
direction ='right'
window.mainloop (window, text ='score:{}'.format(score), font= 'consolas')