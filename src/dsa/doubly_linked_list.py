"""Implements a doubly linked list."""

from typing import Any


class Node:
    """Node class for doubly linked list."""

    def __init__(self, value: Any) -> None:
        """Initialize a new node.

        Args:
            value (Any): The value of the node.
        """
        self.value = value
        self.next = None
        self.prev = None


class DoublyLinkedList:
    """Doubly linked list class."""

    def __init__(self, value: Any) -> None:
        """Initialize a new doubly linked list.

        Args:
            value (Any): The value of the head node.
        """
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self) -> None:
        """Print the list to stdout."""
        temp = self.head
        while temp is not None:
            print(temp.value)  # noqa: T201
            temp = temp.next
