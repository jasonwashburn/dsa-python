"""Implement a stack data structure."""


class Node:
    """Node class for stack."""

    def __init__(self, value: object):
        """Initialize the node.

        Args:
            value (_type_): The value to initialize the node with.
        """
        self.value: object = value
        self.next: Node | None = None


class Stack:
    """Stack class."""

    def __init__(self, value: object):
        """Initialize the stack.

        Args:
            value (_type_): The value to initialize the stack with.
        """
        self.top: Node | None = Node(value)
        self.height: int = 1

    def print_stack(self) -> None:
        """Print the stack to stdout."""
        current = self.top
        while current:
            print(current.value)  # noqa: T201
            current = current.next

    def push(self, value) -> None:
        """Add a node to the stack.

        Args:
            value (_type_): The value to add to the stack.
        """
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node
        self.height += 1

    def pop(self) -> Node | None:
        """Remove a node from the stack.

        Returns:
            Node | None: The node that was removed.
        """
        if temp := self.top:
            self.top = temp.next
            self.height -= 1
            return temp
        return None
