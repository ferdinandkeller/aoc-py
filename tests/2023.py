"""Test all the solutions.
"""

import aoc_2023.solutions.day1
import aoc_2023.solutions.day2
import aoc_2023.solutions.day3
import aoc_2023.solutions.day4
import aoc_2023.solutions.day5
import aoc_2023.solutions.day6


def test_day1():
    """Test the solutions for day 1."""
    with open("aoc_2023/inputs/day1.txt", encoding="utf-8") as f:
        problem = f.read()
    print(aoc_2023.solutions.day1.part1(problem))
    print(aoc_2023.solutions.day1.part2(problem))


def test_day2():
    """Test the solutions for day 2."""
    with open("aoc_2023/inputs/day2.txt", encoding="utf-8") as f:
        problem = f.read()
    print(aoc_2023.solutions.day2.part1(problem))
    print(aoc_2023.solutions.day2.part2(problem))


def test_day3():
    """Test the solutions for day 3."""
    with open("aoc_2023/inputs/day3.txt", encoding="utf-8") as f:
        problem = f.read()
    print(aoc_2023.solutions.day3.part1(problem))
    print(aoc_2023.solutions.day3.part2(problem))


def test_day4():
    """Test the solutions for day 4."""
    with open("aoc_2023/inputs/day4.txt", encoding="utf-8") as f:
        problem = f.read()
    print(aoc_2023.solutions.day4.part1(problem))
    print(aoc_2023.solutions.day4.part2(problem))


def test_day5():
    """Test the solutions for day 5."""
    with open("aoc_2023/inputs/day5.txt", encoding="utf-8") as f:
        problem = f.read()
    print(aoc_2023.solutions.day5.part1(problem))
    print(aoc_2023.solutions.day5.part2(problem))


def test_day6():
    """Test the solutions for day 6."""
    with open("aoc_2023/inputs/day6.txt", encoding="utf-8") as f:
        problem = f.read()
    print(aoc_2023.solutions.day6.part1(problem))
    print(aoc_2023.solutions.day6.part2(problem))
