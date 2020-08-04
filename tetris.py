import keyboard
from utils import setTimeout
from block import Block
from grid import Grid

# create grid
grid = Grid(10, 20)
# add first block to grid
grid.addBlock(Block())
# print grid out
grid.printGrid()
# add listeners
keyboard.on_press_key('left', grid.moveBlock)
keyboard.on_press_key('right', grid.moveBlock)
keyboard.on_press_key('down', grid.dropBlock)
keyboard.on_press_key('up', grid.rotateBlock)
while True:
    # if dropped block is invalid on spawn, game over
    gameNotOver = grid.dropBlock()
    if not gameNotOver:
        break
    # set 1 second timeout
    setTimeout(lambda: None, 1)
print('Game over')