import sys
sys.path.append('../src')
import walktree

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
