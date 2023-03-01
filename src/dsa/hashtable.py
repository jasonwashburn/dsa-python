"""Iplements a HashTable class."""


class HashTable:
    """A HashTable class."""

    def __init__(self, size: int = 7) -> None:
        """Initialize a HashTable instance.

        Args:
            size (int, optional): The size of the HashTable. Defaults to 7.
        """
        self.data_map: list = [None] * size

    def _hash(self, key: str) -> int:
        my_hash = 0
        for letter in key:
            my_hash = (my_hash + ord(letter) * 23) % len(self.data_map)
        return my_hash
