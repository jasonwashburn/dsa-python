"""Tests for the queue module."""

from io import StringIO
from unittest.mock import patch

import pytest

from dsa.queue import Node, Queue


@pytest.fixture()
def empty_queue() -> Queue:
    """Create an empty queue."""
    queue = Queue(value=4)
    queue.first = None
    queue.last = None
    queue.length = 0
    return queue


@pytest.fixture()
def single_item_queue() -> Queue:
    """Create a queue with a single item."""
    return Queue(value=4)


def test_node_builds() -> None:
    """Test that a node can be built."""
    victim = Node(value=4)
    assert victim.value == 4
    assert victim.next is None


def test_queue_builds() -> None:
    """Test that a queue can be built."""
    victim = Queue(value=4)
    assert victim.first.value == 4
    assert victim.last is victim.first
    assert victim.length == 1


def test_queue_supports_len(single_item_queue) -> None:
    """Test that a queue can be built."""
    assert len(single_item_queue) == 1


@patch("sys.stdout", new_callable=StringIO)
def test_print_queue(mock_stdout, single_item_queue) -> None:
    """Test that print_list() prints the list to stdout."""
    single_item_queue.print_queue()
    assert mock_stdout.getvalue() == "4\n"


def test_enqueue(single_item_queue) -> None:
    """Test that enqueue() adds a node to the queue."""
    victim = single_item_queue
    victim.enqueue(5)
    assert victim.length == 2
    assert victim.first.value == 4
    assert victim.last.value == 5


def test_enqueue_on_empty_queue(empty_queue) -> None:
    """Test that enqueue() adds a node to the queue."""
    victim = empty_queue
    victim.enqueue(5)
    assert victim.length == 1
    assert victim.first.value == 5
    assert victim.last.value == 5
