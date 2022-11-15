import pygame

import field

WIDTH = 700
HEIGHT = 560
FPS = 30

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

finished = False
field = field.Field(16, 16, 40)
cell_size = 35

pygame.font.init()
font = pygame.font.SysFont('Times New Roman', 35 * cell_size // 50)
info_font = pygame.font.SysFont('Arial', 20)

time_passed = 0

def draw_field(screen, field):
    for cell_row in field.cells:
        for cell in cell_row:
            if cell.is_open():
                if cell.content_type == "mine":
                    pygame.draw.rect(screen, "red", (cell.x*cell_size, cell.y*cell_size, cell_size, cell_size))
                else:
                    if cell.content.number == 0:
                        pygame.draw.rect(screen, "gray", (cell.x*cell_size, cell.y*cell_size, cell_size, cell_size))
                    else:
                        pygame.draw.rect(screen, cell.content.color, (cell.x*cell_size, cell.y*cell_size, cell_size, cell_size), 3)
                        text = font.render(str(cell.content.number), False, cell.content.color)
                        screen.blit(text, ((cell.x + 0.35)*cell_size, (cell.y + 0.1)*cell_size))
            elif cell.is_flagged():
                pygame.draw.polygon(screen, "red", [((cell.x + 0.2)*cell_size, (cell.y + 0.5)*cell_size),
                                                    ((cell.x + 0.8)*cell_size, (cell.y + 0.2)*cell_size),
                                                    ((cell.x + 0.8)*cell_size, (cell.y + 0.8)*cell_size)])
                pygame.draw.rect(screen, "black", (cell.x*cell_size, cell.y*cell_size, cell_size, cell_size), 3)

            else:
                pygame.draw.rect(screen, "gray", (cell.x*cell_size, cell.y*cell_size, cell_size, cell_size), 1)

def draw_timer(time_passed):
    text = info_font.render("Time: " + str(time_passed//1000), False, "black")
    screen.blit(text, (WIDTH - 120, 20))

while not finished:
    screen.fill("white")
    time_passed += clock.tick(FPS)

    draw_field(screen, field)
    draw_timer(time_passed)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:           # Left mouse button
                field.open(event.pos[0] // cell_size, event.pos[1] // cell_size)
            elif event.button == 3:         # Right mouse button
                field.place_flag(event.pos[0] // cell_size, event.pos[1] // cell_size)
    pygame.display.update()
