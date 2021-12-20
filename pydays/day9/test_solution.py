from .solution import BFS, Cave, CaveSystem

# fmt: off
CAVES_HEIGHTS = [
    [2, 1, 9, 9, 9, 4, 3, 2, 1, 0, ],
    [3, 9, 8, 7, 8, 9, 4, 9, 2, 1, ],
    [9, 8, 5, 6, 7, 8, 9, 8, 9, 2, ],
    [8, 7, 6, 7, 8, 9, 6, 7, 8, 9, ],
    [9, 8, 9, 9, 9, 6, 5, 6, 7, 8, ],
]


# fmt: on
def test_get_lowest_points():
    assert CaveSystem(CAVES_HEIGHTS).get_lowest_points() == [
        Cave(x=1, y=0, height=1),
        Cave(x=9, y=0, height=0),
        Cave(x=2, y=2, height=5),
        Cave(x=6, y=4, height=5),
    ]


def test_cave_pools():
    search = BFS(CaveSystem(CAVES_HEIGHTS), Cave(x=1, y=0, height=1))
    while not search.is_empty:
        search.traverse()

    assert search.visited == [Cave(x=1, y=0, height=1), Cave(x=0, y=0, height=2), Cave(x=0, y=1, height=3)]

    search = BFS(CaveSystem(CAVES_HEIGHTS), Cave(x=9, y=0, height=0))

    while not search.is_empty:
        search.traverse()

    assert len(search.visited) == 9
