import collections
from typing import Generator, Iterable


def fish_spawn(fish: Iterable[int]) -> Generator[list[int], None, None]:
    fishes = [f for f in fish]
    while True:
        for ptr in range(len(fishes)):
            if fishes[ptr] == 0:
                fishes[ptr] = 6
                fishes.append(8)
            else:
                fishes[ptr] -= 1

        yield fishes


def efficient_fish_spawn(fish: Iterable[int]) -> Generator[dict[int, int], None, None]:
    fishes = collections.defaultdict(int)
    for f in fish:
        fishes[f] += 1

    while True:
        fish_counts = collections.defaultdict(int)
        for days_alive, num_fishes in fishes.items():
            if days_alive == 0:
                fish_counts[6] += num_fishes
                fish_counts[8] += num_fishes
            else:
                fish_counts[days_alive - 1] += num_fishes

        fishes = fish_counts
        yield fishes


if __name__ == "__main__":
    with open("./input.txt") as f:
        str_fish = f.read().strip().split(",")
    int_fish = [int(f) for f in str_fish]

    SUNUPSUNDOWN = fish_spawn(int_fish)

    result = []
    for _ in range(80):
        result = next(SUNUPSUNDOWN)

    print(f"Part One: {len(result)}")

    IMGONNAEATYOULITTLEFISHY = efficient_fish_spawn(int_fish)
    for _ in range(256):
        result = next(IMGONNAEATYOULITTLEFISHY)

    print(f"Part Two: {sum(result.values())}")
