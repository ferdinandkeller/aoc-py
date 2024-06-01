def part1(input: str) -> int:
    total = 0
    for line in input.split("\n"):
        total += line_to_number(line)
    return total


def line_to_number(line: str) -> int:
    chars = []
    for char in line:
        if char.isdigit():
            chars.append(char)
    if len(chars) == 0:
        return 0
    return int(chars[0]) * 10 + int(chars[-1])


def processed_line(line: str) -> str:
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


def part2(input: str) -> int:
    # replace text with digits
    total = 0
    for line in input.split("\n"):
        total += line_to_number(processed_line(line))
    return total
