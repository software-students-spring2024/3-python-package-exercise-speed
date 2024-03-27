import argparse
from src.pydancer.options import listOptions

class Tests:
    def test_sanity_check(self):
        expected = True  # the value we expect to be present
        actual = True  # the value we see in reality
        assert actual == expected, "Expected True to be equal to True!"
    def test_options_type(self):
        args = argparse.Namespace()
        for hasChar in [True, False]:
            for hasDiff in [True, False]:
                args.characters = hasChar
                args.difficulties = hasDiff
                actual = listOptions(args)
                assert isinstance(
                    actual, str
                ), f"Expected listOptions() to return a string. Instead, it returned {actual}"
                assert (
                    len(actual) > 0
                ), f"Expected listOptions() not to be empty. Instead, it returned a string with {len(actual)} characters"
    def test_char_difficulties_flag(self):
        args = argparse.Namespace()
        args.characters = True
        args.difficulties = True
        actual = listOptions(args)
        assert (
            actual == 'Characters:\ngirl\nboy\nDifficulties:\neasy\nmedium\nhard'
        ), f"Expected the text returned by listOptions with --characters and --difficulties to list both characters and difficulties.  Instead, it returned '{actual}'."
    def test_char_flag(self):
        args = argparse.Namespace()
        args.characters = True
        args.difficulties = False
        actual = listOptions(args)
        assert (
            actual == 'Characters:\ngirl\nboy'
        ), f"Expected the text returned by listOptions with only --characters to list only characters.  Instead, it returned '{actual}'."
    def test_difficulties_flag(self):
        args = argparse.Namespace()
        args.characters = False
        args.difficulties = True
        actual = listOptions(args)
        assert (
            actual == 'Difficulties:\neasy\nmedium\nhard'
        ), f"Expected the text returned by listOptions with only --difficulties to list only difficultiess.  Instead, it returned '{actual}'."
    def test_no_flags(self):
        args = argparse.Namespace()
        args.characters = False
        args.difficulties = False
        actual = listOptions(args)
        assert (
            actual == 'Characters:\ngirl\nboy\nDifficulties:\neasy\nmedium\nhard'
        ), f"Expected the text returned by listOptions with no flags to list both characters and difficulties.  Instead, it returned '{actual}'."