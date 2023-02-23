"""Tests for stack.py."""
from io import StringIO
from unittest.mock import patch

import pytest

from dsa.stack import Node, Stack


@pytest.fixture()
def single_item_stack() -> Stack:
    """Return a stack with a single item."""
    return Stack(value=4)


@pytest.fixture()
def multi_item_stack() -> Stack:
    """Return a stack with a single item."""
    stack = Stack(value=4)
    stack.push(5)
    stack.push(6)
    return stack


@pytest.fixture()
def empty_stack() -> Stack:
    """Return an empty stack."""
    stack = Stack(value=4)
    stack.top = None
    stack.height = 0
    return stack


def test_node_builds() -> None:
    """Test that the node class builds."""
    victim = Node(value=4)
    assert victim.value == 4
    assert victim.next is None


def test_stack_builds() -> None:
    """Test that the stack builds."""
    victim = Stack(value=4)
    assert victim.top.value == 4
    assert victim.height == 1


@patch("sys.stdout", new_callable=StringIO)
def test_print_stack(mock_stdout, multi_item_stack) -> None:
    """Test that print_stack() prints the stack to stdout."""
    victim = multi_item_stack
    victim.print_stack()
    assert mock_stdout.getvalue() == "6\n5\n4\n"


def test_push(single_item_stack) -> None:
    """Test that push() adds a node to the stack."""
    victim = single_item_stack
    victim.push(5)
    assert victim.top.value == 5
    assert victim.top.next.value == 4
    assert victim.height == 2


def test_push_on_empty_stack(empty_stack) -> None:
    """Test that push() adds a node to the stack."""
    victim = empty_stack
    victim.push(5)
    assert victim.top.value == 5
    assert victim.height == 1


def test_pop(multi_item_stack) -> None:
    """Test that pop() removes a node from the stack."""
    victim = multi_item_stack
    victim.pop()
    assert victim.top.value == 5
    assert victim.height == 2


def test_pop_on_single_item_stack(single_item_stack) -> None:
    """Test that pop() removes a node from the stack."""
    victim = single_item_stack
    victim.pop()
    assert victim.top is None
    assert victim.height == 0


def test_pop_on_empty_stack(empty_stack) -> None:
    """Test that pop() removes a node from the stack."""
    victim = empty_stack
    assert victim.pop() is None
