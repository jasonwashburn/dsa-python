"""Iplements a HashTable class."""


class HashTable:
    """A HashTable class."""

    def __init__(self, size: int = 7) -> None:
        """Initialize a HashTable instance.

        Args:
            size (int, optional): The size of the HashTable. Defaults to 7.
        """
        self.data_map: list = [None] * size
