from src.pydancer.songs import listSongs

class Tests:
    def test_sanity_check(self):
        expected = True  # the value we expect to be present
        actual = True  # the value we see in reality
        assert actual == expected, "Expected True to be equal to True!"
    def test_songs_type(self):
        for genre in [None, 'country', 'pop']:
            actual = listSongs(genre)
            assert isinstance(
                actual, str
            ), f"Expected listSongs() to return a string. Instead, it returned {actual}"
            assert (
                len(actual) > 0
            ), f"Expected listSongs() not to be empty. Instead, it returned a string with {len(actual)} characters"
    def test_country_arg(self):
        actual = listSongs('country')
        assert (
            actual == 'Country Songs:\ncountry song 1\ncountry song 2'
        ), f"Expected the text returned by listSongs('country') to list country songs.  Instead, it returned '{actual}'."
    def test_pop_arg(self):
        actual = listSongs('pop')
        assert (
            actual == 'Pop Songs:\npop song 1\npop song 2'
        ), f"Expected the text returned by listSongs('pop') to list pop songs.  Instead, it returned '{actual}'."
    def test_none_arg(self):
        actual = listSongs(None)
        assert (
            actual == 'Country Songs:\ncountry song 1\ncountry song 2\nPop Songs:\npop song 1\npop song 2'
        ), f"Expected the text returned by listSongs(None) to list country and pop songs.  Instead, it returned '{actual}'."

