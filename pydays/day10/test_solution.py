from .solution import (
    INCOMPLETE_STATE,
    INVALID_STATE,
    parse_syntax_line,
    score_incomplete_syntax_errors,
    score_invalid_syntax_errors,
)

TEST_LINES = [
    "[({(<(())[]>[[{[]{<()<>>",
    "[(()[<>])]({[<{<<[]>>(",
    "{([(<{}[<>[]}>{[]{[(<()>",
    "(((({<>}<{<{<>}{[]{[]{}",
    "[[<[([]))<([[{}[[()]]]",
    "[{[{({}]{}}([{[{{{}}([]",
    "{<[[]]>}<{[{[{[]{()[[[]",
    "[<(<(<(<{}))><([]([]()",
    "<{([([[(<>()){}]>(<<{{",
    "<{([{{}}[<[[[<>{}]]]>[]]",
]


def test_parse_syntax_line():
    assert parse_syntax_line("[(()[<>])]({[<{<<[]>>(") == (INCOMPLETE_STATE, ")}>]})")
    assert parse_syntax_line("{([(<{}[<>[]}>{[]{[(<()>") == (INVALID_STATE, "}")
    assert parse_syntax_line("[[<[([]))<([[{}[[()]]]") == (INVALID_STATE, ")")
    assert parse_syntax_line("[{[{({}]{}}([{[{{{}}([]") == (INVALID_STATE, "]")
    assert parse_syntax_line("<{([([[(<>()){}]>(<<{{") == (INVALID_STATE, ">")


def test_invalid_score_syntax_errors():
    assert score_invalid_syntax_errors([parse_syntax_line(l) for l in TEST_LINES]) == 26397


def test_incomplete_score_syntax_errors():
    assert score_incomplete_syntax_errors([parse_syntax_line(l) for l in TEST_LINES]) == 288957
