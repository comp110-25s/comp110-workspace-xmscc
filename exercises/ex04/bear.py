"""File to define Bear class."""


class Bear:
    """Bear class."""

    age: int
    hunger_score: int

    def __init__(self) -> None:
        """Initial value."""
        self.age = 0
        self.hunger_score = 0

    def one_day(self) -> None:
        """Every day changes."""
        self.age += 1
        self.hunger_score -= 1

    def eat(self, num_fish: int) -> None:
        """Bear's eating changes."""
        self.hunger_score += num_fish
