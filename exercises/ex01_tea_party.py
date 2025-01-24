"""A small program for the tea party!"""

__author__: str = "730824666"


def main_planner(guests: int) -> None:
    """bring all following function together"""
    print(f"A Cozy Tea Party for {guests} People!")
    print(f"Tea Bags: {tea_bags(people=guests)}")
    print(f"Treats: {treats(people=guests)}")
    print(
        f"Cost: ${cost(tea_count=tea_bags(people=guests), treat_count=treats(people=guests))}"
    )


def tea_bags(people: int) -> int:
    """calculate the number of tea bags needed"""
    return people * 2


def treats(people: int) -> int:
    """calculate the number of treats needed"""
    return int(1.5 * tea_bags(people=people))


def cost(tea_count: int, treat_count: int) -> float:
    """calculate needed cost"""
    return tea_count * 0.5 + treat_count * 0.75


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party? ")))
