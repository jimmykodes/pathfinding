class MazeQueue:
    def __init__(self):
        self.queue = []

    def put(self, node):
        self.queue.append(node)

    def pop(self):
        self.queue = list(sorted(self.queue, key=lambda node: node.distance, reverse=True))
        return self.queue.pop()
