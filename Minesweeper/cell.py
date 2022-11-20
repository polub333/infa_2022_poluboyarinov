import digit
import mine

class Cell:
    def __init__(self, x, y, number, content_type):
        self.content_type = content_type
        self._is_opened = False
        self._is_flagged = False
        self.x = x
        self.y = y
        if content_type == "mine":
            self.content = mine.Mine()
        else:
            self.content = digit.Digit(number)
    
    def is_open(self):
        return self._is_opened

    def is_flagged(self):
        return self._is_flagged

    def open(self):
        self._is_opened = True
        self._is_flagged = False

    def place_flag(self):
        if not self._is_opened:
            self._is_flagged = True


if __name__ == "__main__":
    print("This modulde is not for direct call")
