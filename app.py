from io import BytesIO

import cairo
from PIL import Image
import numpy as np

from maze import Maze
from maze_queue import MazeQueue

image_path = 'mazes/normal.png'
img = Image.open(image_path).convert('RGB')
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
            n.via = last
            n.distance = max((abs(n.x - last.x), abs(n.y - last.y))) + last.distance
            queue.put(n)
    finished.append(last)
    last = queue.pop()
print('Finished')
print(f'Total distance: {last.distance}')
print(f'Number of cycles: {steps}')
green = np.array(img)
while last is not None:
    prev = last.via
    x = last.x
    y = last.y
    if prev:
        while x != prev.x or y != prev.y:
            green[y][x] = [0, 255, 0]
            if x != prev.x:
                x += 1 if x < prev.x else -1
            if y != prev.y:
                y += 1 if y < prev.y else -1
    last = prev

# color the start
green[maze.start.y][maze.start.x] = [0, 255, 0]

i = Image.fromarray(green)
with open('solved.png', 'wb') as f:
    i.save(f, format='png')
