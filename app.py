import argparse
import os
import time

import numpy as np
from PIL import Image

from maze import Maze
from methods.astar import astar
from methods.dijkstra import dijkstra


def main():
    funcs = {
        'astar': astar,
        'dijkstra': dijkstra,
    }
    parser = argparse.ArgumentParser()
    parser.add_argument('-m', '--method', default='astar', choices=funcs.keys())
    parser.add_argument("-i", "--input_file", default="mazes/normal.png")
    parser.add_argument("-o", "--output_file", default="solved.png")
    args = parser.parse_args()

    image_path = args.input_file
    print(f'Loading maze image: {os.path.basename(args.input_file)}')
    img = Image.open(image_path).convert('RGB')
    width = img.size[0]
    height = img.size[1]
    print(f'Image size: {width} by {height}')
    maze_data = np.reshape(img.getdata(0), (width, height))

    print('Initializing Maze')
    start = time.time()
    maze = Maze(maze_data)
    print(f'Maze initialized in {time.time() - start:.3f} seconds')
    print(f'Number of Maze Nodes: {maze.node_count}')
    print(f'Number of walkable tiles: {maze.walkable_tile_count}')
    print(f'Using method: {args.method}')
    last, end = funcs[args.method](maze)
    print(f'Total elapsed time: {end - start:.3f} seconds')
    green = np.array(img)
    tiles_walked = 0
    while last is not None:
        prev = last.via
        x = last.x
        y = last.y
        if prev:
            while x != prev.x or y != prev.y:
                green[y][x] = [0, 255, 0]
                tiles_walked += 1
                if x != prev.x:
                    x += 1 if x < prev.x else -1
                if y != prev.y:
                    y += 1 if y < prev.y else -1
        last = prev
    print(f'Tiles walked: {tiles_walked}')
    # color the start
    green[maze.start.y][maze.start.x] = [0, 255, 0]

    i = Image.fromarray(green)
    with open(args.output_file, 'wb') as f:
        i.save(f, format='png')


if __name__ == '__main__':
    main()