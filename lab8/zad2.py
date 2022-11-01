import pygame
from pygame.draw import *
from random import randint
pygame.init()

FPS = 1
screen = pygame.display.set_mode((1200, 900))

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

score = 0

balls = []

def new_ball():
    '''
    Draws new ball with random coordinates and color
    '''
    x = randint(100, 1100)
    y = randint(100, 900)
    r = randint(10, 100)
    color = COLORS[randint(0, 5)]
    balls.append((color, x, y, r))
    
def draw_balls():
    '''
    Draws all balls
    '''
    for ball in balls:
        circle(screen, ball[0], (ball[1], ball[2]), ball[3])
        
def check_ball(ball, event):
    '''
    Checks if the ball was clicked
    '''
    global score
    distance_squared = (event.pos[0] - ball[1])**2 + (event.pos[1] - ball[2])**2
    if(distance_squared <= ball[3]**2):
        score += 1
        
def click(event):
    '''
    Checks if any of balls were clicked
    '''
    for ball in balls:
        check_ball(ball, event)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
            print("Your score is", score)
        if event.type == pygame.MOUSEBUTTONDOWN:
            click(event)
    balls.clear()
    new_ball()
    new_ball()
    draw_balls()
    pygame.display.update()
    screen.fill(BLACK)

pygame.quit()