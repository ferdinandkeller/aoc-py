"""Solutions for day 5."""

import re
from typing import List, Tuple, Optional

Map = Tuple[int, int, int]
MapList = List[Map]
TargetSourceMap = Tuple[Tuple[str, str], MapList]
Instruction = Tuple[List[int], List[TargetSourceMap]]


def ranges_intersection(
    r1: Tuple[int, int], r2: Tuple[int, int]
) -> Optional[Tuple[int, int]]:
    """Find the intersection of two ranges."""
    if not (r1[1] <= r2[0] or r2[1] <= r1[0]):
        return (max(r1[0], r2[0]), min(r1[1], r2[1]))
    return None


def ranges_sub(r1: Tuple[int, int], r2: Tuple[int, int]) -> List[Tuple[int, int]]:
    """Subtract two ranges."""
    if r1[1] <= r2[0] or r2[1] <= r1[0]:
        return [r1]
    if r2[0] <= r1[0] and r1[1] <= r2[1]:
        return []
    if r1[0] < r2[0] and r2[1] < r1[1]:
        return [(r1[0], r2[0]), (r2[1], r1[1])]
    if r1[0] <= r2[0]:
        return [(r1[0], r2[0])]
    if r2[1] <= r1[1]:
        return [(r2[1], r1[1])]
    raise Exception("This should not happen.")  # pylint: disable=broad-exception-raised


def join_ranges(ranges: List[Tuple[int, int]]) -> List[Tuple[int, int]]:
    """Join ranges."""
    split_ranges = []
    for r in ranges:
        split_ranges.append(("start", r[0]))
        split_ranges.append(("end", r[1]))
    split_ranges.sort(key=lambda x: (x[1], 0 if x[0] == "start" else 1))
    result = []
    state = 0
    tmp = None
    for value in split_ranges:
        if value[0] == "start":
            state += 1
            if state == 1:
                tmp = value[1]
        if value[0] == "end":
            state -= 1
            if state == 0:
                result.append((tmp, value[1]))
    return result


def split_range(
    r1: Tuple[int, int], r2: Tuple[int, int]
) -> Tuple[Tuple[int, int], List[Tuple[int, int]]]:
    """Apply a range to another range."""
    matching = ranges_intersection(r1, r2)
    remaining = ranges_sub(r1, r2)
    return (matching, remaining)


def slide_range(r: Tuple[int, int], delta: int) -> Tuple[int, int]:
    """Move a range."""
    return (r[0] + delta, r[1] + delta)


def parse_instructions(parse_seed, instructions: str) -> Instruction:
    """Parse the instructions."""
    instructions = instructions.split("\n\n")
    seeds = parse_seed(instructions[0])
    parsed = []
    for instruction in instructions[1:]:
        parsed.append(parse_instruction(instruction))
    return (seeds, parsed)


def parse_instruction(instruction: str) -> TargetSourceMap:
    """Parse a single instruction."""
    lines = instruction.split("\n")
    text = lines[0]
    values = lines[1:]
    r1 = re.compile(r"(\w+)-to-(\w+) map:")
    m = r1.match(text)
    source = m.group(1)
    target = m.group(2)
    r2 = re.compile(r"(\d+)")
    numbers = []
    for value in values:
        numbers.append([int(n) for n in r2.findall(value)])
    return ((source, target), numbers)


def parse_seeds_v1(seeds: str) -> List[Tuple[int, int]]:
    """Parse the seeds."""
    r = re.compile(r"(\d+)")
    return [(int(n), int(n) + 1) for n in r.findall(seeds)]


def parse_seeds_v2(seeds: str) -> List[Tuple[int, int]]:
    """Parse the seeds."""
    r = re.compile(r"(\d+)")
    numbers = [int(n) for n in r.findall(seeds)]
    out = []
    for i in range(0, len(numbers), 2):
        out.append((numbers[i], numbers[i] + numbers[i + 1]))
    return out


def convert(value: Tuple[str, int], tables: List[TargetSourceMap]) -> Tuple[str, int]:
    """Find which table to use."""
    for table in tables:
        if table[0][0] == value[0]:
            return (table[0][1], convert_using_table(value[1], table))


def convert_using_table(
    values: List[Tuple[int, int]], table: TargetSourceMap
) -> List[Tuple[int, int]]:
    """Convert the value using the table."""
    unprocessed = values
    processed = []
    for custom_map in table[1]:
        delta = custom_map[0] - custom_map[1]
        filter_range = (custom_map[1], custom_map[1] + custom_map[2])
        matching = []
        remaining = []
        for value in unprocessed:
            (mat, rem) = split_range(value, filter_range)
            remaining += rem
            if mat is None:
                continue
            matching.append(slide_range(mat, delta))
        unprocessed = remaining
        processed += matching
    return processed + unprocessed


def solve(seeds: List[Tuple[int, int]], instructions: List[TargetSourceMap]) -> int:
    """Solve the problem."""
    locations = []
    for seed in seeds:
        v = ("seed", [seed])
        while v[0] != "location":
            v = convert(v, instructions)
        locations += v[1]
    return min([v[0] for v in locations])


def part1(problem: str) -> int:
    """Solution for part 1."""
    (seeds, instructions) = parse_instructions(parse_seeds_v1, problem)
    return solve(seeds, instructions)


def part2(problem: str) -> int:
    """Solution for part 2."""
    (seeds, instructions) = parse_instructions(parse_seeds_v2, problem)
    return solve(seeds, instructions)
