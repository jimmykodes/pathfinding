class Node:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.top_node = None
        self.bottom_node = None
        self.left_node = None
        self.right_node = None

    def __str__(self):
        return f"Node at ({self.x}, {self.y})"

    def __repr__(self):
        return self.__str__()
