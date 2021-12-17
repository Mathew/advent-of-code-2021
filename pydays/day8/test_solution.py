from .solution import Display, find_digits

ENTRIES = (
    Display(
        (
            "be",
            "cfbegad",
            "cbdgef",
            "fgaecd",
            "cgeb",
            "fdcge",
            "agebfd",
            "fecdb",
            "fabcd",
            "edb",
        ),
        ("fdgacbe", "cefdb", "cefbgd", "gcbe"),
    ),
    Display(
        (
            "edbfga",
            "begcd",
            "cbg",
            "gc",
            "gcadebf",
            "fbgde",
            "acbgfd",
            "abcde",
            "gfcbed",
            "gfec",
        ),
        ("fcgedb", "cgb", "dgebacf", "gc"),
    ),
    Display(
        (
            "fgaebd",
            "cg",
            "bdaec",
            "gdafb",
            "agbcfd",
            "gdcbef",
            "bgcad",
            "gfac",
            "gcb",
            "cdgabef",
        ),
        ("cg", "cg", "fdcagb", "cbg"),
    ),
    Display(
        (
            "fbegcd",
            "cbd",
            "adcefb",
            "dageb",
            "afcb",
            "bc",
            "aefdc",
            "ecdab",
            "fgdeca",
            "fcdbega",
        ),
        ("efabcd", "cedba", "gadfec", "cb"),
    ),
    Display(
        (
            "aecbfdg",
            "fbg",
            "gf",
            "bafeg",
            "dbefa",
            "fcge",
            "gcbea",
            "fcaegb",
            "dgceab",
            "fcbdga",
        ),
        ("gecf", "egdcabf", "bgf", "bfgea"),
    ),
    Display(
        (
            "fgeab",
            "ca",
            "afcebg",
            "bdacfeg",
            "cfaedg",
            "gcfdb",
            "baec",
            "bfadeg",
            "bafgc",
            "acf",
        ),
        ("gebdcfa", "ecba", "ca", "fadegcb"),
    ),
    Display(
        (
            "dbcfg",
            "fgd",
            "bdegcaf",
            "fgec",
            "aegbdf",
            "ecdfab",
            "fbedc",
            "dacgb",
            "gdcebf",
            "gf",
        ),
        ("cefg", "dcbef", "fcge", "gbcadfe"),
    ),
    Display(
        (
            "bdfegc",
            "cbegaf",
            "gecbf",
            "dfcage",
            "bdacg",
            "ed",
            "bedf",
            "ced",
            "adcbefg",
            "gebcd",
        ),
        ("ed", "bcgafe", "cdgba", "cbgef"),
    ),
    Display(
        (
            "egadfb",
            "cdbfeg",
            "cegd",
            "fecab",
            "cgb",
            "gbdefca",
            "cg",
            "fgcdab",
            "egfdb",
            "bfceg",
        ),
        ("gbdfcae", "bgc", "cg", "cgb"),
    ),
    Display(
        (
            "gcafb",
            "gcf",
            "dcaebfg",
            "ecagb",
            "gf",
            "abcdeg",
            "gaef",
            "cafbge",
            "fdbac",
            "fegbdc",
        ),
        ("fgae", "cfgab", "fg", "bagce"),
    ),
)


def test_find_digits():
    assert find_digits(ENTRIES[1]) == 3
