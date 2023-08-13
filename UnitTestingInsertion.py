# importing necessary modules
import unittest
from unittest.mock import MagicMock
from callbacksforinsert import app, update_data

# Defining test case class
class TestApp(unittest.TestCase):

    # Defining the setUp method to set up the test environment
    def setUp(self):
        self.app = app.server.test_client()


    # Defining the tearDown method to tear down the test environment
    def tearDown(self):
        pass

    # Defining test_update_data method to test the update_data function
    def test_update_data(self):
        # define dummy input values
        player = "THISARA PERERA"
        matches = "10"
        wickets = "5"
        runs = "13"
        type = "Seam"
        role = "Main Bowler"
        table_data = []

        # Calling the update_data function with the dummy input values
        result = update_data(1, player, matches, wickets, runs, type, role, table_data)

        # Asserting that the function returns the expected output
        expected_output =None
        self.assertEqual(result, expected_output)

# Running the unit tests
if __name__ == '__main__':
    unittest.main()
