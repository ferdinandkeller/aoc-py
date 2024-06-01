"""Test all the solutions.
"""

import aoc_2023.day1
import aoc_2023.day2
import aoc_2023.day3
import aoc_2023.day4
import aoc_2023.day5


def day1():
    """Test the solutions for day 1."""
    with open("inputs/day1.txt", encoding="utf-8") as f:
        problem = f.read()
    print(aoc_2023.day1.part1(problem))
    print(aoc_2023.day1.part2(problem))


def day2():
    """Test the solutions for day 2."""
    with open("inputs/day2.txt", encoding="utf-8") as f:
        problem = f.read()
    print(aoc_2023.day2.part1(problem))
    print(aoc_2023.day2.part2(problem))


def day3():
    """Test the solutions for day 3."""
    with open("inputs/day3.txt", encoding="utf-8") as f:
        problem = f.read()
    print(aoc_2023.day3.part1(problem))
    print(aoc_2023.day3.part2(problem))


def day4():
    """Test the solutions for day 4."""
    with open("inputs/day4.txt", encoding="utf-8") as f:
        problem = f.read()
    print(aoc_2023.day4.part1(problem))
    print(aoc_2023.day4.part2(problem))


def day5():
    """Test the solutions for day 5."""
    with open("inputs/day5.txt", encoding="utf-8") as f:
        problem = f.read()
    print(aoc_2023.day5.part1(problem))
    print(aoc_2023.day5.part2(problem))
