"""Tests from doubly_linked_list.py."""

from io import StringIO
from unittest.mock import patch

from dsa.doubly_linked_list import DoublyLinkedList, Node


def test_node() -> None:
    """Test Node class."""
    victim = Node(value=4)
    assert victim.value == 4
    assert victim.next is None
    assert victim.prev is None


def test_doubly_linked_list() -> None:
    """Test DoublyLinkedList class."""
    victim = DoublyLinkedList(value=4)
    assert victim.head.value == 4
    assert victim.head.next is None
    assert victim.head.prev is None
    assert victim.head == victim.tail
    assert victim.length == 1


@patch("sys.stdout", new_callable=StringIO)
def test_print_list(mock_stdout) -> None:
    """Test that print_list() prints the list to stdout."""
    victim = DoublyLinkedList(value=4)
    victim.print_list()
    assert mock_stdout.getvalue() == "4\n"
