import random

import cell

class Field:
    def __init__(self):
        self.cells = [[]]
        mines_pos = list(range(0, 100))
        random.shuffle(mines_pos)
        for i in range(10):
            self.cells.append([])
            for j in range(10):
                #if i*50 + j < 20:
                    #self.cells[i].append(cell.Cell(j, i, 0, "mine"))
                #else:
                    self.cells[i].append(cell.Cell(j, i, random.randint(1, 7), "digit"))

    def open(self, x, y):
        self.cells[y][x].open()

if __name__ == "__main__":
    print("This modulde is not for direct call")