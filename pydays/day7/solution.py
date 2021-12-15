import collections
from typing import Iterable


def get_cheapest_position(crabs: Iterable[int]):
    max_position = max(crabs)
    min_position = min(crabs)

    total_fuel_per_position = collections.defaultdict(int)
    for crab in crabs:
        for pos in range(min_position, max_position):
            total_fuel_per_position[pos] += abs(crab - pos)

    position = min(total_fuel_per_position, key=total_fuel_per_position.get)
    return position, total_fuel_per_position[position]


if __name__ == "__main__":
    with open("input.txt") as f:
        crabs = [int(c) for c in f.read().strip().split(",")]

    position, fuel = get_cheapest_position(crabs)

    print(f"Part One; position: {position} fuel: {fuel}")
