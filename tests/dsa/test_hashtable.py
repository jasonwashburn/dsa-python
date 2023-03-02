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


@pytest.mark.parametrize(
    ("key", "value", "expected_index", "expected_value"),
    [
        ("abc", 123, 0, [("abc", 123)]),
        ("bcd", 456, 6, [("bcd", 456)]),
        ("cde", 789, 5, [("cde", 789)]),
    ],
)
def test_set(
    key: str,
    value: object,
    expected_index: int,
    expected_value: list[tuple[str, object]],
) -> None:
    """Tests that the HashTable sets correctly.

    Args:
        key (str): The key to be hashed.
        value (object): The value to be stored.
        expected_index (int): The expected index.
        expected_value (list[tuple[str, object]]): The expected value.
    """
    victim = HashTable()
    victim.set_value(key=key, value=value)
    assert victim.data_map[expected_index] == expected_value


@pytest.mark.parametrize(
    (
        "key_value_one",
        "key_value_two",
        "expected_index",
        "expected_value",
    ),
    [
        (("abc", 123), ("cba", 321), 0, [("abc", 123), ("cba", 321)]),
        (("bcd", 456), ("dcb", 654), 6, [("bcd", 456), ("dcb", 654)]),
    ],
)
def test_set_with_collision(
    key_value_one: tuple[str, object],
    key_value_two: tuple[str, object],
    expected_index: int,
    expected_value: list[tuple[str, object]],
) -> None:
    """Tests that the HashTable sets correctly with collisions.

    Args:
        key_value_one (tuple[str, object]): A key value pair.
        key_value_two (tuple[str, object]): A key value pair.
        expected_index (int): The expected index.
        expected_value (list[tuple[str, object]]): The expected value.
    """
    victim = HashTable()
    victim.set_value(key=key_value_one[0], value=key_value_one[1])
    victim.set_value(key=key_value_two[0], value=key_value_two[1])
    assert victim.data_map[expected_index] == expected_value
