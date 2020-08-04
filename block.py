from random import randrange

class Block:
    squares = []
    def __init__(self):
        self.type = randrange(5)
        if self.type == 0:
            self.squares = [[0, 3], [0, 4], [0, 5], [0, 6]]
        elif self.type == 1:
            self.squares = [[1, 4], [1, 5], [0, 3], [0, 4]]
        elif self.type == 2:
            self.squares = [[1, 3], [1, 4], [0, 3], [0, 4]]
        elif self.type == 3:
            self.squares = [[1, 3], [1, 2], [0, 3], [0, 4]]
        elif self.type == 4:
            self.squares = [[1, 4], [0, 3], [0, 4], [0, 5]]