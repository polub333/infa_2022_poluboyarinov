import math
from random import choice, randint

import pygame


FPS = 30

RED = 0xFF0000
BLUE = 0x0000FF
YELLOW = 0xFFC91F
GREEN = 0x00FF00
MAGENTA = 0xFF03B8
CYAN = 0x00FFCC
BLACK = (0, 0, 0)
WHITE = 0xFFFFFF
GREY = 0x7D7D7D
GAME_COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

WIDTH = 800
HEIGHT = 600


class Ball:
    def __init__(self, screen: pygame.Surface, x=40, y=450):
        """ Конструктор класса ball

        Args:
        x - начальное положение мяча по горизонтали
        y - начальное положение мяча по вертикали
        """
        self.screen = screen
        self.x = x
        self.y = y
        self.r = 10
        self.vx = 0
        self.vy = 0
        self.color = choice(GAME_COLORS)
        self.live = 30

    def move(self):
        """Переместить мяч по прошествии единицы времени.

        Метод описывает перемещение мяча за один кадр перерисовки. То есть,
        обновляет значения self.x и self.y с учетом скоростей self.vx и
        self.vy, силы гравитации, действующей на мяч, и стен по краям окна
         (размер окна 800х600).
        """
        self.vy -= 1
        self.x += self.vx
        self.y -= self.vy
        self.process_collisions()

    def draw(self):
        pygame.draw.circle(
            self.screen,
            self.color,
            (self.x, self.y),
            self.r
        )

    def hittest(self, obj):
        """
        Функция проверяет сталкивалкивается ли данный обьект с целью,
        описываемой в обьекте obj.

        Args:
            obj: Обьект, с которым проверяется столкновение.
        Returns:
            Возвращает True в случае столкновения мяча и цели. В противном
            случае возвращает False.
        """

        if (self.x - obj.x)**2 + (self.y - obj.y)**2 < (self.r + obj.r)**2:
            return True
        return False

    def process_collisions(self):
        """
        Функция проверяет, произошло ли столкновение со стенками.
        Если произошло, умменьшает скорость в 0.75 раз
        """
        if self.x + self.r > WIDTH and self.vx >= 0:
            self.vx *= -1
            self.vx *= 0.75
            self.vy *= 0.75
        if self.y + self.r > HEIGHT and self.vy <= 0:
            self.vy *= -1
            self.vx *= 0.75
            self.vy *= 0.75


class Gun:
    def __init__(self, screen):
        self.x = 20
        self.y = 450
        self.screen = screen
        self.f2_power = 10
        self.f2_on = 0
        self.an = 1
        self.color = GREY
        self.tx = 100
        self.ty = 100
        self.points = 0
        self.pressed_keys = []

    def fire2_start(self, event):
        self.f2_on = 1

    def fire2_end(self, event):
        """Выстрел мячом.

        Происходит при отпускании кнопки мыши.
        Начальные значения компонент скорости мяча vx и vy
        зависят от положения мыши.
        """
        global balls, bullet
        bullet += 1
        new_ball = Ball(self.screen, self.x, self.y)
        new_ball.r += 5
        self.an = math.atan2((event.pos[1]-new_ball.y),
                             (event.pos[0]-new_ball.x))
        new_ball.vx = self.f2_power * math.cos(self.an)
        new_ball.vy = - self.f2_power * math.sin(self.an)
        balls.append(new_ball)
        self.f2_on = 0
        self.f2_power = 10

    def targetting(self, event):
        """Прицеливание. Зависит от положения мыши."""
        if event and event.pos[0] != self.y:
            self.an = math.atan((event.pos[1]-self.x) / (event.pos[0]-self.y))
            self.tx = event.pos[0]
            self.ty = event.pos[1]
        if self.f2_on:
            self.color = RED
        else:
            self.color = GREY

    def draw(self):
        dx = self.tx - self.x
        dy = self.ty - self.y
        r = (dx**2 + dy**2)**0.5
        dx *= self.f2_power * 4 / r
        dy *= self.f2_power * 4 / r
        pygame.draw.line(screen, self.color, (self.x, self.y),
                         (self.x+dx, self.y+dy), 7)

    def power_up(self):
        if self.f2_on:
            if self.f2_power < 100:
                self.f2_power += 1
            self.color = RED
        else:
            self.color = GREY

    def hit(self):
        self.points += 1

    def add_pressed_key(self, key):
        self.pressed_keys.append(key)

    def delete_pressed_key(self, key):
        self.pressed_keys.remove(key)

    def move(self):
        for pressed_key in self.pressed_keys:
            if pressed_key == pygame.K_a:
                self.x -= 5
            elif pressed_key == pygame.K_s:
                self.y += 5
            elif pressed_key == pygame.K_d:
                self.x += 5
            elif pressed_key == pygame.K_w:
                self.y -= 5


class Target:
    def __init__(self, screen):
        self.x = randint(600, 780)
        self.y = randint(300, 550)
        self.vx = randint(-6, 6)
        self.vy = randint(-6, 6)
        self.r = randint(2, 50)
        self.color = RED
        self.screen = screen

    def draw(self):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.r)

    def move(self):
        self.x += self.vx
        self.y += self.vy
        self.process_collisions()

    def process_collisions(self):
        if (self.x + self.r > WIDTH and self.vx > 0) or \
           (self.x - self.r < 0 and self.vx < 0):
            self.vx *= -1
        if (self.y + self.r > HEIGHT and self.vy > 0) or \
           (self.y - self.r < 0 and self.vy < 0):
            self.vy *= -1


pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
bullet = 0
balls = []

clock = pygame.time.Clock()
gun = Gun(screen)
targets = []
targets.append(Target(screen))
targets.append(Target(screen))

finished = False

while not finished:
    screen.fill(WHITE)
    gun.draw()
    for target in targets:
        target.draw()
    for b in balls:
        b.draw()
    pygame.display.update()

    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            gun.fire2_start(event)
        elif event.type == pygame.MOUSEBUTTONUP:
            gun.fire2_end(event)
        elif event.type == pygame.MOUSEMOTION:
            gun.targetting(event)
        elif event.type == pygame.KEYDOWN:
            gun.add_pressed_key(event.key)
        elif event.type == pygame.KEYUP:
            gun.delete_pressed_key(event.key)

    for b in balls:
        b.move()
        for target in targets:
            if b.hittest(target):
                gun.hit()
                targets.remove(target)
                targets.append(Target(screen))

    for target in targets:
        target.move()

    gun.move()
    gun.power_up()

pygame.quit()
