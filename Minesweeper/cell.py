import digit
import mine

class Cell:
    def __init__(self, x, y, number, content_type):
        self.content_type = content_type
        self._is_opened = False
        self.x = x
        self.y = y
        if content_type == "mine":
            self.content = mine.Mine()
        else:
            self.content = digit.Digit(number)

        """
        self.number = number
        if number == 1:
            color = (0, 0, 255)
        elif number == 2:
            color = (0, 128, 0)
        elif number == 3:
            color = (255, 0, 0)
        elif number == 4:
            color = (75, 0, 130)
        elif number == 5:
            color = (128, 0, 0)
        elif number == 6:
            color = (64, 224, 208)
        elif number == 7:
            color = (255, 255, 255)
        else:
            color = (100, 100, 100)
        self.color = color
        """

    def is_open(self):
        return self._is_opened
    
    def open(self):
        self._is_opened = True


if __name__ == "__main__":
    print("This modulde is not for direct call")