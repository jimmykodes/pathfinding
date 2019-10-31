from PIL import Image
import numpy as np

from maze import Maze
from maze_queue import MazeQueue

img = Image.open('mazes/small.png')
width = img.size[0]
height = img.size[1]
maze_data = np.reshape(img.getdata(0), (width, height))

maze = Maze(maze_data)

neighbors = [
    'left_node',
    'right_node',
    'top_node',
    'bottom_node',
]

queue = MazeQueue()
queue.put(maze.start)
last = queue.pop()
finished = []
steps = 0
while not last.is_end:
    steps += 1
    for neighbor in neighbors:
        n = getattr(last, neighbor)
        if n is not None and n not in finished:
            n.distance = max((abs(n.x - last.x), abs(n.y - last.y))) + last.distance
            queue.put(n)
    finished.append(last)
    last = queue.pop()
print('Finished')
print(f'Total distance: {last.distance}')
print(f'Number of cycles: {steps}')
