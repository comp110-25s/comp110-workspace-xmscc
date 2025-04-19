"""Linked list practice!"""

from __future__ import annotations

__author__: str = "730824666"


class Node:
    """Node in a singly-linked list recursive structure."""

    value: int
    next: Node | None

    def __init__(self, value: int, next: Node | None):
        """Node function itself."""
        self.value = value
        self.next = next

    def __str__(self) -> str:
        """Print Node magic mathod."""
        if self.next is None:
            return f"{self.value} -> None"
        else:
            return f"{self.value} -> {self.next}"


def value_at(head: Node | None, index: int) -> int:
    """Return the value of the Node stored at the given index."""
    if head is None:
        raise IndexError("Index is out of bounds on the list.")
    elif index == 0:
        return head.value
    else:
        return value_at(head.next, index - 1)


def max(head: Node | None) -> int:
    """Return the maximum value."""
    if head is None:
        raise ValueError("Cannot call max with None")
    elif head.next is None:
        return head.value
    else:
        max_rest = max(head.next)
        return head.value if head.value > max_rest else max_rest


def linkify(items: list[int]) -> Node | None:
    """Return a Linked List of Nodes with the same values."""
    if len(items) == 0:
        return None
    else:
        return Node(items[0], linkify(items[1:]))


def scale(head: Node | None, factor: int) -> Node | None:
    """Return a new linked list."""
    if head is None:
        return None
    else:
        return Node(head.value * factor, scale(head.next, factor))
