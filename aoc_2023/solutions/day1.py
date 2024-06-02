"""Solutions for day 1."""


def line_to_number(line: str) -> int:
    """Convert a line to a number."""
    chars = []
    for char in line:
        if char.isdigit():
            chars.append(char)
    if len(chars) == 0:
        return 0
    return int(chars[0]) * 10 + int(chars[-1])


def process_line(line: str) -> str:
    """Process the line to convert text into numbers."""
    line = line.replace("one", "on1e")
    line = line.replace("two", "t2wo")
    line = line.replace("three", "t3hree")
    line = line.replace("four", "4four")
    line = line.replace("five", "5five")
    line = line.replace("six", "6six")
    line = line.replace("seven", "7seven")
    line = line.replace("eight", "eig8ht")
    line = line.replace("nine", "9nine")
    return line


def part1(problem: str) -> int:
    """Part 1 of the problem."""
    total = 0
    for line in problem.split("\n"):
        total += line_to_number(line)
    return total


def part2(problem: str) -> int:
    """Part 2 of the problem."""
    total = 0
    for line in problem.split("\n"):
        total += line_to_number(process_line(line))
    return total
