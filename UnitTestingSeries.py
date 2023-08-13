import unittest
from callbacksandlayout import app

class TestApp(unittest.TestCase):

    def setUp(self):
        self.app = app.server.test_client()

    def test_home_status_code(self):
        result = self.app.get('/')
        self.assertEqual(result.status_code, 200)

    def test_overs_button(self):
        result = self.app.get('/?overs=1')
        self.assertEqual(result.status_code, 200)

    def test_wickets_button(self):
        result = self.app.get('/?wickets=1')
        self.assertEqual(result.status_code, 200)

    def test_average_button(self):
        result = self.app.get('/?average=1')
        self.assertEqual(result.status_code, 200)

    def test_economy_button(self):
        result = self.app.get('/?economy=1')
        self.assertEqual(result.status_code, 200)

    def test_strike_rate_button(self):
        result = self.app.get('/?strike_rate=1')
        self.assertEqual(result.status_code, 200)

    def test_dot_balls_button(self):
        result = self.app.get('/?dot_balls=1')
        self.assertEqual(result.status_code, 200)

    def test_runs_given_button(self):
        result = self.app.get('/?runs_given=1')
        self.assertEqual(result.status_code, 200)

if __name__ == '__main__':
    unittest.main()
