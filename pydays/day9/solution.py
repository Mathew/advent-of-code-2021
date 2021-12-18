from typing import Any


def get(l: list, index: int) -> Any:
    if index < 0:
        return None
    try:
        return l[index]
    except IndexError:
        return None


def get_lowest_points(cave_map: list[list[int]]) -> list[int]:
    lowest_points = []
    for y_pos, caves in enumerate(cave_map):
        for x_pos, cave in enumerate(caves):
            surrounding_caves = [
                v
                for v in [
                    get(get(cave_map, y_pos + 1), x_pos) if get(cave_map, y_pos + 1) is not None else None,
                    get(get(cave_map, y_pos - 1), x_pos) if get(cave_map, y_pos - 1) is not None else None,
                    get(get(cave_map, y_pos), x_pos + 1) if get(cave_map, y_pos) is not None else None,
                    get(get(cave_map, y_pos), x_pos - 1) if get(cave_map, y_pos) is not None else None,
                ]
                if v is not None
            ]

            if min(surrounding_caves) > cave:
                lowest_points.append(cave + 1)

    return lowest_points


if __name__ == "__main__":
    with open("./input.txt") as f:
        cave_map = []
        for line in f.readlines():
            cave_map.append([int(char) for char in line.strip()])

    print(f"Part One: {sum(get_lowest_points(cave_map))}")
