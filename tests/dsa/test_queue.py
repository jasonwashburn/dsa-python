"""Tests for the queue module."""

from dsa.queue import Node, Queue


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
