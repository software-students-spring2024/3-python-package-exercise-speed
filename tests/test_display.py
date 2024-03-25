import argparse
from src.pydancer.display import listDisplay

class Tests:

    def test_sanity_check(self):
        """
        Test debugging... making sure that we can run a simple test that always passes.
        Note the use of the example_fixture in the parameter list - any setup and teardown in that fixture will be run before and after this test function executes
        From the main project directory, run the `python3 -m pytest` command to run all tests.
        """
        expected = True  # the value we expect to be present
        actual = True  # the value we see in reality
        assert actual == expected, "Expected True to be equal to True!"
    def test_display_type(self):
        args = argparse.Namespace()
        for hasChar in [True, False]:
            for hasTheme in [True, False]:
                args.characters = hasChar
                args.themes = hasTheme
                actual = listDisplay(args)
                assert isinstance(
                    actual, str
                ), f"Expected listDisplay() to return a string. Instead, it returned {actual}"
                assert (
                    len(actual) > 0
                ), f"Expected listDisplay() not to be empty. Instead, it returned a string with {len(actual)} characters"
    def test_char_theme_flag(self):
        args = argparse.Namespace()
        args.characters = True
        args.themes = True
        actual = listDisplay(args)
        assert (
            actual == 'Characters:\ngirl character\nboy character\nThemes:\npink\nblue'
        ), f"Expected the text returned by listDisplay with --characters and --themes to list both characters and themes.  Instead, it returned '{actual}'."
    def test_char_flag(self):
        args = argparse.Namespace()
        args.characters = True
        args.themes = False
        actual = listDisplay(args)
        assert (
            actual == 'Characters:\ngirl character\nboy character'
        ), f"Expected the text returned by listDisplay with --characters to list only characters.  Instead, it returned '{actual}'."
    def test_theme_flag(self):
        args = argparse.Namespace()
        args.characters = False
        args.themes = True
        actual = listDisplay(args)
        assert (
            actual == 'Themes:\npink\nblue'
        ), f"Expected the text returned by listDisplay with --characters to list only themes.  Instead, it returned '{actual}'."
    def test_no_flags(self):
        args = argparse.Namespace()
        args.characters = False
        args.themes = False
        actual = listDisplay(args)
        assert (
            actual == 'Characters:\ngirl character\nboy character\nThemes:\npink\nblue'
        ), f"Expected the text returned by listDisplay with no flags to list both characters and themes.  Instead, it returned '{actual}'."