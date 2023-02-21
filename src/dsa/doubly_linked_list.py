"""Implements a doubly linked list."""

from typing import Any


class Node:
    """Node class for doubly linked list."""

    def __init__(self, value: Any) -> None:
        """Initialize a new node.

        Args:
            value (Any): The value of the node.
        """
        self.value: Any = value
        self.next: Node | None = None
        self.prev: Node | None = None


class DoublyLinkedList:
    """Doubly linked list class."""

    def __init__(self, value: Any) -> None:
        """Initialize a new doubly linked list.

        Args:
            value (Any): The value of the head node.
        """
        new_node = Node(value)
        self.head: Node | None = new_node
        self.tail: Node | None = new_node
        self.length: int = 1

    def print_list(self) -> None:
        """Print the list to stdout."""
        temp = self.head
        while temp is not None:
            print(temp.value)  # noqa: T201
            temp = temp.next

    def append(self, value: Any) -> bool:
        """Append a node to the end of the list.

        Args:
            value (Any): The value of the node to append.
        """
        new_node = Node(value)
        if self.length == 0 or self.head is None or self.tail is None:
            self.head = new_node
            self.tail = new_node
            self.length += 1
            return True
        new_node.prev = self.tail
        self.tail.next = new_node
        self.tail = new_node
        self.length += 1
        return True

    def pop(self) -> Node | None:
        """Remove the last node in the list.

        Returns:
            Node | None: The last node in the list.
        """
        if self.length == 0 or self.head is None or self.tail is None:
            return None

        temp = self.tail
        if self.length == 1 or self.tail.prev is None:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
            temp.prev = None
        self.length -= 1
        return temp

    def prepend(self, value: Any) -> bool:
        """Prepend a node to the beginning of the list.

        Args:
            value (Any): The value of the node to prepend.

        Returns:
            bool: True if successful, False otherwise.
        """
        new_node = Node(value)
        new_node.next = self.head
        if self.length == 0:
            self.tail = new_node
        self.head = new_node
        self.length += 1
        return True

    def pop_first(self) -> Node | None:
        """Remove the first node in the list and return it.

        Returns:
            Node | None: The first node in the list.
        """
        if self.length == 0 or self.head is None:
            return None
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -= 1
        if self.length == 0:
            self.tail = None
        return temp
