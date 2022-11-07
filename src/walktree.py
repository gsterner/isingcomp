import enum
from polymersim import Direction
from numba import deferred_type, optional
from numba.experimental import jitclass

node_type = deferred_type()

spec_node = [('north', optional(node_type)),
        ('south', optional(node_type)),
        ('east', optional(node_type)),
        ('west', optional(node_type)),
    ]

@jitclass(spec_node)
class Node(object):
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
            return self.north is not None
        if direction == Direction.SOUTH:
            return self.south is not None
        if direction == Direction.EAST:
            return self.east is not None
        if direction == Direction.WEST:
            return self.west is not None

node_type.define(Node.class_type.instance_type)
spec_tree = [('root', node_type)]

@jitclass(spec_tree)
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
