from src.pydancer.howto import printHowTo

class Tests:
    def test_sanity_check(self):
        expected = True  # the value we expect to be present
        actual = True  # the value we see in reality
        assert actual == expected, "Expected True to be equal to True!"
    def test_songs_type(self):
        for long in [True, False]:
            actual = printHowTo(long)
            assert isinstance(
                actual, str
            ), f"Expected printHowTo() to return a string. Instead, it returned {actual}"
            assert (
                len(actual) > 0
            ), f"Expected printHowTo() not to be empty. Instead, it returned a string with {len(actual)} characters"
    def test_long_true_arg(self):
        actual = printHowTo(True)
        assert (
            actual == 'This is such an awesome game! Play with Up, Down, Left, Right arrows.'
        ), f"Expected the text returned by printHowTo(True) to list the long how-to guide.  Instead, it returned '{actual}'."
    def test_long_false_arg(self):
        actual = printHowTo(False)
        assert (
            actual == 'awesome game, use arrows.'
        ), f"Expected the text returned by printHowTo(False) to list the short how-to guide.  Instead, it returned '{actual}'."
 