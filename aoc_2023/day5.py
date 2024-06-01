"""Solutions for day 5."""

import re
from typing import List, Tuple, Optional, Callable
from dataclasses import dataclass


@dataclass
class SourcedRanges:
    """Sourced range."""

    source: str
    ranges: List[range]


@dataclass
class MapDescription:
    """Map description."""

    map_range: range
    delta: int


@dataclass
class MapTable:
    """Target map description."""

    source: str
    target: str
    maps_descriptions: List[MapDescription]


@dataclass
class Instructions:
    """Mapping instruction."""

    seeds: List[SourcedRanges]
    targets: List[MapTable]


@dataclass
class RangeSplit:
    """Range split."""

    matching: range
    remaining: List[range]


def ranges_intersection(r1: range, r2: range) -> Optional[range]:
    """Find the intersection of two ranges."""
    if not (r1.stop <= r2.start or r2.stop <= r1.start):
        return range(max(r1.start, r2.start), min(r1.stop, r2.stop))
    return None


def ranges_sub(r1: range, r2: range) -> List[range]:
    """Subtract two ranges."""
    if r1.end <= r2.start or r2.end <= r1.start:
        return [r1]
    if r2.start <= r1.start and r1.end <= r2.end:
        return []
    if r1.start < r2.start and r2.end < r1.end:
        return [(r1.start, r2.start), (r2.end, r1.end)]
    if r1.start <= r2.start:
        return [(r1.start, r2.start)]
    if r2.end <= r1.end:
        return [(r2.end, r1.end)]
    raise Exception("This should not happen.")  # pylint: disable=broad-exception-raised


def join_ranges(ranges: List[range]) -> List[range]:
    """Join ranges."""
    split_ranges = []
    for r in ranges:
        split_ranges.append((r.start, 0))
        split_ranges.append((r.stop, 1))
    split_ranges.sort()
    result = []
    state = 0
    tmp = None
    for value in split_ranges:
        if value[1] == 0:
            state += 1
            if state == 1:
                tmp = value[0]
        if value[1] == 1:
            state -= 1
            if state == 0:
                result.append(range(tmp, value[0]))
    return result


def split_range(
    r1: range,
    r2: range,
) -> RangeSplit:
    """Apply a range to another range."""
    matching = ranges_intersection(r1, r2)
    remaining = ranges_sub(r1, r2)
    return RangeSplit(matching, remaining)


def slide_range(r: range, delta: int) -> range:
    """Move a range."""
    return range(r.start + delta, r.stop + delta)


def parse_seeds_v1(raw_seeds: str) -> List[SourcedRanges]:
    """Parse the seed (version 1)."""
    r = re.compile(r"(\d+)")
    return [
        SourcedRanges(source="seed", ranges=range(int(n), int(n) + 1))
        for n in r.findall(raw_seeds)
    ]


def parse_seeds_v2(seeds: str) -> List[SourcedRanges]:
    """Parse the seeds (version 2)."""
    r = re.compile(r"(\d+)")
    numbers = [int(n) for n in r.findall(seeds)]
    out = []
    for i in range(0, len(numbers), 2):
        out.append(
            SourcedRanges(
                source="seed", ranges=range(numbers[i], numbers[i] + numbers[i + 1])
            )
        )
    return out


def parse_instruction(block: str) -> MapTable:
    """Parse a single instruction."""
    lines = block.split("\n")
    text = lines[0]
    values = lines[1:]
    r1 = re.compile(r"(\w+)-to-(\w+) map:")
    m = r1.match(text)
    source = m.group(1)
    target = m.group(2)
    r2 = re.compile(r"(\d+)")
    maps_descriptions: List[MapDescription] = []
    for value in values:
        single_map = [int(n) for n in r2.findall(value)]
        maps_descriptions.append(
            MapDescription(
                map_range=range(single_map[1], single_map[1] + single_map[2]),
                delta=single_map[0] - single_map[1],
            )
        )
    return MapTable(source, target, maps_descriptions)


def parse_instructions(
    parse_seed_fn: Callable[[str], List[range]], raw_instructions: str
) -> Instructions:
    """Parse the instructions."""
    blocks = raw_instructions.split("\n\n")
    seeds = parse_seed_fn(blocks[0])
    targets = []
    for block in blocks[1:]:
        targets.append(parse_instruction(block))
    return Instructions(seeds, targets)


def convert_using_table(
    sourced_ranges: SourcedRanges, table: MapTable
) -> SourcedRanges:
    """Convert the value using the table."""
    unprocessed = sourced_ranges.ranges
    processed = []
    for map_description in table.maps_descriptions:
        matching = []
        remaining = []
        for value in unprocessed:
            range_split = split_range(value, map_description.map_range)
            remaining += range_split.remaining
            if range_split.matching is None:
                continue
            matching.append(slide_range(range_split.matching, map_description.delta))
        unprocessed = remaining
        processed += matching
    return processed + unprocessed


def convert(sourced_range: SourcedRanges, tables: List[MapTable]) -> SourcedRanges:
    """Find which table to use."""
    for table in tables:
        if table.source == sourced_range.source:
            return SourcedRanges(
                source=table.target,
                ranges=convert_using_table(sourced_range, table),
            )


def solve(instructions: Instructions) -> int:
    """Solve the problem."""
    locations = []
    for seed in instructions.seeds:
        while seed.source != "location":
            seed = convert(seed, instructions)
        locations += seed.ranges
    return min([v.start for v in locations])


def part1(problem: str) -> int:
    """Solution for part 1."""
    instructions = parse_instructions(parse_seeds_v1, problem)
    return solve(instructions)


def part2(problem: str) -> int:
    """Solution for part 2."""
    instructions = parse_instructions(parse_seeds_v2, problem)
    return solve(instructions)
