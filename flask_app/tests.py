import unittest
from flask_app.app import app


class FlaskAppTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.client = app.test_client()
        app.config['TESTING'] = True

    def test_home_route(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Expected content', response.data)

    def test_prediction_route(self):
        response = self.client.post('/predict',
                                    json={"question": "Sample question"})
        self.assertEqual(response.status_code, 200)
        self.assertIn('tags', response.get_json())


if __name__ == "__main__":
    unittest.main()
