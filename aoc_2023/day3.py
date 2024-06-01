from typing import Tuple, List
import re


def part1(problem: str) -> int:
    """Part 1 of the problem."""
    grid = to_grid(problem)
    (width, height) = get_dim(grid)
    mask = new_mask(width, height)
    setup_mask_v1(grid, mask, width, height)
    check_hash = hash_mask(mask)
    while True:
        iterate_mask(grid, mask, width, height)
        new_check_hash = hash_mask(mask)
        if new_check_hash == check_hash:
            break
        check_hash = new_check_hash
    masked_grid = mask_grid(grid, mask, width, height)
    numbers = extract_numbers(masked_grid)
    total = sum(numbers)
    return total


def extract_numbers(masked_grid: List[List[str]]) -> List[int]:
    """Extracts the numbers from the masked grid."""
    lines = ["".join(line) for line in masked_grid]
    r = re.compile(r"\d+")
    numbers = []
    for line in lines:
        numbers += [int(n) for n in r.findall(line)]
    return numbers


def mask_grid(
    grid: List[List[str]], mask: List[List[str]], width: int, height: int
) -> List[List[str]]:
    """Masks the grid with the mask."""
    clone = clone_grid(grid)
    for y in range(height):
        for x in range(width):
            if mask[y][x] != "." or not clone[y][x].isdigit():
                clone[y][x] = "."
    return clone


def clone_grid(grid: List[List[int]]) -> List[List[int]]:
    """Clones a grid."""
    return [line.copy() for line in grid]


def iterate_mask(
    grid: List[List[int]], mask: List[List[int]], width: int, height: int
) -> str:
    """Iterates the mask."""
    for y in range(height):
        for x in range(width):
            c = grid[y][x]
            if c.isdigit():
                next_to_special_char = False
                for dy in range(-1, 2):
                    for dx in range(-1, 2):
                        if (
                            x == 0
                            and dx == -1
                            or x == width - 1
                            and dx == 1
                            or y == 0
                            and dy == -1
                            or y == height - 1
                            and dy == 1
                        ):
                            continue
                        c2 = mask[y + dy][x + dx]
                        if c2 == ".":
                            next_to_special_char = True
                if next_to_special_char:
                    mask[y][x] = "."


def hash_mask(mask: List[List[str]]) -> str:
    """Returns a hash of the grid."""
    return "".join(["".join(line) for line in mask])


def to_grid(schema: str) -> List[List[str]]:
    """Converts a string schema to a 2D grid."""
    return [list(line) for line in schema.split("\n")]


def display_grid(grid: List[List[str]]):
    """Displays a 2D grid."""
    out = ""
    for line in grid:
        for c in line:
            out += c
        out += "\n"
    print(out)


def get_dim(grid: List[List[str]]) -> Tuple[int, int]:
    """Returns the width and height of a 2D grid."""
    return (len(grid[0]), len(grid))


def new_mask(width: int, height: int) -> List[List[str]]:
    """Creates a new mask of the same size as the grid."""
    mask = []
    for _ in range(height):
        l = []
        for _ in range(width):
            l.append("_")
        mask.append(l)
    return mask


def setup_mask_v1(
    grid: List[List[str]], mask: List[List[str]], width: int, height: int
):
    """Sets the mask to "." where there are special characters in the grid."""
    for y in range(height):
        for x in range(width):
            c = grid[y][x]
            if c != "." and not c.isdigit():
                mask[y][x] = "."


def setup_mask_v2(
    grid: List[List[str]], mask: List[List[str]], width: int, height: int
):
    """Sets the mask to "." where there are special characters in the grid."""
    for y in range(height):
        for x in range(width):
            c = grid[y][x]
            if c == "*":
                for dy in range(-1, 2):
                    for dx in range(-1, 2):
                        if (
                            x == 0
                            and dx == -1
                            or x == width - 1
                            and dx == 1
                            or y == 0
                            and dy == -1
                            or y == height - 1
                            and dy == 1
                        ):
                            continue
                        if grid[y + dy][x + dx].isdigit():
                            mask[y][x] = "."


def split_masks(
    mask: List[List[str]], width: int, height: int
) -> List[List[List[str]]]:
    """Splits the mask into separate masks."""
    masks_needed = sum([line.count(".") for line in mask])
    masks = [new_mask(width, height) for _ in range(masks_needed)]
    current_mask_index = 0
    for y in range(height):
        for x in range(width):
            if mask[y][x] == ".":
                masks[current_mask_index][y][x] = "."
                current_mask_index += 1
    return masks


def part2(problem: str) -> int:
    """Part 2 of the problem."""
    grid = to_grid(problem)
    (width, height) = get_dim(grid)
    base_mask = new_mask(width, height)
    setup_mask_v2(grid, base_mask, width, height)
    masks = split_masks(base_mask, width, height)
    total = 0
    for mask in masks:
        check_hash = hash_mask(mask)
        while True:
            iterate_mask(grid, mask, width, height)
            new_check_hash = hash_mask(mask)
            if new_check_hash == check_hash:
                break
            check_hash = new_check_hash
        masked_grid = mask_grid(grid, mask, width, height)
        numbers = extract_numbers(masked_grid)
        if len(numbers) == 2:
            total += numbers[0] * numbers[1]
    return total
