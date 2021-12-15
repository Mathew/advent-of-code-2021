from .solution import efficient_fish_spawn, fish_spawn

FISH = [3, 4, 3, 1, 2]


def test_fish_spawn():
    fish_gen = fish_spawn(FISH)
    assert next(fish_gen) == [2, 3, 2, 0, 1]
    assert next(fish_gen) == [1, 2, 1, 6, 0, 8]


def test_fish_spawn_days():
    fish_gen = fish_spawn(FISH)

    result = []
    for _ in range(80):
        result = next(fish_gen)

    assert len(result) == 5934


def test_efficient_fish_spawn():
    fish_gen = efficient_fish_spawn(FISH)
    assert next(fish_gen) == {2: 2, 3: 1, 0: 1, 1: 1}
    assert next(fish_gen) == {1: 2, 2: 1, 6: 1, 8: 1, 0: 1}


def test_efficient_fish_spawn_days():
    fish_gen = efficient_fish_spawn(FISH)

    result = []
    for _ in range(80):
        result = next(fish_gen)

    print(result.items())

    assert sum(result.values()) == 5934
