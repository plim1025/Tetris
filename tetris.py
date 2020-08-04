import keyboard
from utils import setTimeout
from block import Block
from grid import Grid

grid = Grid(10, 20)
grid.addBlock(Block())
grid.printGrid()
keyboard.on_press_key('left', grid.moveBlock)
keyboard.on_press_key('right', grid.moveBlock)
keyboard.on_press_key('down', grid.dropBlock)
keyboard.on_press_key('up', grid.rotateBlock)
while True:
    gameNotOver = grid.dropBlock()
    if not gameNotOver:
        break
    setTimeout(lambda: None, 1)
print('Game over')