"""Implement a queue using a linked list."""


class Node:
    """A node in a queue."""

    def __init__(self, value: object):
        """Initialize a node.

        Args:
            value (object): The value to store in the node.
        """
        self.value: object = value
        self.next: Node | None = None


class Queue:
    """A queue."""

    def __init__(self, value: object):
        """Initialize a queue.

        Args:
            value (object): The value to store in the queue.
        """
        self.first: Node | None = Node(value)
        self.last: Node | None = self.first
        self.length: int = 1

    def __len__(self) -> int:
        """Return the length of the queue."""
        return self.length

    def print_queue(self) -> None:
        """Print the queue."""
        temp = self.first
        while temp is not None:
            print(temp.value)  # noqa: T201
            temp = temp.next

    def enqueue(self, value: object) -> bool:
        """Add a node to the queue.

        Args:
            value (object): The value to store in the node.

        Returns:
            bool: True if the node was added, False otherwise.
        """
        new_node = Node(value)
        if self.length == 0 or self.first is None or self.last is None:
            self.first = new_node
            self.last = new_node
        self.last.next = new_node
        self.last = new_node
        self.length += 1
        return True

    def dequeue(self) -> Node | None:
        """Remove a node from the queue.

        Returns:
            Node | None: The node that was removed, or None if the queue is empty.
        """
        if self.length == 0 or self.first is None or self.last is None:
            return None
        temp = self.first
        self.first = self.first.next
        self.length -= 1
        if self.length == 0:
            self.last = None
        temp.next = None
        return temp
