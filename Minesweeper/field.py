import random

import cell

class Field:
    def __init__(self, x, y, mines_num):
        self.x = x
        self.y = y
        self.mines_num = mines_num
        self.cells = [[]]
        self.fill_field()

    def fill_field(self):
        mines_pos = list(range(0, self.x*self.y))
        random.shuffle(mines_pos)
        for i in range(self.y):
            self.cells.append([])
            for j in range(self.x):
                if mines_pos[i*self.y + j] < self.mines_num:
                    self.cells[i].append(cell.Cell(j, i, 0, "mine"))
                else:
                    self.cells[i].append(cell.Cell(j, i, 0, "digit"))
        for i in range(self.y):
            for j in range(self.x):
                if self.cells[i][j].content_type == "mine":
                    continue
                mines_around = 0
                if i > 0:
                    mines_around += (self.cells[i-1][j].content_type == "mine")
                if i > 0 and j > 0:
                    mines_around += (self.cells[i-1][j-1].content_type == "mine")
                if i > 0 and j < self.x - 1:
                    mines_around += (self.cells[i-1][j+1].content_type == "mine")
                if i < self.y - 1:
                    mines_around += (self.cells[i+1][j].content_type == "mine")
                if i < self.y - 1 and j > 0:
                    mines_around += (self.cells[i+1][j-1].content_type == "mine")
                if i < self.y - 1 and j < self.x - 1:
                    mines_around += (self.cells[i+1][j+1].content_type == "mine")
                if j > 0:
                    mines_around += (self.cells[i][j-1].content_type == "mine")
                if j < self.x - 1:
                    mines_around += (self.cells[i][j+1].content_type == "mine")
                self.cells[i][j].content.set_number(mines_around)

    def open(self, x, y):
        
        if self.cells[y][x].content_type == "digit" and self.cells[y][x].is_open():
            mines_around = 0
            if y > 0 and self.cells[y-1][x].is_flagged():
                mines_around += 1
            if y > 0 and x > 0 and self.cells[y-1][x-1].is_flagged():
                mines_around += 1
            if y > 0 and x < self.x - 1 and self.cells[y-1][x+1].is_flagged():
                mines_around += 1
            if y < self.y - 1 and self.cells[y+1][x].is_flagged():
                mines_around += 1
            if y < self.y - 1 and x > 0 and self.cells[y+1][x-1].is_flagged():
                mines_around += 1
            if y < self.y - 1 and x < self.x - 1 and self.cells[y+1][x+1].is_flagged():
                mines_around += 1
            if x > 0 and self.cells[y][x-1].is_flagged():
                mines_around += 1
            if x < self.x - 1 and self.cells[y][x+1].is_flagged():
                mines_around += 1
            if mines_around == self.cells[y][x].content.number:
                if y > 0 and not self.cells[y-1][x].is_open() and not self.cells[y-1][x].is_flagged():
                    self.open(x, y-1)
                if y > 0 and x > 0 and not self.cells[y-1][x-1].is_open() and not self.cells[y-1][x-1].is_flagged():
                    self.open(x-1, y-1)
                if y > 0 and x < self.x - 1 and not self.cells[y-1][x+1].is_open() and not self.cells[y-1][x+1].is_flagged():
                    self.open(x+1, y-1)
                if y < self.y - 1 and not self.cells[y+1][x].is_open() and not self.cells[y+1][x].is_flagged():
                    self.open(x, y+1)
                if y < self.y - 1 and x > 0 and not self.cells[y+1][x-1].is_open() and not self.cells[y+1][x-1].is_flagged():
                    self.open(x-1, y+1)
                if y < self.y - 1 and x < self.x - 1 and not self.cells[y+1][x+1].is_open() and not self.cells[y+1][x+1].is_flagged():
                    self.open(x+1, y+1)
                if x > 0 and not self.cells[y][x-1].is_open() and not self.cells[y][x-1].is_flagged():
                    self.open(x-1, y)
                if x < self.x - 1 and not self.cells[y][x+1].is_open() and not self.cells[y][x+1].is_flagged():
                    self.open(x+1, y)

        self.cells[y][x].open()
        if self.cells[y][x].content_type == "digit" and self.cells[y][x].content.number == 0:
            if y > 0 and not self.cells[y-1][x].is_open():
                self.open(x, y-1)
            if y > 0 and x > 0 and not self.cells[y-1][x-1].is_open():
                self.open(x-1, y-1)
            if y > 0 and x < self.x - 1 and not self.cells[y-1][x+1].is_open():
                self.open(x+1, y-1)
            if y < self.y - 1 and not self.cells[y+1][x].is_open():
                self.open(x, y+1)
            if y < self.y - 1 and x > 0 and not self.cells[y+1][x-1].is_open():
                self.open(x-1, y+1)
            if y < self.y - 1 and x < self.x - 1 and not self.cells[y+1][x+1].is_open():
                self.open(x+1, y+1)
            if x > 0 and not self.cells[y][x-1].is_open():
                self.open(x-1, y)
            if x < self.x - 1 and not self.cells[y][x+1].is_open():
                self.open(x+1, y)

    def place_flag(self, x, y):
        self.cells[y][x].place_flag()

if __name__ == "__main__":
    print("This modulde is not for direct call")