import random

import cell

class Field:
    def __init__(self, x, y, mines_num):
        self.x = x
        self.y = y
        self.mines_num = mines_num
        self.cells = [[]]
        self.digits_pos = []
        self.init_field()
        self.place_mines()

    def init_field(self):
        for i in range(self.y):
            self.cells.append([])
            for j in range(self.x):
                self.cells[i].append(cell.Cell(j, i, 0, "digit"))
                self.digits_pos.append((i, j))

    def place_mines(self):
        mines_pos = list(range(0, self.x*self.y))
        random.shuffle(mines_pos)
        for i in range(self.y):
            for j in range(self.x):
                if mines_pos[i*self.y + j] < self.mines_num:
                    self.cells[i][j] = cell.Cell(j, i, 0, "mine")
                    self.digits_pos.remove((i, j))

    def create_island(self, x, y):
        for i in range(y-2 if y > 1 else 0, y+3 if x < self.y-2 else self.y):
            for j in range(x-2 if x > 1 else 0, x+3 if x<self.x-2 else self.x):
                if self.cells[i][j].content_type == "mine":
                    self.cells[i][j] = cell.Cell(j, i, 0, "digit")
                    new_mine_pos = random.randint(0, len(self.digits_pos)-1)
                    new_i = self.digits_pos[new_mine_pos][0]
                    new_j = self.digits_pos[new_mine_pos][1]
                    self.cells[new_i][new_j] = cell.Cell(new_j, new_i, 0, "mine")
                    self.digits_pos.remove((new_i, new_j))
        self.fill_field()

    def fill_field(self):
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
            if self.check_all_mines_around_are_open(x, y):
                self.open_around_filled_cell(x, y)
        self.cells[y][x].open()
        if self.cells[y][x].content_type == "digit" and self.cells[y][x].content.number == 0:
            self.open_around_empty_cell(x, y)


    def open_around_empty_cell(self, x, y):
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

    def check_all_mines_around_are_open(self, x, y):
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
        return mines_around == self.cells[y][x].content.number
    
    def open_around_filled_cell(self, x, y):
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
            

    def place_flag(self, x, y):
        self.cells[y][x].place_flag()

if __name__ == "__main__":
    print("This modulde is not for direct call")