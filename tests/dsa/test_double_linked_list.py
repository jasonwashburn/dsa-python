"""Tests from doubly_linked_list.py."""

from io import StringIO
from unittest.mock import patch

import pytest

from dsa.doubly_linked_list import DoublyLinkedList, Node


@pytest.fixture()
def single_item_list() -> DoublyLinkedList:
    """Return a DoublyLinkedList with one node [4]."""
    return DoublyLinkedList(value=4)


@pytest.fixture()
def two_item_list() -> DoublyLinkedList:
    """Return a DoublyLinkedList with two nodes [4, 5]."""
    victim = DoublyLinkedList(value=4)
    victim.append(5)
    return victim


@pytest.fixture()
def empty_list() -> DoublyLinkedList:
    """Return an empty DoublyLinkedList [None]."""
    empty_list = DoublyLinkedList(value=4)
    empty_list.head = None
    empty_list.tail = None
    empty_list.length = 0
    return empty_list


@pytest.fixture()
def multi_item_list() -> DoublyLinkedList:
    """Return a DoublyLinkedList with five nodes [4, 5, 6, 7, 8]."""
    victim = DoublyLinkedList(value=4)
    victim.append(5)
    victim.append(6)
    victim.append(7)
    victim.append(8)
    return victim


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
def test_print_list(mock_stdout, single_item_list) -> None:
    """Test that print_list() prints the list to stdout."""
    single_item_list.print_list()
    assert mock_stdout.getvalue() == "4\n"


def test_append(single_item_list) -> None:
    """Test that append() adds a node to the end of the list."""
    victim = single_item_list
    assert victim.append(5)
    assert victim.tail.value == 5
    assert victim.head.next == victim.tail
    assert victim.tail.prev == victim.head
    assert victim.length == 2


def test_append_on_empty_list(empty_list) -> None:
    """Test that append() works on empty list."""
    victim = empty_list
    assert victim.append(5)
    assert victim.tail.value == 5
    assert victim.head == victim.tail
    assert victim.length == 1


def test_pop(two_item_list) -> None:
    """Test that pop() removes the last node in the list."""
    victim = two_item_list
    popped_node = victim.pop()
    assert popped_node.value == 5
    assert popped_node.next is None
    assert popped_node.prev is None
    assert victim.tail.value == 4
    assert victim.tail.next is None
    assert victim.length == 1


def test_pop_on_empty_list(empty_list) -> None:
    """Test that pop() returns None on empty list."""
    victim = empty_list
    assert victim.pop() is None


def test_pop_on_single_node_list(single_item_list) -> None:
    """Test that pop() returns the node and sets head and tail to None."""
    victim = single_item_list
    popped_node = victim.pop()
    assert popped_node.value == 4
    assert popped_node.next is None
    assert popped_node.prev is None
    assert victim.head is None
    assert victim.tail is None
    assert victim.length == 0


def test_prepend(single_item_list) -> None:
    """Test that prepend() adds a node to the beginning of the list."""
    victim = single_item_list
    victim.prepend(5)
    assert victim.head.value == 5
    assert victim.tail.value == 4
    assert victim.length == 2


def test_prepend_on_empty_list(empty_list) -> None:
    """Test that prepend() works on empty list."""
    victim = empty_list
    victim.prepend(4)
    assert victim.head.value == 4
    assert victim.tail.value == 4
    assert victim.length == 1


def test_pop_first(two_item_list) -> None:
    """Test that pop_first() returns the first node in the list."""
    victim = two_item_list
    assert victim.pop_first().value == 4
    assert victim.length == 1
    assert victim.head.value == 5


def test_pop_first_on_empty_list(empty_list) -> None:
    """Test that pop_first() returns None on empty list."""
    victim = empty_list
    victim.head = None
    victim.tail = None
    victim.length = 0
    assert victim.pop_first() is None


def test_pop_first_on_one_item_list(single_item_list) -> None:
    """Test pop_first() on one item list returns node and sets head and tail to None."""
    victim = single_item_list
    assert victim.pop_first().value == 4
    assert victim.length == 0
    assert victim.head is None
    assert victim.tail is None


def test_get(multi_item_list) -> None:
    """Test that get() returns the node at the given index."""
    victim = multi_item_list
    assert victim.get(0).value == 4
    assert victim.get(1).value == 5
    assert victim.get(2).value == 6
    assert victim.get(3).value == 7
    assert victim.get(4).value == 8


def test_get_on_empty_list(empty_list) -> None:
    """Test that get() returns None on empty list."""
    victim = empty_list
    assert victim.get(0) is None


@pytest.mark.parametrize("index", [-1, 5])
def test_get_on_out_of_bounds_index(multi_item_list, index) -> None:
    """Test that get() returns None on out of bounds index."""
    victim = multi_item_list
    assert victim.get(index) is None


@pytest.mark.parametrize("index", [-1, 5])
def test_set_value_on_out_of_bounds_index(multi_item_list, index) -> None:
    """Test that set_value() returns False on out of bounds index."""
    victim = multi_item_list
    assert not victim.set_value(index=index, value=9)


def test_set_value(multi_item_list) -> None:
    """Test that set_value() sets the value of the node at the given index."""
    victim = multi_item_list
    assert victim.set_value(index=3, value=9)
    assert victim.get(3).value == 9


def test_set_value_on_empty_list(empty_list) -> None:
    """Test that set_value() returns False on empty list."""
    victim = empty_list
    assert not victim.set_value(index=0, value=9)


def test_insert_on_empty_list(empty_list) -> None:
    """Test that insert() works on empty list."""
    victim = empty_list
    empty_list.insert(index=0, value=4)
    assert victim.head.value == 4
    assert victim.tail.value == 4
    assert victim.length == 1


def test_insert(two_item_list) -> None:
    """Test that insert() inserts a node at the given index."""
    victim = two_item_list
    assert victim.insert(index=1, value=9)
    assert victim.get(1).value == 9
    assert victim.get(2).value == 5
    assert victim.length == 3


@pytest.mark.parametrize("index", [-1, 6])
def test_insert_on_out_of_bounds_index(multi_item_list, index) -> None:
    """Test that insert() returns False on out of bounds index."""
    victim = multi_item_list
    assert not victim.insert(index=index, value=9)
