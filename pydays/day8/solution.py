import itertools
import typing


class Display(typing.NamedTuple):
    signals: tuple[str, ...]
    output: tuple[str, ...]


def find_digits(display: Display) -> int:
    values = {3: "7", 2: "1", 7: "8", 4: "4"}
    return sum(1 for out in display.output if values.get(len(out)))


def calculate_display_digits(display: Display) -> dict[int, str]:
    length_to_number = {3: 7, 2: 1, 7: 8, 4: 4}

    digits: dict[int, str] = {}
    groupings = {}

    sorted_signals = sorted(display.signals, key=len)
    for key, group in itertools.groupby(sorted_signals, key=len):
        if key in length_to_number:
            digits[length_to_number[key]] = next(group)
        else:
            groupings[key] = [v for v in group]

    digits[2] = [signal for signal in groupings[5] if len(set(digits[4]).difference(set(signal))) == 2][0]
    groupings[5].remove(digits[2])

    digits[3] = [signal for signal in groupings[5] if len(set(digits[2]).difference(set(signal))) == 1][0]
    groupings[5].remove(digits[3])
    digits[5] = groupings[5][0]

    digits[0] = [signal for signal in groupings[6] if len(set(digits[5]).difference(set(signal))) == 1][0]
    groupings[6].remove(digits[0])

    digits[9] = [signal for signal in groupings[6] if len(set(digits[3]).difference(set(signal))) == 0][0]
    groupings[6].remove(digits[9])
    digits[6] = groupings[6][0]

    return digits


def solve_output_with_digits(display: Display, digits_mapping: dict[int, str]) -> int:
    code_to_digit = {str(sorted(v)): k for k, v in digits_mapping.items()}
    return sum(
        [code_to_digit[str(sorted(output))] * position for output, position in zip(display.output, (1000, 100, 10, 1))]
    )


if __name__ == "__main__":
    with open("./input.txt") as f:
        entries = [line.strip().split("|") for line in f.readlines()]

    displays = [Display(tuple(entry[0].strip().split(" ")), tuple(entry[1].strip().split(" "))) for entry in entries]

    print(f"Part One: {sum(find_digits(display) for display in displays)}")
    print(
        f"Part Two: {sum(solve_output_with_digits(display, calculate_display_digits(display)) for display in displays)}"
    )
