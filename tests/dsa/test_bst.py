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


def test_insert_on_empty_tree() -> None:
    """Test that a node can be inserted into an empty tree."""
    victim = BinarySearchTree()
    victim.insert(4)
    assert victim.root.value == 4
    assert victim.root.left is None
    assert victim.root.right is None


def test_insert_on_non_empty_tree() -> None:
    """Test that a node can be inserted into a non-empty tree."""
    victim = BinarySearchTree()
    victim.insert(4)
    victim.insert(2)
    victim.insert(6)
    assert victim.root.value == 4
    assert victim.root.left.value == 2
    assert victim.root.right.value == 6


def test_insert_on_node_present() -> None:
    """Test that a node can be inserted into a non-empty tree."""
    victim = BinarySearchTree()
    victim.insert(4)
    victim.insert(2)
    victim.insert(6)
    assert victim.insert(4) is False


def test_insert_left() -> None:
    """Test that nodes can be inserted to the left."""
    victim = BinarySearchTree()
    assert victim.insert(4)
    assert victim.insert(3)
    assert victim.insert(2)


def test_insert_right() -> None:
    """Test that nodes can be inserted to the right."""
    victim = BinarySearchTree()
    assert victim.insert(4)
    assert victim.insert(5)
    assert victim.insert(6)
