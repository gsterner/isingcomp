import enum
from polymersim import Direction

class Node():
    def __init__(self):
        self.children = {Direction.NORTH: None,
                         Direction.SOUTH: None,
                         Direction.EAST: None,
                         Direction.WEST: None}

    def add_child(self, direction):
        self.children[direction] = Node()

    def get_child(self, direction):
        return self.children[direction]

    def has_child(self, direction):
        return self.children[direction] != None

class WalkTree():
    def __init__(self):
        self.root = Node()

    def add_walk(self, walk):
        current_node = self.root
        for current_direction in walk:
            current_node.add_child(current_direction)
            current_node = current_node.get_child(current_direction)

    def has_walk(self, walk):
        current_node = self.root
        for current_direction in walk:
            if current_node.has_child(current_direction):
                current_node = current_node.get_child(current_direction)
            else:
                return False
        return True
