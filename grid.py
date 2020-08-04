import os
from block import Block

class Grid:
    curBlock = []
    curBlockType = 0
    curBlockRotation = 1
    def __init__(self, cols: int, rows: int):
        self.cols = cols
        self.rows = rows
        self.map = [[' ']*cols for i in range(self.rows)]
    
    def printGrid(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        for i in range(self.rows):
            for j in range(self.cols):
                print('|' + self.map[i][j], end = '')
            print('|\n')
        print('\n')

    def addBlock(self, Block):
        self.curBlock = []
        self.curBlockType = Block.type
        for square in Block.squares:
            self.curBlock.append(square)
            if self.map[square[0]][square[1]] != ' ':
                return False
            self.map[square[0]][square[1]] = '\u2588'
        return True

    # determines whether given block is a valid move based on current grid and previous block
    def validBlock(self, block) -> bool:
        for square in block:
            row = square[0]
            col = square[1]
            # goes below map
            if row >= len(self.map):
                return False
            # goes off edge of left or right of map
            if col >= len(self.map[0]) or col < 0:
                return False
            # if map's spot is taken by one not already in block
            if self.map[row][col] != ' ' and [row, col] not in self.curBlock:
                return False
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

    def validMove(self, move) -> bool:
        for square in self.curBlock:
            row = square[0]
            col = square[1]
            if move == 'right' and len(self.map[0]) - 1 == col:
                return False
            if move == 'left' and col == 0:
                return False
            if move == 'right' and self.map[row][col+1] != ' ' and [row, col+1] not in self.curBlock:
                return False
            if move == 'left' and self.map[row][col-1] != ' ' and [row, col-1] not in self.curBlock:
                return False
        return True
    
    def validRotate(self) -> bool:
        if self.curBlockType == 0:
            if self.curBlockRotation == 1:
                self.map
                self.curBlockRotation += 1
            elif self.curBlockRotation == 2:
                self.curBlockRotation = 1
    #     elif self.curBlockType == 1:

    #     elif self.curBlockType == 2:

    #     elif self.curBlockType == 3:
        
    #     elif self.curBlockType == 4:


    def dropBlock(self, keyPressed = None) -> bool:
        if not self.validDrop():
            validAdd = self.addBlock(Block())
            if not validAdd:
                self.printGrid()
                return False
        else:
            for i in range(len(self.curBlock)):
                row = self.curBlock[i][0]
                col = self.curBlock[i][1]
                self.map[row][col] = ' '
                self.map[row+1][col] = '\u2588'
                self.curBlock[i][0] += 1
        self.printGrid()
        return True

    def moveBlock(self, keyPressed):
        move = 'right' if str(keyPressed) == 'KeyboardEvent(right down)' else 'left'
        if self.validMove(move):
            for i in range(len(self.curBlock)):
                row = self.curBlock[i][0]
                col = self.curBlock[i][1]
                self.map[row][col] = ' '
                if move == 'right':
                    self.curBlock[i][1] += 1
                elif move == 'left':
                    self.curBlock[i][1] -= 1
            for square in self.curBlock:
                row = square[0]
                col = square[1]
                self.map[row][col] = '\u2588'
            self.printGrid()
        
    # def rotateBlock(self, keyPressed):