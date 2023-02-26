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
    assert isinstance(victim.root, Node)
    assert victim.root.value == 4
    assert victim.root.left is None
    assert victim.root.right is None


def test_insert_on_non_empty_tree() -> None:
    """Test that a node can be inserted into a non-empty tree."""
    victim = BinarySearchTree()
    victim.insert(4)
    victim.insert(2)
    victim.insert(6)
    assert isinstance(victim.root, Node)
    assert isinstance(victim.root.left, Node)
    assert isinstance(victim.root.right, Node)
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


def test_contains_on_empty_tree() -> None:
    """Test that contains returns false on an empty tree."""
    victim = BinarySearchTree()
    assert victim.contains(4) is False


def test_contains_on_root_only() -> None:
    """Test that contains returns true on the root only."""
    victim = BinarySearchTree()
    victim.insert(4)
    assert victim.contains(4) is True


def test_contains_on_left() -> None:
    """Test that contains returns true on the left."""
    victim = BinarySearchTree()
    victim.insert(4)
    victim.insert(2)
    assert victim.contains(2) is True


def test_contains_on_right() -> None:
    """Test that contains returns true on the right."""
    victim = BinarySearchTree()
    victim.insert(4)
    victim.insert(6)
    assert victim.contains(6) is True


def test_contains_on_missing() -> None:
    """Test that contains returns false on a missing value."""
    victim = BinarySearchTree()
    victim.insert(4)
    victim.insert(6)
    assert victim.contains(5) is False


def test_contains_on_deep_left() -> None:
    """Test that contains returns true on a deep left."""
    victim = BinarySearchTree()
    victim.insert(4)
    victim.insert(2)
    victim.insert(1)
    assert victim.contains(1) is True


def test_contains_on_deep_right() -> None:
    """Test that contains returns true on a deep right."""
    victim = BinarySearchTree()
    victim.insert(4)
    victim.insert(6)
    victim.insert(7)
    assert victim.contains(7) is True
