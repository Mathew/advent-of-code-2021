import typing


class Display(typing.NamedTuple):
    signals: tuple[str, ...]
    output: tuple[str, ...]


def find_digits(display: Display):
    values = {3: "7", 2: "1", 7: "4", 4: "8"}
    return sum(1 for out in display.output if values.get(len(out)))


if __name__ == "__main__":
    with open("./input.txt") as f:
        entries = [line.strip().split("|") for line in f.readlines()]

    displays = [Display(tuple(entry[0].strip().split(" ")), tuple(entry[1].strip().split(" "))) for entry in entries]

    print(f"Part One: {sum(find_digits(display) for display in displays)}")
