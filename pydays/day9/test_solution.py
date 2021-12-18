from .solution import get_lowest_points

# fmt: off
CAVES_HEIGHTS = [
    [2, 1, 9, 9, 9, 4, 3, 2, 1, 0,],
    [3, 9, 8, 7, 8, 9, 4, 9, 2, 1,],
    [9, 8, 5, 6, 7, 8, 9, 8, 9, 2,],
    [8, 7, 6, 7, 8, 9, 6, 7, 8, 9,],
    [9, 8, 9, 9, 9, 6, 5, 6, 7, 8,],
]


# fmt: on
def test_get_lowest_points():
    assert get_lowest_points(CAVES_HEIGHTS) == [2, 1, 6, 6]
