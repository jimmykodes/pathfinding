class MazeQueue:
    def __init__(self):
        self.queue = []

    def put(self, obj, distance):
        self.queue.append((obj, distance))

    def pop(self):
        self.queue = list(sorted(self.queue, key=lambda q: q[1], reverse=True))
        return self.queue.pop()
