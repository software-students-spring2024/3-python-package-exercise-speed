import sys
import pathlib
from src.pydancer.songs import listSongs

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
    def test_songs_type(self):
        for param in [None, 'country', 'pop']:
            actual = listSongs(param)
            assert isinstance(
                actual, str
            ), f"Expected listSongs() to return a string. Instead, it returned {actual}"
            assert (
                len(actual) > 0
            ), f"Expected listSongs() not to be empty. Instead, it returned a string with {len(actual)} characters"
    def test_country_param(self):
        actual = listSongs('country')
        assert (
            actual == 'Country Songs:\ncountry song 1\ncountry song 2'
        ), f"Expected the text returned by listSongs('country') to list country songs.  Instead, it returned '{actual}'."
    def test_pop_param(self):
        actual = listSongs('pop')
        assert (
            actual == 'Pop Songs:\npop song 1\npop song 2'
        ), f"Expected the text returned by listSongs('pop') to list pop songs.  Instead, it returned '{actual}'."
    def test_none_param(self):
        actual = listSongs(None)
        assert (
            actual == 'Country Songs:\ncountry song 1\ncountry song 2\nPop Songs:\npop song 1\npop song 2'
        ), f"Expected the text returned by listSongs(None) to list country and pop songs.  Instead, it returned '{actual}'."

