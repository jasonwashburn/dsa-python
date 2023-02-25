"""Test module for bst.py."""

from dsa.bst import BinarySearchTree, Node


def test_node_builds() -> None:
    """Test that a node can be built."""
    victim = Node(value=4)
    assert victim.value == 4
    assert victim.left is None
    assert victim.right is None


def test_binary_search_tree_builds() -> None:
    """Test that a binary search tree can be built."""
    victim = BinarySearchTree()
    assert victim.root is None
