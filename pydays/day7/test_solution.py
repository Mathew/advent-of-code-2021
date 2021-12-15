from .solution import get_cheapest_position

CRABS = (16, 1, 2, 0, 4, 2, 7, 1, 2, 14)


def test_cheapest_positioning():
    assert get_cheapest_position(CRABS) == (2, 37)
