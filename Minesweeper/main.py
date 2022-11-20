import pygame

import field

WIDTH = 700
HEIGHT = 560
FPS = 30

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

finished = False
FIELD_WIDTH = 16
FIELD_HEIGHT = 16
MINES_NUMBER = 40
field = field.Field(FIELD_WIDTH, FIELD_HEIGHT, MINES_NUMBER)
CELL_SIZE = 35

pygame.font.init()
font = pygame.font.SysFont('Times New Roman', 35 * CELL_SIZE // 50)
info_font = pygame.font.SysFont('Arial', 20)

time_passed = 0

def draw_field(screen, field):
    """
    Отрисовывает все клетки поля. Подсчитывает, сколько клеток открыто.
    Если открыты все клетки - вызывается функция победы в игре.
    """
    opened = 0
    for cell_row in field.cells:
        for cell in cell_row:
            if cell.is_open():
                opened += 1
                if cell.content_type == "mine":
                    pygame.draw.rect(screen, "red", (cell.x*CELL_SIZE, cell.y*CELL_SIZE, CELL_SIZE, CELL_SIZE))
                    lose_game()
                else:
                    pygame.draw.rect(screen, (220, 220, 220), (cell.x*CELL_SIZE, cell.y*CELL_SIZE, CELL_SIZE, CELL_SIZE))
                    pygame.draw.rect(screen, "gray", (cell.x*CELL_SIZE, cell.y*CELL_SIZE, CELL_SIZE, CELL_SIZE), 1)
                    if cell.content.number != 0:
                        text = font.render(str(cell.content.number), False, cell.content.color)
                        screen.blit(text, ((cell.x + 0.35)*CELL_SIZE, (cell.y + 0.1)*CELL_SIZE))
            elif cell.is_flagged():
                pygame.draw.polygon(screen, "red", [((cell.x + 0.2)*CELL_SIZE, (cell.y + 0.5)*CELL_SIZE),
                                                    ((cell.x + 0.8)*CELL_SIZE, (cell.y + 0.2)*CELL_SIZE),
                                                    ((cell.x + 0.8)*CELL_SIZE, (cell.y + 0.8)*CELL_SIZE)])
                pygame.draw.rect(screen, "black", (cell.x*CELL_SIZE, cell.y*CELL_SIZE, CELL_SIZE, CELL_SIZE), 3)
            else:
                pygame.draw.rect(screen, "gray", (cell.x*CELL_SIZE, cell.y*CELL_SIZE, CELL_SIZE, CELL_SIZE), 1)
    if opened == FIELD_WIDTH*FIELD_HEIGHT - MINES_NUMBER:
        win_game()

def draw_timer(time_passed):
    """
    Отрисовывает таймер, показывающий, сколько прошло времени.
    """
    text = info_font.render("Time: " + str(time_passed//1000), False, "black")
    screen.blit(text, (WIDTH - 120, 20))

def win_game():
    """
    Вызывается при победе в игре. Проверяет на новый рекорд,
    выводит прошедшее время в консоль.
    """
    global finished
    finished = True
    old_record = 0
    time = time_passed // 1000
    print("Time: " + str(time) + "s")
    with open("record.txt", "r") as f:
        old_record = f.read().rstrip()
    if(time < int(old_record)):
        print("New record! Previus record was " + old_record + "s")
        with open("record.txt", "w") as f:
            f.write(str(time))
    else:
        print("Curent record is " + old_record + "s")

def lose_game():
    """
    Вызывается, если игра проиграна.
    Выводит соответсвующее сообщение в консоль.
    """
    global finished
    finished = True
    print("You loser")

firstClick = True

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
                if firstClick:
                    firstClick = False
                    field.create_island(event.pos[0] // CELL_SIZE, event.pos[1] // CELL_SIZE)
                field.open(event.pos[0] // CELL_SIZE, event.pos[1] // CELL_SIZE)
            elif event.button == 3:         # Right mouse button
                field.place_flag(event.pos[0] // CELL_SIZE, event.pos[1] // CELL_SIZE)
    pygame.display.update()
