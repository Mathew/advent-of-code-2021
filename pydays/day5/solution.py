import collections
import math


class Vector:
    x: int
    y: int

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return (
            self.x == other.x
            and self.y == other.y
            and self.direction_x == other.direction_x
            and self.direction_y == other.direction_y
        )

    def __repr__(self):
        return f"{self.__dict__.items()}"

    def magnitude(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def is_horizontal(self) -> bool:
        return self.x == 0

    def is_vertical(self) -> bool:
        return self.y == 0

    @property
    def direction_x(self) -> int:
        return -1 if self.x < 0 else 1

    @property
    def direction_y(self) -> int:
        return -1 if self.y < 0 else 1


class Coordinate:
    x: int
    y: int

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def calculate_vector(self, terminus: "Coordinate") -> Vector:
        return Vector(terminus.x - self.x, terminus.y - self.y)


class Vent:
    start: Coordinate
    end: Coordinate

    def __init__(self, start: Coordinate, end: Coordinate):
        self.start = start
        self.end = end

    def calculate_vector(self) -> Vector:
        return self.start.calculate_vector(self.end)


class HydrothermalVentMap:
    map: dict[str, int]

    def __init__(self):
        self.map = collections.defaultdict(int)

    def plot_vent(self, vent: Vent):
        vector = vent.calculate_vector()

        if vector.is_horizontal() or vector.is_vertical():
            for x in range(vent.start.x, vent.end.x + vector.direction_x, vector.direction_x):
                for y in range(vent.start.y, vent.end.y + vector.direction_y, vector.direction_y):
                    self.map[f"{x}, {y}"] += 1

    def calculate_coincidents(self) -> int:
        return len({k: v for k, v in self.map.items() if v > 1})


if __name__ == "__main__":
    with open("./input.txt") as f:
        vents = []
        for line in f.readlines():
            line = line.strip().split(" -> ")
            vents.append(
                Vent(
                    Coordinate(*(int(x) for x in line[0].split(","))),
                    Coordinate(*(int(x) for x in line[1].split(","))),
                )
            )

        vent_map = HydrothermalVentMap()
        [vent_map.plot_vent(v) for v in vents]
        print(f"Part One: {vent_map.calculate_coincidents()}")
