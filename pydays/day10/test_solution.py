from .solution import parse_syntax_line, score_syntax_errors

TEST_LINES = [
    "{([(<{}[<>[]}>{[]{[(<()>",
    "[[<[([]))<([[{}[[()]]]",
    "[{[{({}]{}}([{[{{{}}([]",
    "[<(<(<(<{}))><([]([]()",
    "<{([([[(<>()){}]>(<<{{",
]


def test_parse_syntax_line():
    assert parse_syntax_line("[(()[<>])]({[<{<<[]>>(") == (False, None)
    assert parse_syntax_line("{([(<{}[<>[]}>{[]{[(<()>") == (False, "}")
    assert parse_syntax_line("[[<[([]))<([[{}[[()]]]") == (False, ")")
    assert parse_syntax_line("[{[{({}]{}}([{[{{{}}([]") == (False, "]")
    assert parse_syntax_line("<{([([[(<>()){}]>(<<{{") == (False, ">")


def test_score_syntax_errors():
    assert score_syntax_errors([parse_syntax_line(l) for l in TEST_LINES]) == 26397
