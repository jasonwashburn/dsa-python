"""Implement a queue using a linked list."""

from typing import Any


class Node:
    """A node in a queue."""

    def __init__(self, value: Any):
        """Initialize a node.

        Args:
            value (Any): The value to store in the node.
        """
        self.value = value
        self.next = None


class Queue:
    """A queue."""

    def __init__(self, value: Any):
        """Initialize a queue.

        Args:
            value (Any): The value to store in the queue.
        """
        self.first = Node(value)
        self.last = self.first
        self.length = 1

    def __len__(self) -> int:
        """Return the length of the queue."""
        return self.length

    def print_queue(self) -> None:
        """Print the queue."""
        temp = self.first
        while temp is not None:
            print(temp.value)  # noqa: T201
            temp = temp.next
