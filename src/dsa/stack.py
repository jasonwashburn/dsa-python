"""Implement a stack data structure."""


class Node:
    """Node class for stack."""

    def __init__(self, value):
        """Initialize the node.

        Args:
            value (_type_): The value to initialize the node with.
        """
        self.value = value
        self.next = None


class Stack:
    """Stack class."""

    def __init__(self, value):
        """Initialize the stack.

        Args:
            value (_type_): The value to initialize the stack with.
        """
        self.top = Node(value)
        self.height = 1

    def print_stack(self):
        """Print the stack to stdout."""
        current = self.top
        while current:
            print(current.value)  # noqa: T201
            current = current.next
