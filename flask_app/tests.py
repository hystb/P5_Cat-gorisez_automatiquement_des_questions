import unittest
from app import app


class FlaskAppTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.client = app.test_client()
        app.config['TESTING'] = True

    def test_health_route(self):
        response = self.client.get('/health')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'{"status":"healthy"}\n', response.data)

    def test_prediction_route(self):
        response = self.client.post('/api/v1/predict',
                                    json={"question": "Sample question"})
        self.assertEqual(response.status_code, 200)
        self.assertIn('tag', response.get_json()[0])


if __name__ == "__main__":
    unittest.main()
