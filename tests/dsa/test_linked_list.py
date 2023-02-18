"""Test the linked_list module."""
from io import StringIO
from unittest.mock import patch

from dsa.linked_list import LinkedList, Node


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
def test_print_list(mock_stdout) -> None:
    """Test that print_list() prints the list to stdout."""
    victim = LinkedList(value=4)
    victim.print_list()
    assert mock_stdout.getvalue() == "4\n"


def test_append() -> None:
    """Test that append() adds value to the end of the list."""
    victim = LinkedList(value=4)
    victim.append(value=5)
    assert victim.tail.value == 5
    assert victim.head.next.value == 5
    assert victim.length == 2


def test_append_to_empty_list() -> None:
    """Test that append() properly adds value if the list is empty."""
    victim = LinkedList(value=4)
    victim.head = None
    victim.tail = None
    victim.length = 0
    victim.append(value=5)
    assert victim.head.value == 5
    assert victim.tail.value == 5
    assert victim.length == 1


def test_pop_removes_last_node() -> None:
    """Test that pop() removes and returns the last node from the list."""
    victim = LinkedList(value=4)
    victim.append(value=5)
    victim.append(value=6)
    assert victim.pop().value == 6
    assert victim.tail.value == 5
    assert victim.length == 2
    assert victim.tail.next is None


def test_pop_on_empty_list_returns_none() -> None:
    """Test that pop() returns None if the list is empty."""
    victim = LinkedList(value=4)
    victim.head = None
    victim.tail = None
    victim.length = 0
    assert victim.pop() is None


def test_pop_on_list_with_one_node() -> None:
    """Test that pop() works on a list with one node."""
    victim = LinkedList(value=4)
    assert victim.pop().value == 4
    assert victim.head is None
    assert victim.tail is None
    assert victim.length == 0


def test_prepend_adds_node_to_front_of_list() -> None:
    """Test that prepend() adds a node to the front of the list."""
    victim = LinkedList(value=4)
    victim.prepend(value=3)
    assert victim.head.value == 3
    assert victim.tail.value == 4
    assert victim.length == 2


def test_prepend_on_empty_list() -> None:
    """Test that prepend() works on an empty list."""
    victim = LinkedList(value=4)
    victim.head = None
    victim.tail = None
    victim.length = 0
    victim.prepend(value=3)
    assert victim.head.value == 3
    assert victim.tail.value == 3
    assert victim.length == 1


def test_pop_first_node() -> None:
    """Test that pop() removes and returns the first node from the list."""
    victim = LinkedList(value=4)
    victim.append(value=5)
    victim.append(value=6)
    assert victim.pop_first().value == 4
    assert victim.head.value == 5
    assert victim.length == 2


def test_pop_first_on_empty_list_returns_none() -> None:
    """Test that pop_first() returns None if the list is empty."""
    victim = LinkedList(value=4)
    victim.head = None
    victim.tail = None
    victim.length = 0
    assert victim.pop_first() is None


def test_pop_first_on_list_with_one_node() -> None:
    """Test that pop_first() works on a list with one node."""
    victim = LinkedList(value=4)
    assert victim.pop_first().value == 4
    assert victim.head is None
    assert victim.tail is None
    assert victim.length == 0


def test_pop_first_returned_node_is_not_linked_to_other_nodes() -> None:
    """Test that pop_first() returns a node that is not linked to other nodes."""
    victim = LinkedList(value=4)
    victim.append(value=5)
    victim.append(value=6)
    assert victim.pop_first().next is None


def test_get_node_at_index() -> None:
    """Test that get() returns the node at the given index."""
    victim = LinkedList(value=4)
    victim.append(value=5)
    victim.append(value=6)
    assert victim.get(0).value == 4
    assert victim.get(1).value == 5
    assert victim.get(2).value == 6


def test_get_on_empty_list_returns_none() -> None:
    """Test that get() returns None if the list is empty."""
    victim = LinkedList(value=4)
    victim.head = None
    victim.tail = None
    victim.length = 0
    assert victim.get(0) is None


def test_set_value_sets_value_of_node_at_index() -> None:
    """Test that set_value() sets the value of the node at the given index."""
    victim = LinkedList(value=4)
    victim.append(value=5)
    victim.append(value=6)
    victim.set_value(1, 7)
    assert victim.get(0).value == 4
    assert victim.get(1).value == 7
    assert victim.get(2).value == 6


def test_set_value_on_empty_list_returns_none() -> None:
    """Test that set_value() returns None if the list is empty."""
    victim = LinkedList(value=4)
    victim.head = None
    victim.tail = None
    victim.length = 0
    assert victim.set_value(0, 7) is False
