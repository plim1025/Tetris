import os
from block import Block

class Grid:
    curBlock = []
    curBlockType = 0
    curBlockRotation = 1
    score = 0
    tetris = False
    def __init__(self, cols: int, rows: int):
        self.cols = cols
        self.rows = rows
        self.map = [[' ']*cols for i in range(self.rows)]
    
    def printGrid(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print('Score: ' + str(self.score))
        for i in range(self.rows):
            for j in range(self.cols):
                print('|' + self.map[i][j], end = '')
            print('|\n')
        print('\n')

    def addBlock(self, Block):
        self.deleteFullRows()
        self.curBlock = []
        self.curBlockType = Block.type
        self.curBlockRotation = 1
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
            # goes below map or above map
            if row >= len(self.map) or row < 0:
                return False
            # goes off edge of left or right of map
            if col >= len(self.map[0]) or col < 0:
                return False
            # if map's spot is taken by one not already in block
            if self.map[row][col] != ' ' and [row, col] not in self.curBlock:
                return False
        return True

    def validDrop(self) -> bool:
        testBlock = []
        for square in self.curBlock:
            row = square[0]
            col = square[1]
            testBlock.append([row+1, col])
        return self.validBlock(testBlock)

    def validMove(self, move) -> bool:
        testBlock = []
        for square in self.curBlock:
            row = square[0]
            col = square[1]
            if move == 'right':
                testBlock.append([row, col+1])
            if move == 'left':
                testBlock.append([row, col-1])
        return self.validBlock(testBlock)
    
    def validRotate(self) -> bool:
        testBlock = []
        if self.curBlockType == 0:
            if self.curBlockRotation == 1:
                testBlock.append(self.curBlock[1])
                testBlock.append([self.curBlock[1][0]-1, self.curBlock[1][1]])
                testBlock.append([self.curBlock[1][0]+1, self.curBlock[1][1]])
                testBlock.append([self.curBlock[1][0]+2, self.curBlock[1][1]])
            elif self.curBlockRotation == 2:
                testBlock.append(self.curBlock[1])
                testBlock.append([self.curBlock[1][0], self.curBlock[1][1]-1])
                testBlock.append([self.curBlock[1][0], self.curBlock[1][1]+1])
                testBlock.append([self.curBlock[1][0], self.curBlock[1][1]+2])
        elif self.curBlockType == 1:
            if self.curBlockRotation == 1:
                testBlock.append(self.curBlock[1])
                testBlock.append(self.curBlock[2])
                testBlock.append([self.curBlock[0][0]-2, self.curBlock[0][1]])
                testBlock.append([self.curBlock[0][0]-1, self.curBlock[0][1]])
            elif self.curBlockRotation == 2:
                testBlock.append(self.curBlock[1])
                testBlock.append(self.curBlock[2])
                testBlock.append([self.curBlock[1][0], self.curBlock[1][1]-1])
                testBlock.append([self.curBlock[2][0], self.curBlock[2][1]+1])
        elif self.curBlockType == 2:
            if self.curBlockRotation == 1:
                testBlock.append(self.curBlock[0])
                testBlock.append(self.curBlock[3])
                testBlock.append([self.curBlock[3][0], self.curBlock[3][1]+1])
                testBlock.append([self.curBlock[3][0]-1, self.curBlock[3][1]+1])
            elif self.curBlockRotation == 2:
                testBlock.append(self.curBlock[0])
                testBlock.append(self.curBlock[3])
                testBlock.append([self.curBlock[1][0]+1, self.curBlock[1][1]])
                testBlock.append([self.curBlock[1][0], self.curBlock[1][1]-2])
        elif self.curBlockType == 3:
            if self.curBlockRotation == 1:
                testBlock.append(self.curBlock[0])
                testBlock.append(self.curBlock[1])
                testBlock.append([self.curBlock[0][0], self.curBlock[0][1]+1])
                testBlock.append([self.curBlock[1][0]-1, self.curBlock[1][1]])
            elif self.curBlockRotation == 2:
                testBlock.append(self.curBlock[0])
                testBlock.append(self.curBlock[2])
                testBlock.append([self.curBlock[0][0], self.curBlock[0][1]-1])
                testBlock.append([self.curBlock[2][0]-1, self.curBlock[2][1]])
            elif self.curBlockRotation == 3:
                testBlock.append(self.curBlock[2])
                testBlock.append(self.curBlock[3])
                testBlock.append([self.curBlock[3][0]-1, self.curBlock[3][1]])
                testBlock.append([self.curBlock[3][0]-1, self.curBlock[3][1]-1])
            elif self.curBlockRotation == 4:
                testBlock.append(self.curBlock[3])
                testBlock.append([self.curBlock[3][0], self.curBlock[3][1]-1])
                testBlock.append([self.curBlock[3][0], self.curBlock[3][1]+1])
                testBlock.append([self.curBlock[3][0]+1, self.curBlock[3][1]-1])
        elif self.curBlockType == 4:
            if self.curBlockRotation == 1:
                testBlock.append(self.curBlock[0])
                testBlock.append(self.curBlock[2])
                testBlock.append(self.curBlock[3])
                testBlock.append([self.curBlock[2][0]-1, self.curBlock[2][1]])
            elif self.curBlockRotation == 2:
                testBlock.append(self.curBlock[1])
                testBlock.append(self.curBlock[2])
                testBlock.append(self.curBlock[3])
                testBlock.append([self.curBlock[2][0], self.curBlock[2][1]-1])
            elif self.curBlockRotation == 3:
                testBlock.append(self.curBlock[0])
                testBlock.append(self.curBlock[1])
                testBlock.append(self.curBlock[2])
                testBlock.append([self.curBlock[2][0]+1, self.curBlock[2][1]])
            elif self.curBlockRotation == 4:
                testBlock.append(self.curBlock[0])
                testBlock.append(self.curBlock[2])
                testBlock.append(self.curBlock[3])
                testBlock.append([self.curBlock[2][0], self.curBlock[2][1]+1])
        return self.validBlock(testBlock)


    def dropBlock(self, keyPressed = None) -> bool:
        if not self.validDrop():
            validAdd = self.addBlock(Block())
            if not validAdd:
                self.printGrid()
                return False
        else:
            self.deleteCurBlockFromMap()
            for i in range(len(self.curBlock)):
                row = self.curBlock[i][0]
                col = self.curBlock[i][1]
                self.map[row+1][col] = '\u2588'
                self.curBlock[i][0] += 1
        self.printGrid()
        return True

    def moveBlock(self, keyPressed):
        move = 'right' if str(keyPressed) == 'KeyboardEvent(right down)' else 'left'
        if self.validMove(move):
            self.deleteCurBlockFromMap()
            for i in range(len(self.curBlock)):
                if move == 'right':
                    self.curBlock[i][1] += 1
                elif move == 'left':
                    self.curBlock[i][1] -= 1
            self.addCurBlockToMap()
            self.printGrid()
        
    def deleteCurBlockFromMap(self):
        for square in self.curBlock:
            row = square[0]
            col = square[1]
            self.map[row][col] = ' '

    def addCurBlockToMap(self):
        for square in self.curBlock:
            row = square[0]
            col = square[1]
            self.map[row][col] = '\u2588'

    def rotateBlock(self, keyPressed):
        if self.validRotate():
            self.deleteCurBlockFromMap()
            if self.curBlockType == 0:
                if self.curBlockRotation == 1:
                    self.curBlock[0] = [self.curBlock[1][0]-1, self.curBlock[1][1]]
                    self.curBlock[2] = [self.curBlock[1][0]+1, self.curBlock[1][1]]
                    self.curBlock[3] = [self.curBlock[1][0]+2, self.curBlock[1][1]]
                    self.curBlockRotation += 1
                elif self.curBlockRotation == 2:
                    self.deleteCurBlockFromMap()
                    self.curBlock[0] = [self.curBlock[1][0], self.curBlock[1][1]-1]
                    self.curBlock[2] = [self.curBlock[1][0], self.curBlock[1][1]+1]
                    self.curBlock[3] = [self.curBlock[1][0], self.curBlock[1][1]+2]
                    self.curBlockRotation = 1
            elif self.curBlockType == 1:
                if self.curBlockRotation == 1:
                    self.curBlock[0] = [self.curBlock[0][0]-1, self.curBlock[0][1]]
                    self.curBlock[3] = [self.curBlock[0][0]-1, self.curBlock[0][1]]
                    self.curBlockRotation += 1
                elif self.curBlockRotation == 2:
                    self.curBlock[0] = [self.curBlock[1][0], self.curBlock[1][1]-1]
                    self.curBlock[3] = [self.curBlock[2][0], self.curBlock[2][1]+1]
                    self.curBlockRotation = 1
            elif self.curBlockType == 2:
                if self.curBlockRotation == 1:
                    self.curBlock[1] = [self.curBlock[3][0], self.curBlock[3][1]+1]
                    self.curBlock[2] = [self.curBlock[3][0]-1, self.curBlock[3][1]+1]
                    self.curBlockRotation += 1
                elif self.curBlockRotation == 2:
                    self.curBlock[1] = [self.curBlock[1][0]+1, self.curBlock[1][1]]
                    self.curBlock[2] = [self.curBlock[3][0], self.curBlock[3][1]-1]
                    self.curBlockRotation = 1
            elif self.curBlockType == 3:
                if self.curBlockRotation == 1:
                    self.curBlock[2] = [self.curBlock[0][0], self.curBlock[0][1]+1]
                    self.curBlock[3] = [self.curBlock[1][0]-1, self.curBlock[1][1]]
                    self.curBlockRotation += 1
                elif self.curBlockRotation == 2:
                    self.curBlock[1] = [self.curBlock[0][0], self.curBlock[0][1]-1]
                    self.curBlock[3] = [self.curBlock[2][0]-1, self.curBlock[2][1]]
                    self.curBlockRotation += 1
                elif self.curBlockRotation == 3:
                    self.curBlock[0] = [self.curBlock[3][0]-1, self.curBlock[3][1]]
                    self.curBlock[1] = [self.curBlock[3][0]-1, self.curBlock[3][1]-1]
                    self.curBlockRotation += 1
                elif self.curBlockRotation == 4:
                    self.curBlock[0] = [self.curBlock[3][0]+1, self.curBlock[3][1]-1]
                    self.curBlock[1] = [self.curBlock[3][0], self.curBlock[3][1]-1]
                    self.curBlock[2] = [self.curBlock[3][0], self.curBlock[3][1]+1]
                    self.curBlockRotation = 1
            elif self.curBlockType == 4:
                if self.curBlockRotation == 1:
                    self.curBlock[1] = [self.curBlock[2][0]-1, self.curBlock[2][1]]
                    self.curBlockRotation += 1
                elif self.curBlockRotation == 2:
                    self.curBlock[0] = [self.curBlock[2][0], self.curBlock[2][1]-1]
                    self.curBlockRotation += 1
                elif self.curBlockRotation == 3:
                    self.curBlock[3] = [self.curBlock[2][0]+1, self.curBlock[2][1]]
                    self.curBlockRotation += 1
                elif self.curBlockRotation == 4:
                    self.curBlock[0] = [self.curBlock[2][0]+1, self.curBlock[2][1]]
                    self.curBlock[1] = [self.curBlock[2][0], self.curBlock[2][1]-1]
                    self.curBlock[3] = [self.curBlock[2][0], self.curBlock[2][1]+1]
                    self.curBlockRotation = 1
            self.addCurBlockToMap()
            self.printGrid()

    
    def deleteFullRows(self):
        rows = len(self.map)
        cols = len(self.map[0])
        rowsToDelete = []
        for i in range(rows):
            squaresFilled = 0
            for j in range(cols):
                if self.map[i][j] == ' ':
                    break
                squaresFilled += 1
            if squaresFilled == cols:
                rowsToDelete.append(i)

        for i in rowsToDelete:
            newMap = [[' ']*cols for i in range(rows)]
            for row in range(i):
                for col in range(cols):
                    if self.map[row][col] != ' ':
                        newMap[row+1][col] = '\u2588'
            for row in range(i+1, rows):
                for col in range(cols):
                    newMap[row][col] = self.map[row][col]
            self.map = newMap
    
        self.score += len(rowsToDelete)