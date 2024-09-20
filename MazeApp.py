import sys
from MazeAlgorithm import *

maze = Maze(sys.argv[1])

if maze.solve():
    maze.res_display()
else:
    print("No Solution")
