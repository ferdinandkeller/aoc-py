"""Solutions for day 5."""

from math import sqrt, ceil
from dataclasses import dataclass
from typing import List
import re


@dataclass
class Race:
    """Represents a single race."""

    time: int
    distance: int


def parse_races_v1(problem: str) -> List[Race]:
    """Parses the races to usefull data."""
    r1 = re.compile(r"Time: +(.+)\nDistance: +(.+)")
    m = r1.match(problem)
    raw_times = m.group(1)
    raw_distances = m.group(2)
    r2 = re.compile(r"(\d+)")
    times = r2.findall(raw_times)
    distances = r2.findall(raw_distances)
    races = []
    n = len(times)
    for i in range(n):
        races.append(Race(time=int(times[i]), distance=int(distances[i])))
    return races


def parse_races_v2(problem: str) -> Race:
    """Parses the race to usefull data."""
    r1 = re.compile(r"Time: +(.+)\nDistance: +(.+)")
    m = r1.match(problem)
    time = int(m.group(1).replace(" ", ""))
    distance = int(m.group(2).replace(" ", ""))
    return Race(time=time, distance=distance)


def compute_winning_ranges(races: List[Race]) -> List[range]:
    """Computes the winning ranges for each race"""
    return [compute_winning_range(r) for r in races]


def compute_winning_range(race: Race) -> range:
    """Computes the range of winning"""
    delta = sqrt(race.time**2 - 4 * race.distance)
    range_start_float = (race.time - delta) / 2
    if range_start_float.is_integer():
        range_start = int(range_start_float) + 1
    else:
        range_start = ceil(range_start_float)
    range_end_float = (race.time + delta) / 2
    if range_end_float.is_integer():
        range_end = int(range_end_float)
    else:
        range_end = ceil(range_end_float)
    return range(range_start, range_end)


def compute_score(winning_ranges: List[range]) -> int:
    """Compute the winning score."""
    total = 1
    for winning_range in winning_ranges:
        total *= len(winning_range)
    return total


def part1(problem: str) -> int:
    """Solution for part 1."""
    races = parse_races_v1(problem)
    winning_ranges = compute_winning_ranges(races)
    return compute_score(winning_ranges)


def part2(problem: str) -> int:
    """Solution for part 2."""
    race = parse_races_v2(problem)
    winning_range = compute_winning_range(race)
    return len(winning_range)
