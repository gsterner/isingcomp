import enum
from polymersim import Direction

class Node():
    def __init__(self):
        self.north = None
        self.south = None
        self.east = None
        self.west = None

    def add_child(self, direction):
        if direction == Direction.NORTH:
            self.north = Node()
        if direction == Direction.SOUTH:
            self.south = Node()
        if direction == Direction.EAST:
            self.east = Node()
        if direction == Direction.WEST:
            self.west = Node()

    def get_child(self, direction):
        if direction == Direction.NORTH:
            return self.north
        if direction == Direction.SOUTH:
            return self.south
        if direction == Direction.EAST:
            return self.east
        if direction == Direction.WEST:
            return self.west

    def has_child(self, direction):
        if direction == Direction.NORTH:
            return self.north != None
        if direction == Direction.SOUTH:
            return self.south != None
        if direction == Direction.EAST:
            return self.east != None
        if direction == Direction.WEST:
            return self.west != None

# test_walk = [Direction.NORTH, Direction.WEST]

# tree_root = Node()
# current_node = tree_root
# for current_direction in test_walk:
#     current_node.add_child(current_direction)
#     current_node = current_node.get_child(current_direction)
