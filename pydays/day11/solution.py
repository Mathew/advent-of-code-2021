import copy
import typing


class OctopusPosition(typing.NamedTuple):
    x: int
    y: int


def is_valid_position(x: int, y: int, octopi: list[list[int]]) -> bool:
    if y < 0 or y >= len(octopi):
        return False
    if x < 0 or x >= len(octopi[y]):
        return False

    return True


def increase_neighbours(position: OctopusPosition, octopi: list[list[int]]) -> list[OctopusPosition]:
    flashed = []
    for y in range(position.y - 1, position.y + 2):
        for x in range(position.x - 1, position.x + 2):
            if x == position.x and y == position.y:
                continue

            if is_valid_position(x, y, octopi):
                octopi[y][x] += 1
                if octopi[y][x] == 10:
                    flashed.append(OctopusPosition(x, y))

    return flashed


def step(octopuses: list[list[int]]) -> typing.Generator[list[list[int]], None, None]:
    octopi = copy.deepcopy(octopuses)

    while True:
        flashed: list[OctopusPosition] = []
        visited_flashed: list[OctopusPosition] = []
        octopi = [[v + 1 for v in row] for row in octopi]

        for y, row in enumerate(octopi):
            for x, energy in enumerate(row):
                if energy == 10:
                    flashed.append(OctopusPosition(x, y))

        while set(flashed).difference(visited_flashed):
            for f in set(flashed).difference(visited_flashed):
                flashed.extend(increase_neighbours(OctopusPosition(f.x, f.y), octopi))
                visited_flashed.append(f)

        octopi = [[0 if v > 9 else v for v in row] for row in octopi]
        yield octopi, len(flashed)


if __name__ == "__main__":
    with open("./input.txt") as f:
        octopi = []
        for line in f.readlines():
            octopi.append([int(char) for char in line.strip()])

    os = step(octopi)
    print(f"Part One: {sum([(next(os)[1]) for _ in range(100)])}")

    total_octopi = sum([len(row) for row in octopi])
    os = step(octopi)
    num_flashed = 0
    step_count = 0
    while total_octopi != num_flashed:
        num_flashed = next(os)[1]
        step_count += 1

    print(f"Part Two: {step_count}")
