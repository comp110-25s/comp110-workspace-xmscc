"""File to define Fish class."""


class Fish:
    """Fish class."""

    age: int

    def __init__(self) -> None:
        """Initial value."""
        self.age = 0

    def one_day(self) -> None:
        """Everyday changes."""
        self.age += 1
