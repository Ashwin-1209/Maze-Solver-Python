from MazeAlgorithm import *

maze = Maze("maze5.txt")

if maze.solve():
    maze.res_display()
else:
    print("No Solution")
