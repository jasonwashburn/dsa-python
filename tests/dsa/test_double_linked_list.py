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


def test_append() -> None:
    """Test that append() adds a node to the end of the list."""
    victim = DoublyLinkedList(value=4)
    assert victim.append(5)
    assert victim.tail.value == 5
    assert victim.head.next == victim.tail
    assert victim.tail.prev == victim.head
    assert victim.length == 2


def test_append_on_empty_list() -> None:
    """Test that append() works on empty list."""
    victim = DoublyLinkedList(value=4)
    victim.head = None
    victim.tail = None
    victim.length = 0
    assert victim.append(5)
    assert victim.tail.value == 5
    assert victim.head == victim.tail
    assert victim.length == 1


def test_pop() -> None:
    """Test that pop() removes the last node in the list."""
    victim = DoublyLinkedList(value=4)
    victim.append(5)
    popped_node = victim.pop()
    assert popped_node.value == 5
    assert popped_node.next is None
    assert popped_node.prev is None
    assert victim.tail.value == 4
    assert victim.tail.next is None
    assert victim.length == 1


def test_pop_on_empty_list() -> None:
    """Test that pop() returns None on empty list."""
    victim = DoublyLinkedList(value=4)
    victim.head = None
    victim.tail = None
    victim.length = 0
    assert victim.pop() is None


def test_pop_on_single_node_list() -> None:
    """Test that pop() returns the node and sets head and tail to None."""
    victim = DoublyLinkedList(value=4)
    popped_node = victim.pop()
    assert popped_node.value == 4
    assert popped_node.next is None
    assert popped_node.prev is None
    assert victim.head is None
    assert victim.tail is None
    assert victim.length == 0


def test_prepend() -> None:
    """Test that prepend() adds a node to the beginning of the list."""
    victim = DoublyLinkedList(value=4)
    victim.prepend(5)
    assert victim.head.value == 5
    assert victim.tail.value == 4
    assert victim.length == 2


def test_prepend_on_empty_list() -> None:
    """Test that prepend() works on empty list."""
    victim = DoublyLinkedList(value=4)
    victim.head = None
    victim.tail = None
    victim.length = 0
    victim.prepend(4)
    assert victim.head.value == 4
    assert victim.tail.value == 4
    assert victim.length == 1


def test_pop_first() -> None:
    """Test that pop_first() returns the first node in the list."""
    victim = DoublyLinkedList(value=4)
    victim.append(5)
    assert victim.pop_first().value == 4
    assert victim.length == 1
    assert victim.head.value == 5


def test_pop_first_on_empty_list() -> None:
    """Test that pop_first() returns None on empty list."""
    victim = DoublyLinkedList(value=4)
    victim.head = None
    victim.tail = None
    victim.length = 0
    assert victim.pop_first() is None


def test_pop_first_on_one_item_list() -> None:
    """Test pop_first() on one item list returns node and sets head and tail to None."""
    victim = DoublyLinkedList(value=4)
    assert victim.pop_first().value == 4
    assert victim.length == 0
    assert victim.head is None
    assert victim.tail is None
