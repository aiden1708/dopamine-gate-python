#!/usr/bin/env python3

from dataclasses import dataclass


@dataclass
class Mismatch:
    position: int
    expected: str
    actual: str


def find_first_mismatch(
    typed: str,
    expected: str,
) -> Mismatch | None:
    """Find the first character that differs."""

    minimum = min(len(typed), len(expected))

    for index in range(minimum):
        if typed[index] != expected[index]:
            return Mismatch(
                position=index,
                expected=expected[index],
                actual=typed[index],
            )

    if len(typed) > len(expected):
        return Mismatch(
            position=len(expected),
            expected="",
            actual=typed[len(expected)],
        )

    if len(typed) < len(expected):
        return Mismatch(
            position=len(typed),
            expected=expected[len(typed)],
            actual="",
        )

    return None


def is_complete(
    typed: str,
    expected: str,
) -> bool:
    return typed == expected
