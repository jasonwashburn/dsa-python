"""Test the linked_list module."""
from io import StringIO
from unittest.mock import patch

import pytest

from dsa.linked_list import LinkedList, Node


@pytest.fixture()
def empty_list() -> LinkedList:
    """Return an empty LinkedList."""
    empty_list = LinkedList(value=4)
    empty_list.head = None
    empty_list.tail = None
    empty_list.length = 0
    return empty_list


@pytest.fixture()
def single_node_list() -> LinkedList:
    """Return a LinkedList with one node."""
    return LinkedList(value=4)


@pytest.fixture()
def multi_node_list() -> LinkedList:
    """Return a LinkedList with multiple nodes."""
    victim = LinkedList(value=4)
    victim.append(value=5)
    victim.append(value=6)
    return victim


def test_node_builds() -> None:
    """Test that a Node can be instantiated."""
    node = Node(value=4)
    assert node.value == 4
    assert node.next is None


def test_linked_list_builds() -> None:
    """Test that a LinkedList can be instantiated."""
    victim = LinkedList(value=4)
    assert isinstance(victim.head, Node)
    assert isinstance(victim.tail, Node)
    assert victim.head is victim.tail
    assert victim.head.value == 4
    assert victim.tail.value == 4


@patch("sys.stdout", new_callable=StringIO)
def test_print_list(mock_stdout, multi_node_list) -> None:
    """Test that print_list() prints the list to stdout."""
    victim = multi_node_list
    victim.print_list()
    assert mock_stdout.getvalue() == "4\n5\n6\n"


def test_append(single_node_list) -> None:
    """Test that append() adds value to the end of the list."""
    victim = single_node_list
    victim.append(value=5)
    assert victim.tail.value == 5
    assert victim.head.next.value == 5
    assert victim.length == 2


def test_append_to_empty_list(empty_list) -> None:
    """Test that append() properly adds value if the list is empty."""
    victim = empty_list
    victim.append(value=5)
    assert victim.head.value == 5
    assert victim.tail.value == 5
    assert victim.length == 1


def test_pop_removes_last_node(multi_node_list) -> None:
    """Test that pop() removes and returns the last node from the list."""
    victim = multi_node_list
    assert victim.pop().value == 6
    assert victim.tail.value == 5
    assert victim.length == 2
    assert victim.tail.next is None


def test_pop_on_empty_list_returns_none(empty_list) -> None:
    """Test that pop() returns None if the list is empty."""
    victim = empty_list
    victim.head = None
    victim.tail = None
    victim.length = 0
    assert victim.pop() is None


def test_pop_on_list_with_one_node(single_node_list) -> None:
    """Test that pop() works on a list with one node."""
    victim = single_node_list
    assert victim.pop().value == 4
    assert victim.head is None
    assert victim.tail is None
    assert victim.length == 0


def test_prepend_adds_node_to_front_of_list(single_node_list) -> None:
    """Test that prepend() adds a node to the front of the list."""
    victim = single_node_list
    victim.prepend(value=3)
    assert victim.head.value == 3
    assert victim.tail.value == 4
    assert victim.length == 2


def test_prepend_on_empty_list(empty_list) -> None:
    """Test that prepend() works on an empty list."""
    victim = empty_list
    victim.prepend(value=3)
    assert victim.head.value == 3
    assert victim.tail.value == 3
    assert victim.length == 1


def test_pop_first_node(multi_node_list) -> None:
    """Test that pop() removes and returns the first node from the list."""
    victim = multi_node_list
    assert victim.pop_first().value == 4
    assert victim.head.value == 5
    assert victim.length == 2


def test_pop_first_on_empty_list_returns_none(empty_list) -> None:
    """Test that pop_first() returns None if the list is empty."""
    victim = empty_list
    assert victim.pop_first() is None


def test_pop_first_on_list_with_one_node(single_node_list) -> None:
    """Test that pop_first() works on a list with one node."""
    victim = single_node_list
    assert victim.pop_first().value == 4
    assert victim.head is None
    assert victim.tail is None
    assert victim.length == 0


