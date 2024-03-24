import sys
import pathlib
sys.path.append(f"{pathlib.Path(__file__).parent.resolve()}/../src")
from pydancer.__main__ import *

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
        #just should test the Songs.py file, not the main function
        assert True
