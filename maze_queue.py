class QueueException(Exception):
    pass


class MazeQueue:
    def __init__(self):
        self.queue = {}

    def put(self, node):
        try:
            old = self.queue[f'{node.x}|{node.y}']
            if node.distance < old.distance:
                self.queue[f'{node.x}|{node.y}'] = node
        except KeyError:
            self.queue[f'{node.x}|{node.y}'] = node

    def pop(self):
        if self.empty():
            raise QueueException('Queue is empty')
        shortest = min(self.queue.values(), key=lambda n: n.distance)
        return self.queue.pop(f'{shortest.x}|{shortest.y}')

    def empty(self):
        return not bool(self.queue)
