"""Implements Linked List Data Structure."""
from typing import Any, Optional


class Node:
    """A node in a linked list."""

    def __init__(self, value: Any) -> None:
        """Initialize a node.

        Args:
            value (Any): The value of the node.
        """
        self.value: Any = value
        self.next: Optional[Node] = None


class LinkedList:
    """A linked list."""

    def __init__(self, value: Any) -> None:
        """Initialize a linked list.

        Args:
            value (Any): The initial value in the linked list.
        """
        node = Node(value=value)
        self.head: Optional[Node] = node
        self.tail: Optional[Node] = node
        self.length: int = 1

    def print_list(self) -> None:
        """Print the linked list to stdout."""
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def append(self, value: Any) -> bool:
        """Append a value to the end of the linked list.

        Args:
            value (Any): The value to append.

        Returns:
            bool: True if the value was appended, False otherwise.
        """
        new_node = Node(value=value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True

    def pop(self) -> Optional[Node]:
        """Remove and return the last node from the linked list.

        Returns:
            Optional[Node]: The last node, or None if the list is empty.
        """
        temp = self.head
        pre = self.head
        if self.length == 0:
            return None
        while temp.next:
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp

    def prepend(self, value: Any) -> bool:
        """Prepend a value to the beginning of the linked list.

        Args:
            value (Any): The value to prepend.

        Returns:
            bool: True if the value was prepended, False otherwise.
        """
        new_node = Node(value=value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node

        self.length += 1
        return True


def main():
    """Test the LinkedList class."""
    my_linked_list = LinkedList(1)
    my_linked_list.append(2)

    print(my_linked_list.pop())
    print(my_linked_list.pop())
    print(my_linked_list.pop())


if __name__ == "__main__":
    main()
