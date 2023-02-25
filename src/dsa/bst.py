"""Implementation of the binary search tree data structure."""

from typing import Any


class Node:
    """A node in a binary search tree."""

    def __init__(self, value: Any) -> None:
        """Initialize a node.

        Args:
            value: The value to store in the node.
        """
        self.value: Any = value
        self.right: Node | None = None
        self.left: Node | None = None


class BinarySearchTree:
    """A binary search tree."""

    def __init__(self) -> None:
        """Initialize a binary search tree."""
        self.root: Node | None = None
