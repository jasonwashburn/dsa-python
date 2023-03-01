"""Tests for HashTable class."""
import pytest

from dsa.hashtable import HashTable


def test_hastable_builds() -> None:
    """Tests that the HashTable class builds."""
    victim = HashTable()
    assert len(victim.data_map) == 7


def test_hashtable_builds_with_size() -> None:
    """Tests that the HashTable class builds with a size."""
    victim = HashTable(11)
    assert len(victim.data_map) == 11


@pytest.mark.parametrize(
    ("size", "key", "expected"),
    [
        (7, "abc", 0),
        (7, "bcd", 6),
        (7, "cde", 5),
        (7, "def", 4),
        (9, "abc", 3),
        (9, "bcd", 0),
        (9, "cde", 6),
        (9, "def", 3),
    ],
)
def test_hash(size, key, expected) -> None:
    """Tests that the HashTable class builds with a size.

    Args:
        size (int): The size of the HashTable.
        key (str): The key to be hashed.
        expected (int): The expected hash.
    """
    victim = HashTable(size=size)
    assert victim._hash(key) == expected
