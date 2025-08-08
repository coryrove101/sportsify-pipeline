import unittest
from src.web.app import app

class WebAppTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_home_page(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Welcome to March Madness', response.data)

    def test_prediction_page(self):
        response = self.app.get('/predictions')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Predictions', response.data)

    def test_data_endpoint(self):
        response = self.app.get('/data')
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json, dict)

if __name__ == '__main__':
    unittest.main()