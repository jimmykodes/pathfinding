import time

from maze_queue import MazeQueue


def dijkstra(maze):
    neighbors = [
        'left_node',
        'right_node',
        'top_node',
        'bottom_node',
    ]

    queue = MazeQueue()
    print(f'Starting maze traversal at {maze.start}')
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
    end = time.time()
    print('Finished')
    print(f'Number of nodes completed: {len(finished)}')
    print(f'Number of cycles: {steps}')
    return last, end
