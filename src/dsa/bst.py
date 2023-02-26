"""Implementation of the binary search tree data structure."""


class Node:
    """A node in a binary search tree."""

    def __init__(self, value: int | float) -> None:
        """Initialize a node.

        Args:
            value: The value to store in the node.
        """
        self.value: int | float = value
        self.right: Node | None = None
        self.left: Node | None = None


class BinarySearchTree:
    """A binary search tree."""

    def __init__(self) -> None:
        """Initialize a binary search tree."""
        self.root: Node | None = None

    def insert(self, value: int | float) -> bool:
        """Insert a value into the binary search tree.

        Args:
            value (object): The value to insert.

        Returns:
            bool: True if the value was inserted, False if the value was
            already present.
        """
        if self.root is None:
            self.root = Node(value)
            return True
        temp = self.root
        while True:
            if value == temp.value:
                return False
            if value < temp.value:
                if temp.left is None:
                    temp.left = Node(value)
                    return True
                temp = temp.left
            elif value > temp.value:
                if temp.right is None:
                    temp.right = Node(value)
                    return True
                temp = temp.right
