from .solution import (
    BingoCard,
    play_bingo_part_one,
    play_bingo_part_two,
    transpose_matrix,
)

# fmt: off
TEST_BALLS = (
    7, 4, 9, 5, 11, 17, 23, 2, 0, 14, 21, 24, 10, 16, 13, 6, 15, 25, 12, 22, 18, 20, 8, 19, 3, 26,
    1)

TEST_CARDS = (
    (
        (22, 13, 17, 11, 0,),
        (8, 2, 23, 4, 24,),
        (21, 9, 14, 16, 7,),
        (6, 10, 3, 18, 5,),
        (1, 12, 20, 15, 19,),
    ), (
        (3, 15, 0, 2, 22,),
        (9, 18, 13, 17, 5,),
        (19, 8, 7, 25, 23,),
        (20, 11, 10, 24, 4,),
        (14, 21, 16, 12, 6,),
    ), (
        (14, 21, 17, 24, 4,),
        (10, 16, 15, 9, 19,),
        (18, 8, 23, 26, 20,),
        (22, 11, 13, 6, 5,),
        (2, 0, 12, 3, 7,),
    )
)


# fmt: on


def test_play_bingo_part_one():
    winning_score = play_bingo_part_one(TEST_BALLS, TEST_CARDS)
    assert winning_score == 4512


def test_play_bingo_part_two():
    winning_score = play_bingo_part_two(TEST_BALLS, TEST_CARDS)
    assert winning_score == 1924


def test_transpose_matrix():
    t = (
        (
            1,
            2,
            3,
        ),
        (
            4,
            5,
            6,
        ),
    )
    exp = ((1, 4), (2, 5), (3, 6))

    assert transpose_matrix(t) == exp


def test_is_a_bingo():
    card = BingoCard(TEST_CARDS[0])
    [
        card.mark_call(call)
        for call in [
            8,
            2,
            23,
            4,
            24,
        ]
    ]
    assert card.is_that_a_bingo() is True

    card = BingoCard(TEST_CARDS[0])
    [
        card.mark_call(call)
        for call in [
            22,
            8,
            21,
            6,
            1,
        ]
    ]
    assert card.is_that_a_bingo() is True


def test_score():
    card = BingoCard(TEST_CARDS[0])
    [
        card.mark_call(call)
        for call in [
            8,
            2,
            23,
            4,
            24,
        ]
    ]
    assert card.score() == 5736
