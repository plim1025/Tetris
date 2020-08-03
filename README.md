# Tetris
Played on an *m x n* grid, blocks made up of four squares will drop downwards from the grid until they either hit the bottom of the grid or hit another solid, and once this occurs, another block will spawn at the top. The player is also able to rotate the block as it falls, using the *up arrow* and *down arrow* keys, and move a block horizontally with *left arrow* and *right arrow*. If a row is completely full of solid blocks, it will be deleted, and the blocks above will fall down. The game is over when the spawned block interferes with previous placed blocks on the grid.

# Algorithm
A **tetris** is a simultaneous deletion of four consecutive rows.
