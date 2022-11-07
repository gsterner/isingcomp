import sys
sys.path.append('../src')
import walktree
from polymersim import Direction

def test_node_add():
    tree_node = walktree.Node()
    tree_node.add_child(Direction.NORTH)
    assert tree_node.has_child(Direction.NORTH) == True
    assert tree_node.has_child(Direction.EAST) == False
    assert tree_node.has_child(Direction.WEST) == False
    assert tree_node.has_child(Direction.SOUTH) == False

def test_node_get():
    tree_node = walktree.Node()
    tree_node.add_child(Direction.NORTH)
    north_child = tree_node.get_child(Direction.NORTH)
    south_child = tree_node.get_child(Direction.SOUTH)
    east_child = tree_node.get_child(Direction.EAST)
    west_child = tree_node.get_child(Direction.WEST)
    assert north_child != None
    assert south_child == None
    assert east_child == None
    assert west_child == None

def test_tree_add():
    tree = walktree.WalkTree()
    test_walk = [Direction.NORTH, Direction.WEST]
    tree.add_walk(test_walk)
    north_child = tree.root.get_child(Direction.NORTH)
    south_child = tree.root.get_child(Direction.SOUTH)
    east_child = tree.root.get_child(Direction.EAST)
    west_child = tree.root.get_child(Direction.WEST)
    assert north_child != None
    assert south_child == None
    assert east_child == None
    assert west_child == None
    north_north_child = north_child.get_child(Direction.NORTH)
    north_south_child = north_child.get_child(Direction.SOUTH)
    north_east_child = north_child.get_child(Direction.EAST)
    north_west_child = north_child.get_child(Direction.WEST)
    assert north_north_child == None
    assert north_south_child == None
    assert north_east_child == None
    assert north_west_child != None

def test_tree_has():
    tree = walktree.WalkTree()
    add_walk = [Direction.NORTH, Direction.WEST]
    tree.add_walk(add_walk)
    test_walk_one = [Direction.SOUTH, Direction.WEST]
    test_walk_two = [Direction.NORTH, Direction.EAST]
    assert tree.has_walk(add_walk) == True
    assert tree.has_walk(test_walk_one) == False
    assert tree.has_walk(test_walk_two) == False

def test_tree_has_long():
    tree = walktree.WalkTree()
    add_walk = [Direction.NORTH, Direction.WEST, Direction.NORTH, Direction.WEST, Direction.SOUTH]
    tree.add_walk(add_walk)
    test_walk_one = [Direction.NORTH, Direction.WEST, Direction.NORTH, Direction.SOUTH, Direction.SOUTH]
    assert tree.has_walk(add_walk) == True
    assert tree.has_walk(test_walk_one) == False
