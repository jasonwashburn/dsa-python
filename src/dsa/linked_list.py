from typing import Any


class Node:
    """A node in a linked list."""

    def __init__(self, value: Any) -> None:
        self.value = value
        self.next = None


class LinkedList:
    """A linked list."""

    def __init__(self, value: Any) -> None:
        """A linked list.

        Args:
            value (Any): The initial value in the linked list.
        """
        node = Node(value=value)
        self.head = node
        self.tail = node
        self.length = 1


def main():
    """Main function to test the LinkedList class"""
    my_linked_list = LinkedList(4)

    print("Head:", my_linked_list.head.value)
    print("Tail:", my_linked_list.tail.value)
    print("Length:", my_linked_list.length)


if __name__ == "__main__":
    main()
