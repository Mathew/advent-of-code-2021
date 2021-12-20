import math
from queue import Queue
from typing import Any, NamedTuple


def get(l: list, index: int) -> Any:
    if index < 0:
        return None
    try:
        return l[index]
    except IndexError:
        return None


class Cave(NamedTuple):
    x: int
    y: int
    height: int


class CaveSystem:
    _lowest_points: list[Cave]
    _caves: list[list[int]]

    def __init__(self, caves: list[list[int]]):
        self._caves = caves
        self._lowest_points = []

    def discover_adjacent(self, cave: Cave) -> list[Cave]:
        coords = [(cave.x, cave.y + 1), (cave.x, cave.y - 1), (cave.x + 1, cave.y), (cave.x - 1, cave.y)]
        adjacent_caves = []

        for pair in coords:
            cave = Cave(
                pair[0],
                pair[1],
                get(get(self._caves, pair[1]), pair[0]) if get(self._caves, pair[1]) is not None else None,
            )

            if cave.height is not None:
                adjacent_caves.append(cave)

        return adjacent_caves

    def get_lowest_points(self) -> list[Cave]:
        lowest_points = []
        for y_pos, caves in enumerate(self._caves):
            for x_pos, cave in enumerate(caves):
                cave = Cave(x_pos, y_pos, cave)
                adjacent_caves = self.discover_adjacent(cave)

                if min([c.height for c in adjacent_caves]) > cave.height:
                    lowest_points.append(cave)

        self._lowest_points = lowest_points
        return self._lowest_points


class BFS:
    _start: Cave
    _cave_system: CaveSystem
    _queue: Queue[Cave]
    _visited = list[(int, int)]

    def __init__(self, cave_system: CaveSystem, start: Cave):
        self._start: Cave = start
        self._visited: list[Cave] = []
        self._queue: Queue[Cave] = Queue()
        self._queue.put(self._start)
        self._cave_system: CaveSystem = cave_system

    def add_edge(self, node: Cave):
        if node not in self._visited:
            self._queue.put(node)

    @property
    def is_empty(self) -> bool:
        return self._queue.empty()

    @property
    def visited(self) -> list[Cave]:
        return self._visited

    def traverse(self):
        if self.is_empty:
            return []

        current_node = self._queue.get()
        if current_node in self._visited:
            return

        self._visited.append(current_node)

        adjacents = [
            cave
            for cave in self._cave_system.discover_adjacent(current_node)
            if cave.height > current_node.height and cave.height != 9
        ]
        [self.add_edge(adjacent) for adjacent in adjacents]


if __name__ == "__main__":
    with open("./input.txt") as f:
        cave_map = []
        for line in f.readlines():
            cave_map.append([int(char) for char in line.strip()])

    cave_system = CaveSystem(cave_map)
    print(f"Part One: {sum(cave.height + 1 for cave in cave_system.get_lowest_points())}")

    largest_basin_sizes = [0, 0, 0]
    for lowest_point in cave_system.get_lowest_points():
        breadth_first_search = BFS(cave_system, lowest_point)
        while not breadth_first_search.is_empty:
            breadth_first_search.traverse()

        if len(breadth_first_search.visited) > min(largest_basin_sizes):
            largest_basin_sizes.append(len(breadth_first_search.visited))
            if len(largest_basin_sizes) > 3:
                largest_basin_sizes.remove(min(largest_basin_sizes))

    print(f"Part Two: {math.prod(largest_basin_sizes)}")
