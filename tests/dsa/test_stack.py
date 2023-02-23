"""Tests for stack.py."""
from io import StringIO
from unittest.mock import patch

import pytest

from dsa.stack import Node, Stack


@pytest.fixture()
def single_item_stack() -> Stack:
    """Return a stack with a single item."""
    return Stack(value=4)


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
def test_print_stack(mock_stdout, single_item_stack) -> None:
    """Test that print_stack() prints the stack to stdout."""
    victim = single_item_stack
    victim.print_stack()
    assert mock_stdout.getvalue() == "4\n"
