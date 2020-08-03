from random import randrange

class Block:
    squares = []
    def __init__(self):
        blockType = randrange(5)
        if blockType == 0:
            self.squares = [[3, 0], [4, 0], [5, 0], [6, 0]]
        elif blockType == 1:
            self.squares = [[3, 0], [4, 0], [4, 1], [5, 1]]
        elif blockType == 2:
            self.squares = [[3, 0], [4, 0], [3, 1], [4, 1]]
        elif blockType == 3:
            self.squares = [[3, 0], [4, 0], [3, 1], [2, 1]]
        elif blockType == 4:
            self.squares = [[3, 0], [4, 0], [5, 0], [4, 1]]

class Grid:
    curBlock = []
    def __init__(self, cols: int, rows: int):
        self.cols = cols
        self.rows = rows
        self.map = [[' ']*cols for i in range(self.rows)]
    
    def printGrid(self):
        for i in range(self.rows):
            for j in range(self.cols):
                print(self.map[i][j], end = '')
            print('\n')

    # def addBlock(self, Block):

    #     # adds random block at top of grid

    # def 

    # def nextCycle(self, )


# class Block:
    

grid = Grid(10, 20)
# while(true):
grid.printGrid()