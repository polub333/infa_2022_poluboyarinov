class Digit:
    def __init__(self, number):
        self.number = number
        self.color = "black"
        self.set_number(number)

    def set_number(self, number):
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
            color = (0, 0, 0)
        else:
            color = (255, 255, 0)
        self.color = color


if __name__ == "__main__":
    print("This modulde is not for direct call")
