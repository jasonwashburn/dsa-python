"""Tests for HashTable class."""
from dsa.hashtable import HashTable


def test_hastable_builds() -> None:
    """Tests that the HashTable class builds."""
    victim = HashTable()
    assert len(victim.data_map) == 7


def test_hashtable_builds_with_size() -> None:
    """Tests that the HashTable class builds with a size."""
    victim = HashTable(11)
    assert len(victim.data_map) == 11
