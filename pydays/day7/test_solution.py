from .solution import get_cheapest_position

CRABS = (16, 1, 2, 0, 4, 2, 7, 1, 2, 14)


def test_cheapest_positioning():
    assert get_cheapest_position(CRABS, lambda x: abs(x)) == (2, 37)


def test_cheapest_positioning_expensive_fuel():
    assert get_cheapest_position(CRABS, lambda x: sum(range(1, abs(x) + 1))) == (5, 168)
