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

# test_walk = [Direction.NORTH, Direction.WEST]

# tree_root = Node()
# current_node = tree_root
# for current_direction in test_walk:
#     current_node.add_child(current_direction)
#     current_node = current_node.get_child(current_direction)
