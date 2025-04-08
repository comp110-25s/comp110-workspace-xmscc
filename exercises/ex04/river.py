"""File to define River class."""

__author__: str = "730824666"

from exercises.EX04.fish import Fish
from exercises.EX04.bear import Bear


class River:
    """River class."""

    day: int
    bears: list
    fish: list

    def __init__(self, num_fish: int, num_bears: int):
        """New River with num_fish Fish and num_bears Bears."""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for _ in range(0, num_fish):
            self.fish.append(Fish())
        for _ in range(0, num_bears):
            self.bears.append(Bear())

    def check_ages(self) -> None:
        """Keep only fish age 3 or less."""
        surviving_fish: list = []
        for fish in self.fish:
            if fish.age <= 3:
                surviving_fish.append(fish)
        self.fish = surviving_fish

        """Keep only bears age 5 or less."""
        surviving_bears: list = []
        for bear in self.bears:
            if bear.age <= 5:
                surviving_bears.append(bear)
        self.bears = surviving_bears

    def remove_fish(self, amount: int) -> None:
        """Remove amount many Fish from the River."""
        for _ in range(min(amount, len(self.fish))):
            self.fish.pop(0)

    def bears_eating(self) -> None:
        """Bear will eat 3 Fish if there are at least 5."""
        for bear in self.bears:
            if len(self.fish) >= 5:
                self.remove_fish(3)
                bear.eat(3)

    def check_hunger(self) -> None:
        """Checks the hunger_score."""
        surviving_bears: list = []
        for bear in self.bears:
            if bear.hunger_score >= 0:
                surviving_bears.append(bear)
        self.bears = surviving_bears

    def repopulate_fish(self) -> None:
        """Each pair of fish will produce 4 offspring."""
        new_fish = (len(self.fish) // 2) * 4
        for _ in range(new_fish):
            self.fish.append(Fish())

    def repopulate_bears(self) -> None:
        """Each pair of Bear's will produce 1 offspring."""
        new_bears = len(self.bears) // 2
        for _ in range(new_bears):
            self.bears.append(Bear())

    def view_river(self) -> None:
        """Print the simulation."""
        print(f"~~~ Day {self.day}: ~~~")
        print(f"Fish population: {len(self.fish)}")
        print(f"Bear population: {len(self.bears)}")

    def one_river_day(self) -> None:
        """Simulate one day of life in the river."""
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for bear in self.bears:
            bear.one_day()
        # Simulate one day for all Fish
        for fish in self.fish:
            fish.one_day()
        # Simulate Bear's eating
        self.bears_eating()
        # Remove hungry Bear's from River
        self.check_hunger()
        # Remove old Fish and Bear's from River
        self.check_ages()
        # Simulate Fish repopulation
        self.repopulate_fish()
        # Simulate Bear repopulation
        self.repopulate_bears()
        # Visualize River
        self.view_river()

    def one_river_week(self) -> None:
        """Call one_river_day() seven times."""
        for _ in range(7):
            self.one_river_day()
