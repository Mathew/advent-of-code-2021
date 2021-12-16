import collections
from typing import Callable, Iterable


def get_cheapest_position(crabs: Iterable[int], fuel_calculator: Callable[[int], int]):
    max_position = max(crabs)
    min_position = min(crabs)

    total_fuel_per_position = collections.defaultdict(int)
    for crab in crabs:
        for pos in range(min_position, max_position):
            total_fuel_per_position[pos] += fuel_calculator(crab - pos)

    position = min(total_fuel_per_position, key=total_fuel_per_position.get)
    return position, total_fuel_per_position[position]


if __name__ == "__main__":
    with open("input.txt") as f:
        crabs = [int(c) for c in f.read().strip().split(",")]

    position, fuel = get_cheapest_position(crabs, fuel_calculator=lambda x: abs(x))

    print(f"Part One; position: {position} fuel: {fuel}")

    position, fuel = get_cheapest_position(crabs, fuel_calculator=lambda x: sum(range(1, abs(x) + 1)))
    print(f"Part One; position: {position} fuel: {fuel}")
