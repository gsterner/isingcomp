import sys
sys.path.append('../src')
import walktree
from polymersim import Direction

def test_node_add():
    tree_node = walktree.Node()
    tree_node.add_child(walktree.Direction.NORTH)
    assert tree_node.has_child(walktree.Direction.NORTH) == True
    assert tree_node.has_child(walktree.Direction.EAST) == False
    assert tree_node.has_child(walktree.Direction.WEST) == False
    assert tree_node.has_child(walktree.Direction.SOUTH) == False

def test_node_get():
    tree_node = walktree.Node()
    tree_node.add_child(walktree.Direction.NORTH)
    north_child = tree_node.get_child(walktree.Direction.NORTH)
    south_child = tree_node.get_child(walktree.Direction.SOUTH)
    east_child = tree_node.get_child(walktree.Direction.EAST)
    west_child = tree_node.get_child(walktree.Direction.WEST)
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
