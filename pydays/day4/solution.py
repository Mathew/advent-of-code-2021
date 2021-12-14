import itertools
from typing import Any, Iterable, Sequence

from input import CALLS, BINGO_CARDS


class BingoCard:
    _card: tuple[tuple[int]]
    _marked_calls: list[int]
    _numbers: list[int]
    _lines: tuple[tuple[int, ...]]

    def __init__(self, card: tuple[tuple[int, ...]]):
        self._card = card
        self._lines = card + transpose_matrix(card)
        self._marked_calls = []
        self._numbers = list(itertools.chain.from_iterable(card))

    def mark_call(self, call: int):
        for line in self._lines:
            if call in line:
                self._marked_calls.append(call)
                break

    def is_that_a_bingo(self) -> bool:
        if len(self._marked_calls) > 4:
            for line in self._lines:
                if set(line).issubset(self._marked_calls):
                    return True
        return False

    def score(self) -> int:
        if self.is_that_a_bingo():
            unmarked = set(self._numbers).difference(self._marked_calls)
            return sum(unmarked) * self._marked_calls[-1]
        return 0


def transpose_matrix(matrix: Sequence[Sequence[Any]]) -> tuple[tuple[Any, ...]]:
    l = [r for r in zip(*matrix)]
    return tuple(l)


def play_bingo_part_one(calls: Iterable[int], bingo_cards: tuple[tuple[tuple[int, ...]]]) -> int:
    cards = [BingoCard(card) for card in bingo_cards]
    for call in calls:
        for card in cards:
            card.mark_call(call)
            if card.is_that_a_bingo():
                return card.score()


def play_bingo_part_two(calls: Iterable[int], bingo_cards: tuple[tuple[tuple[int, ...]]]) -> int:
    cards = [BingoCard(card) for card in bingo_cards]
    last_winning_card: BingoCard = None

    cards_in_play = cards
    for call in calls:
        losing_cards = []
        for card in cards_in_play:
            card.mark_call(call)
            if card.is_that_a_bingo():
                last_winning_card = card
            else:
                losing_cards.append(card)
        cards_in_play = losing_cards

    return last_winning_card.score()


if __name__ == "__main__":
    print(f'Part 1: Winning Bingo Score: {play_bingo_part_one(CALLS, BINGO_CARDS)}')
    print(f'Part 2: Last Winning Bingo Score: {play_bingo_part_two(CALLS, BINGO_CARDS)}')
