import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((500, 500))

screen.fill((255, 255, 255))
circle(screen, (255, 255, 0), (250, 250), 200, 0)
circle(screen, (255, 0, 0), (150, 200), 40, 0)
circle(screen, (0, 0, 0), (150, 200), 15, 0)

circle(screen, (255, 0, 0), (350, 200), 30, 0)
circle(screen, (0, 0, 0), (350, 200), 10, 0)

rect(screen, (0, 0, 0), (125, 325, 250, 30), 0)
polygon(screen, (0, 0, 0), [(200, 200), (215, 185), (125, 95), (110, 110)])
polygon(screen, (0, 0, 0), [(300, 190), (285, 175), (410, 150), (425, 165)])

pygame.display.update()

clock = pygame.time.Clock()
while True:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()