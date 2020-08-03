import keyboard
from random import randrange
from utils import setTimeout

class Block:
    squares = []
    def __init__(self):
        blockType = randrange(5)
        if blockType == 0:
            self.squares = [[0, 3], [0, 4], [0, 5], [0, 6]]
        elif blockType == 1:
            self.squares = [[1, 4], [1, 5], [0, 3], [0, 4]]
        elif blockType == 2:
            self.squares = [[1, 3], [1, 4], [0, 3], [0, 4]]
        elif blockType == 3:
            self.squares = [[1, 3], [1, 2], [0, 3], [0, 4]]
        elif blockType == 4:
            self.squares = [[1, 4], [0, 3], [0, 4], [0, 5]]

class Grid:
    curBlock = []
    def __init__(self, cols: int, rows: int):
        self.cols = cols
        self.rows = rows
        self.map = [[' ']*cols for i in range(self.rows)]
    
    def printGrid(self):
        for i in range(self.rows):
            for j in range(self.cols):
                print('|' + self.map[i][j], end = '')
            print('|\n')
        print('\n')

    def addBlock(self, Block):
        self.curBlock = []
        for square in Block.squares:
            self.curBlock.append(square)
            if self.map[square[0]][square[1]] != ' ':
                return False
            self.map[square[0]][square[1]] = '\u2588'
        return True

    def validDrop(self) -> bool:
        for square in self.curBlock:
            row = square[0]
            col = square[1]
            if len(self.map) - 1 == row:
                return False
            if self.map[row+1][col] != ' ' and [row+1, col] not in self.curBlock:
                return False
        return True

    def dropBlock(self) -> bool:
        if not self.validDrop():
            validAdd = self.addBlock(Block())
            if not validAdd:
                return False
        else:
            for i in range(len(self.curBlock)):
                row = self.curBlock[i][0]
                col = self.curBlock[i][1]
                self.map[row][col] = ' '
                self.map[row+1][col] = '\u2588'
                self.curBlock[i][0] += 1
        return True

keyboard.wait('esc')
grid = Grid(10, 20)
grid.addBlock(Block())
while True:
    gameNotOver = grid.dropBlock()
    if not gameNotOver:
        break
    # detect rotation or horizontal change as many times as the user presses it,
    # and reprint the grid each time the user presses a key without
    # dropping the blocks
    setTimeout(grid.printGrid, 1)
print('Game over')