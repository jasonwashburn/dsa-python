"""Implements Linked List Data Structure."""
from typing import Any


class Node:
    """A node in a linked list."""

    def __init__(self, value: Any) -> None:
        """Initialize a node.

        Args:
            value (Any): The value of the node.
        """
        self.value = value
        self.next = None


class LinkedList:
    """A linked list."""

    def __init__(self, value: Any) -> None:
        """Initialize a linked list.

        Args:
            value (Any): The initial value in the linked list.
        """
        node = Node(value=value)
        self.head = node
        self.tail = node
        self.length = 1

    def print_list(self) -> None:
        """Print the linked list to stdout."""
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next


def main():
    """Test the LinkedList class."""
    my_linked_list = LinkedList(4)

    print("Head:", my_linked_list.head.value)
    print("Tail:", my_linked_list.tail.value)
    print("Length:", my_linked_list.length)

    my_linked_list.print_list()


if __name__ == "__main__":
    main()
