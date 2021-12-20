from queue import LifoQueue

VALID_SYNTAX = {
    "(": ")",
    "[": "]",
    "{": "}",
    "<": ">",
}
INVALID_SYNTAX_SCORES = {")": 3, "]": 57, "}": 1197, ">": 25137, None: 0}


def parse_syntax_line(line: str) -> (bool, str):
    queue: LifoQueue[str] = LifoQueue()
    for c in line:
        if c in VALID_SYNTAX.keys():
            queue.put(VALID_SYNTAX[c])
        else:
            if c != queue.get():
                return False, c

    return queue.qsize() == 0, None


def score_syntax_errors(results: list[(bool, str)]) -> int:
    return sum(INVALID_SYNTAX_SCORES[result[1]] for result in results if result[0] is False)


if __name__ == "__main__":
    with open("./input.txt") as f:
        lines = [line.strip() for line in f.readlines()]

    results = [parse_syntax_line(l) for l in lines]
    print(f"Part One: {score_syntax_errors(results)}")
