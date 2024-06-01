import re
from typing import Tuple, Dict


def part1(input: str) -> int:
    ok = {"red": 12, "green": 13, "blue": 14}
    total = 0
    for line in input.split("\n"):
        group_details = get_group_details(line)
        if (
            group_details[1]["red"] <= ok["red"]
            and group_details[1]["green"] <= ok["green"]
            and group_details[1]["blue"] <= ok["blue"]
        ):
            total += group_details[0]
    return total


def get_group_details(line: str) -> Tuple[int, Dict[str, int]]:
    r1 = re.compile(r"Game (\d+): (.+)")
    r2 = re.compile(r"(\d+) (\w+)")

    group_top = {}
    m1 = r1.match(line)
    group_id = int(m1.group(1))
    for group in m1.group(2).split("; "):
        for card in group.split(", "):
            m2 = r2.match(card)
            number = int(m2.group(1))
            color = m2.group(2)
            if color not in group_top:
                group_top[color] = number
            group_top[color] = max(group_top[color], number)
    return (group_id, group_top)


def part2(input: str) -> int:
    total = 0
    for line in input.split("\n"):
        group_details = get_group_details(line)
        group_power = (
            group_details[1]["red"]
            * group_details[1]["green"]
            * group_details[1]["blue"]
        )
        total += group_power
    return total
