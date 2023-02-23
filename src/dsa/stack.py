"""Implement a stack data structure."""


from typing import Any


class Node:
    """Node class for stack."""

    def __init__(self, value: Any):
        """Initialize the node.

        Args:
            value (_type_): The value to initialize the node with.
        """
        self.value: Any = value
        self.next: Node | None = None


class Stack:
    """Stack class."""

    def __init__(self, value: Any):
        """Initialize the stack.

        Args:
            value (_type_): The value to initialize the stack with.
        """
        self.top: Node | None = Node(value)
        self.height: int = 1

    def print_stack(self):
        """Print the stack to stdout."""
        current = self.top
        while current:
            print(current.value)  # noqa: T201
            current = current.next

    def push(self, value):
        """Add a node to the stack.

        Args:
            value (_type_): The value to add to the stack.
        """
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node
        self.height += 1
