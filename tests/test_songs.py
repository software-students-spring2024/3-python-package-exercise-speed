from src.pydancer.songs import listSongs

class Tests:
    def test_sanity_check(self):
        expected = True  # the value we expect to be present
        actual = True  # the value we see in reality
        assert actual == expected, "Expected True to be equal to True!"
    def test_songs_type(self):
        for genre in [None, 'rock', 'house']:
            actual = listSongs(genre)
            assert isinstance(
                actual, str
            ), f"Expected listSongs() to return a string. Instead, it returned {actual}"
            assert (
                len(actual) > 0
            ), f"Expected listSongs() not to be empty. Instead, it returned a string with {len(actual)} characters"
    def test_rock_arg(self):
        actual = listSongs('rock')
        assert (
            actual == 'Rock Songs:\n Blood And Steel'
        ), f"Expected the text returned by listSongs('rock') to list rock songs.  Instead, it returned '{actual}'."
    def test_house_arg(self):
        actual = listSongs('house')
        assert (
            actual == 'House Songs:\nTwo In The Rain'
        ), f"Expected the text returned by listSongs('house') to list house songs.  Instead, it returned '{actual}'."
    def test_none_arg(self):
        actual = listSongs(None)
        assert (
            actual == 'Rock Songs:\nBlood And Steel \nHouse Songs:\nTwo In The Rain'
        ), f"Expected the text returned by listSongs(None) to list all songs.  Instead, it returned '{actual}'."

