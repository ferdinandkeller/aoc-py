"""Solutions for day 4."""

import re
from typing import List, Tuple


def part1(problem: str) -> int:
    """Solution for part 1."""
    parsed_cards = parse_cards(problem)
    matches = compute_cards_matches(parsed_cards)
    score = compute_cards_score(matches)
    return score


def parse_cards(cards: str) -> List[Tuple[List[int], List[int]]]:
    """Parse the card data."""
    return [parse_card(card) for card in cards.split("\n")]


def parse_card(card: str) -> Tuple[List[int], List[int]]:
    """Parse the card data."""
    re_1 = re.compile(r"Card +\d+: (.*)")
    m = re_1.match(card).group(1)
    s = m.split(" | ")
    return (parse_numbers(s[0]), parse_numbers(s[1]))


def parse_numbers(numbers: str) -> List[int]:
    """Parse the numbers."""
    out = []
    for n in numbers.split(" "):
        if len(n) > 0:
            out.append(int(n))
    return out


def compute_cards_matches(cards: List[Tuple[List[int], List[int]]]) -> List[int]:
    """Compute the total matches of all cards."""
    return [compute_card_matches(card) for card in cards]


def compute_card_matches(card: Tuple[List[int], List[int]]) -> int:
    """Compute the match for a single card."""
    valid_number = 0
    for n in card[0]:
        if n in card[1]:
            valid_number += 1
    return valid_number


def compute_cards_score(matches: List[int]) -> int:
    """Compute the total score of all cards."""
    return sum([compute_card_score(card) for card in matches])


def compute_card_score(matches: int) -> int:
    """Compute the score for a single card."""
    return 2 ** (matches - 1) if matches > 0 else 0


def compute_matches_tower(matches: List[int]) -> List[int]:
    """Compute the total matches of all cards."""
    tower = [1 for _ in range(len(matches))]
    c = len(matches)
    for h in range(c):
        for h2 in range(h + 1, min(h + 1 + matches[h], c)):
            tower[h2] += tower[h]
    return tower


def part2(problem: str) -> int:
    """Solution for part 2."""
    parsed_cards = parse_cards(problem)
    matches = compute_cards_matches(parsed_cards)
    tower = compute_matches_tower(matches)
    score = sum(tower)
    return score
