import pygame
from pygame.draw import *
from random import randint
pygame.init()

FPS = 30
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
    Creates new ball with random coordinates and color
    '''
    x = randint(100, 1100)
    y = randint(100, 800)
    r = randint(10, 100)
    vel_x = randint(-10, 10)
    vel_y = randint(-10, 10)
    color = COLORS[randint(0, 5)]
    balls.append([color, x, y, r, vel_x, vel_y])
    
def draw_balls():
    '''
    Draws all balls
    '''
    for ball in balls:
        circle(screen, ball[0], (ball[1], ball[2]), ball[3])

def move_balls():
    '''
    Moves all balls
    '''
    for ball in balls:
        ball[1] += ball[4]
        ball[2] += ball[5]

def process_collosions():
    '''
    Handles wall collisions
    '''
    for ball in balls:
        if (ball[1] - ball[3] <= 0) and (ball[4] < 0):
            ball[4] = randint(-10, 10)  
        elif (ball[1] + ball[3] >= 1200) and (ball[4] > 0):
            ball[4] = randint(-10, 10) 
        elif (ball[2] - ball[3] <= 0) and (ball[5] < 0):
            ball[5] = randint(-10, 10) 
        elif (ball[2] + ball[3] >= 900) and (ball[5] > 0):
            ball[5] = randint(-10, 10) 
        
def click(event):
    '''
    Checks if any of the balls was clicked
    '''
    for ball in balls:
        global score
        distance_squared = (event.pos[0] - ball[1])**2 + (event.pos[1] - ball[2])**2
        if(distance_squared <= ball[3]**2):
            score += 1
            balls.remove(ball)
            new_ball()

def update_records(nickname):
    '''
    Reads from file, updates, writes to file and shows best records
    '''
    records = read_records_from_file()
    records.append((nickname, score))
    records.sort(key=lambda x: x[1], reverse=True)
    print_best_records(records)
    write_records_to_file(records)
    
def read_records_from_file():
    '''
    Reads records from file 'records.txt'
    '''
    with open("records.txt", "r") as f:
        records_str = f.readline().split()
        records = []
        for i in range(0, len(records_str), 2):
            records.append((records_str[i], int(records_str[i + 1])))
    return records

def write_records_to_file(records):
    '''
    Writes records to file 'records.txt'
    '''
    with open("records.txt", "w") as f:
        for record in records:
            f.write(str(record[0]) + " " + str(record[1]) + " ")

def print_best_records(records):
    '''
    Prints 5 best records
    '''
    print("5 best records:")
    for i in range(min(5, len(records))):
        print(records[i][0] + " - " + str(records[i][1]))

pygame.display.update()
clock = pygame.time.Clock()
finished = False

new_ball()
new_ball()

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            click(event)

    move_balls()
    process_collosions()
    draw_balls()
    pygame.display.update()
    screen.fill(BLACK)

pygame.quit()
print("Your score is", score, ". Enter your nickname:")
nickname = input()
update_records(nickname)
