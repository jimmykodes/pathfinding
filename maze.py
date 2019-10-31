from node import Node


class Maze:
    def __init__(self, maze_data):
        self.maze_data = maze_data
        self.start = None
        self.end = None
        self.height = maze_data.shape[0]
        self.width = maze_data.shape[1]

        left_node = None
        top_nodes = [None] * self.width

        for i, row in enumerate(self.maze_data):
            for j, col in enumerate(row):
                if col == 0:
                    left_node = None
                    top_nodes[j] = None
                    continue

                neighbors = {
                    'left': self.is_walkable(i, j - 1),
                    'right': self.is_walkable(i, j + 1),
                    'top': self.is_walkable(i - 1, j),
                    'bottom': self.is_walkable(i + 1, j)
                }
                if neighbors['left'] and neighbors['right'] and not neighbors['top'] and not neighbors['bottom']:
                    continue
                elif neighbors['top'] and neighbors['bottom'] and not neighbors['right'] and not neighbors['left']:
                    continue
                else:
                    n = Node(j, i)
                    if i == 0:
                        self.start = n
                        n.distance = 0
                    elif i == self.height - 1:
                        # in the bottom row
                        self.end = n
                        n.is_end = True
                    if left_node is not None:
                        left_node.right_node = n
                        n.left_node = left_node
                        left_node = n
                    if top_nodes[j] is not None:
                        top_nodes[j].bottom_node = n
                        n.top_node = top_nodes[j]
                    if neighbors['bottom']:
                        top_nodes[j] = n
                    if neighbors['right']:
                        left_node = n

    def is_walkable(self, r, c):
        try:
            return bool(self.maze_data[r][c])
        except IndexError:
            return False