def test_pop_first_returned_node_is_not_linked_to_other_nodes(multi_node_list) -> None:
    """Test that pop_first() returns a node that is not linked to other nodes."""
    victim = multi_node_list
    assert victim.pop_first().next is None


def test_get_node_at_index(multi_node_list) -> None:
    """Test that get() returns the node at the given index."""
    victim = multi_node_list
    assert victim.get(0).value == 4
    assert victim.get(1).value == 5
    assert victim.get(2).value == 6


def test_get_on_empty_list_returns_none(empty_list) -> None:
    """Test that get() returns None if the list is empty."""
    victim = empty_list
    assert victim.get(0) is None


def test_set_value_sets_value_of_node_at_index(multi_node_list) -> None:
    """Test that set_value() sets the value of the node at the given index."""
    victim = multi_node_list
    victim.set_value(1, 7)
    assert victim.get(0).value == 4
    assert victim.get(1).value == 7
    assert victim.get(2).value == 6


def test_set_value_on_empty_list_returns_none(empty_list) -> None:
    """Test that set_value() returns None if the list is empty."""
    victim = empty_list
    assert victim.set_value(0, 7) is False


def test_insert(multi_node_list) -> None:
    """Test that insert() inserts a node at the given index."""
    victim = multi_node_list
    victim.insert(1, 7)
    assert victim.get(0).value == 4
    assert victim.get(1).value == 7
    assert victim.get(2).value == 5
    assert victim.get(3).value == 6
    assert victim.length == 4


def test_insert_on_empty_list(empty_list) -> None:
    """Test that insert() works on an empty list."""
    victim = empty_list
    victim.insert(0, 7)
    assert victim.get(0).value == 7
    assert victim.length == 1


@pytest.mark.parametrize("index", [-1, 3])
def test_insert_on_invalid_index_returns_false(single_node_list, index: int) -> None:
    """Test that insert() returns False if the index is invalid."""
    victim = single_node_list
    assert victim.insert(index, 7) is False


def test_remove(multi_node_list) -> None:
    """Test that remove() removes and returns the node at the given index."""
    victim = multi_node_list
    assert victim.remove(1).value == 5
    assert victim.get(0).value == 4
    assert victim.get(1).value == 6
    assert victim.length == 2


def test_remove_first_item(multi_node_list) -> None:
    """Test that remove() removes and returns the first item in the list."""
    victim = multi_node_list
    assert victim.remove(0).value == 4
    assert victim.get(0).value == 5
    assert victim.get(1).value == 6
    assert victim.length == 2


def test_remove_last_item(multi_node_list) -> None:
    """Test that remove() removes and returns the last item in the list."""
    victim = multi_node_list
    assert victim.remove(2).value == 6
    assert victim.get(0).value == 4
    assert victim.get(1).value == 5
    assert victim.length == 2


def test_remove_on_empty_list_returns_false(empty_list) -> None:
    """Test that remove() returns False if the list is empty."""
    victim = empty_list
    assert victim.remove(0) is False


def test_reverse(multi_node_list) -> None:
    """Test that reverse() reverses the list."""
    victim = multi_node_list
    victim.reverse()
    assert victim.get(0).value == 6
    assert victim.get(1).value == 5
    assert victim.get(2).value == 4


def test_reverse_empty_list(empty_list) -> None:
    """Test that reverse() works on an empty list."""
    victim = empty_list
    victim.reverse()
    assert victim.head is None
    assert victim.tail is None
    assert victim.length == 0


def test_reverse_one_item_list(single_node_list) -> None:
    """Test that reverse() works on a list with one item."""
    victim = single_node_list
    victim.reverse()
    assert victim.get(0).value == 4
    assert victim.length == 1


def test_linked_list_handles_len_for_empty_list(empty_list) -> None:
    """Test that len() works on an empty list."""
    victim = empty_list
    assert len(victim) == 0


def test_linked_list_haneles_len_for_one_item_list(single_node_list) -> None:
    """Test that len() works on a list with one item."""
    victim = single_node_list
    assert len(victim) == 1


def test_linked_list_handles_len(multi_node_list) -> None:
    """Test that len() works on a list with multiple items."""
    victim = multi_node_list
    assert len(victim) == 3
