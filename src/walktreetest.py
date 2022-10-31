import enum

class Direction(enum.Enum):
    NORTH = enum.auto()
    SOUTH = enum.auto()
    EAST = enum.auto()
    WEST = enum.auto()

class Node():
    def __init__(self):
        self.north = None
        self.south = None
        self.east = None
        self.west = None

    def set_direction(self, direction):
        if direction == Direction.NORTH:
            self.north = Node()
        if direction == Direction.SOUTH:
            self.south = Node()
        if direction == Direction.EAST:
            self.east = Node()
        if direction == Direction.WEST:
            self.west = Node()

test_walk = [Direction.NORTH, Direction.WEST]
test_root = Node()
test_root.set_direction(Direction.NORTH)

print(test_root)
print(test_root.north)
print(test_root.south)
