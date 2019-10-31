from PIL import Image
import numpy as np

from maze import Maze

img = Image.open('mazes/small.png')
width = img.size[0]
height = img.size[1]
maze_data = np.reshape(img.getdata(0), (width, height))

maze = Maze(maze_data)
