import pygame

import field

WIDTH = 600
HEIGHT = 400
FPS = 30

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
pygame.font.init()
font = pygame.font.SysFont('Times New Roman', 35)

finished = False
field = field.Field()
cell_size = 50

def draw_field(screen, field):
    for cell_row in field.cells:
        for cell in cell_row:
            if cell.is_open():
                if cell.content_type == "mine":
                    print("Boom")
                else:
                    pygame.draw.rect(screen, cell.content.color, (cell.x*cell_size, cell.y*cell_size, cell_size, cell_size), 3)
                    text = font.render(str(cell.content.number), False, cell.content.color)
                    screen.blit(text, ((cell.x + 0.35)*cell_size, (cell.y + 0.1)*cell_size))


screen.fill("white")
while not finished:
    clock.tick(FPS)

    draw_field(screen, field)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:           # Left mouse button
                field.open(event.pos[0] // cell_size, event.pos[1] // cell_size)
            elif event.button == 3:         # Right mouse button
                field.place_flag(event.pos[0] // cell_size, event.pos[1] // cell_size)
    pygame.display.update()
