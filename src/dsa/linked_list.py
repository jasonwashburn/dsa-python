"""Implements Linked List Data Structure."""
from typing import Any


class Node:
    """A node in a linked list."""

    def __init__(self, value: Any) -> None:
        """Initialize a node.

        Args:
            value (Any): The value of the node.
        """
        self.value: Any = value
        self.next: Node | None = None


class LinkedList:
    """A linked list."""

    def __init__(self, value: Any) -> None:
        """Initialize a linked list.

        Args:
            value (Any): The initial value in the linked list.
        """
        node = Node(value=value)
        self.head: Node | None = node
        self.tail: Node | None = node
        self.length: int = 1

    def print_list(self) -> None:
        """Print the linked list to stdout."""
        temp = self.head
        while temp is not None:
            print(temp.value)  # noqa: T201
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

    def pop(self) -> Node | None:
        """Remove and return the last node from the linked list.

        Returns:
            Node | None: The last node, or None if the list is empty.
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

    def pop_first(self) -> Node | None:
        """Remove and return the first node from the linked list.

        Returns:
            Node | None: The first node, or None if the list is empty.
        """
        if self.length == 0:
            return None
        temp = self.head
        new_head = self.head.next
        temp.next = None
        self.head = new_head
        self.length -= 1
        if self.length == 0:
            self.tail = None
        return temp

    def get(self, index: int) -> Node | None:
        """Get the node at the given index.

        Args:
            index (int): The index of the node to get.

        Returns:
            Node | None: The node at the given index, or None if the index
                is out of bounds.
        """
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp

    def set_value(self, index: int, value: Any) -> bool:
        """Set the value of the node at the given index.

        Args:
            index (int): The index of the node to set.
            value (Any): The new value of the node.

        Returns:
            bool: True if the value was set, False otherwise.
        """
        node = self.get(index)
        if node is None:
            return False
        node.value = value
        return True

    def insert(self, index: int, value: Any) -> bool:
        """Insert a node at the given index.

        Args:
            index (int): The index to insert the node at.
            value (Any): The value of the node to insert.

        Returns:
            bool: True if the node was inserted, False otherwise.
        """
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.prepend(value=value)
        if index == self.length:
            return self.append(value=value)
        leader = self.get(index - 1)
        new_node = Node(value=value)
        follower = leader.next
        new_node.next = follower
        leader.next = new_node
        self.length += 1
        return True


def main():
    """Run Main function."""
    ...


if __name__ == "__main__":
    main()
