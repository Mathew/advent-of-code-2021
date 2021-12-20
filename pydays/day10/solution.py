from queue import LifoQueue

VALID_SYNTAX = {
    "(": ")",
    "[": "]",
    "{": "}",
    "<": ">",
}
INVALID_SYNTAX_SCORES = {")": 3, "]": 57, "}": 1197, ">": 25137, None: 0}
INCOMPLETE_SYNTAX_SCORES = {
    ")": 1,
    "]": 2,
    "}": 3,
    ">": 4,
}
INVALID_STATE = "INVALID"
INCOMPLETE_STATE = "INCOMPLETE"


def parse_syntax_line(line: str) -> (bool, str):
    queue: LifoQueue[str] = LifoQueue()
    for c in line:
        if c in VALID_SYNTAX.keys():
            queue.put(VALID_SYNTAX[c])
        else:
            if c != queue.get():
                return INVALID_STATE, c

    chars = ""
    while not queue.empty():
        chars += queue.get()

    return INCOMPLETE_STATE, "".join(chars)


def score_invalid_syntax_errors(results: list[(str, str)]) -> int:
    return sum(INVALID_SYNTAX_SCORES[result[1]] for result in results if result[0] == INVALID_STATE)


def score_incomplete_syntax_errors(results: list[(str, str)]) -> int:
    scores = []
    for result in results:
        if result[0] == INCOMPLETE_STATE:
            score = 0
            for c in result[1]:
                score = (score * 5) + INCOMPLETE_SYNTAX_SCORES[c]
            scores.append(score)

    scores.sort()
    return scores[int((len(scores) - 1) / 2)]


if __name__ == "__main__":
    with open("./input.txt") as f:
        lines = [line.strip() for line in f.readlines()]

    results = [parse_syntax_line(l) for l in lines]
    print(f"Part One: {score_invalid_syntax_errors(results)}")
    print(f"Part Two: {score_incomplete_syntax_errors(results)}")
