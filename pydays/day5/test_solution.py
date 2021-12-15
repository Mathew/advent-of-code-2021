import collections

from .solution import Coordinate, HydrothermalVentMap, Vector, Vent

# fmt: off
VENTS = [
    Vent(Coordinate(0, 9), (Coordinate(5, 9))),
    Vent(Coordinate(8, 0), (Coordinate(0, 8))),
    Vent(Coordinate(9, 4), (Coordinate(3, 4))),
    Vent(Coordinate(2, 2), (Coordinate(2, 1))),
    Vent(Coordinate(7, 0), (Coordinate(7, 4))),
    Vent(Coordinate(6, 4), (Coordinate(2, 0))),
    Vent(Coordinate(0, 9), (Coordinate(2, 9))),
    Vent(Coordinate(3, 4), (Coordinate(1, 4))),
    Vent(Coordinate(0, 0), (Coordinate(8, 8))),
    Vent(Coordinate(5, 5), (Coordinate(8, 2))),
]


# fmt: on


def test_calculate_vector():
    assert Coordinate(4, 5).calculate_vector(Coordinate(1, 5)) == Vector(-3, 0)


def test_plot_vent_horizontal_and_vertical():
    vent_map = HydrothermalVentMap()
    vent_map.plot_vent(VENTS[0])
    vent_map.plot_vent(VENTS[2])
    vent_map.plot_vent(VENTS[3])
    vent_map.plot_vent(VENTS[4])
    vent_map.plot_vent(VENTS[6])

    assert vent_map.map == collections.defaultdict(
        int,
        {
            "0, 9": 2,
            "1, 9": 2,
            "2, 9": 2,
            "3, 9": 1,
            "4, 9": 1,
            "5, 9": 1,
            "9, 4": 1,
            "8, 4": 1,
            "7, 4": 2,
            "6, 4": 1,
            "5, 4": 1,
            "4, 4": 1,
            "3, 4": 1,
            "2, 2": 1,
            "2, 1": 1,
            "7, 0": 1,
            "7, 1": 1,
            "7, 2": 1,
            "7, 3": 1,
        },
    )


def test_plot_vent_diagonal():
    vent_map = HydrothermalVentMap()
    vent_map.plot_vent(Vent(Coordinate(8, 0), (Coordinate(0, 8))))
    assert vent_map.map == collections.defaultdict(
        int,
        {"8, 0": 1, "7, 1": 1, "6, 2": 1, "5, 3": 1, "4, 4": 1, "3, 5": 1, "2, 6": 1, "1, 7": 1, "0, 8": 1},
    )

    vent_map = HydrothermalVentMap()
    vent_map.plot_vent(Vent(Coordinate(1, 1), (Coordinate(3, 3))))
    assert vent_map.map == collections.defaultdict(
        int,
        {"1, 1": 1, "2, 2": 1, "3, 3": 1},
    )

    vent_map = HydrothermalVentMap()
    vent_map.plot_vent(Vent(Coordinate(6, 4), (Coordinate(2, 0))))
    assert vent_map.map == collections.defaultdict(
        int,
        {"6, 4": 1, "5, 3": 1, "4, 2": 1, "3, 1": 1, "2, 0": 1},
    )


def test_number_of_coincidents_horizontal():
    vent_map = HydrothermalVentMap()
    for vent in VENTS:
        vector = vent.calculate_vector()
        if vector.is_horizontal() or vector.is_vertical():
            vent_map.plot_vent(vent)
    assert vent_map.calculate_coincidents() == 5


def test_number_of_coincidents_any():
    vent_map = HydrothermalVentMap()
    for vent in VENTS:
        vent_map.plot_vent(vent)
    assert vent_map.calculate_coincidents() == 12
