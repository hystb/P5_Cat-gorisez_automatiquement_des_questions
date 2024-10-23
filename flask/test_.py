import unittest
from app import app


class FlaskAppTestCase(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()
        self.client.testing = True

    def test_predict_valid_question(self):
        sample_question = {
            "question": "How do I reverse a list in Python?"
        }
        response = self.client.post('/api/v1/predict', json=sample_question)

        self.assertEqual(response.status_code, 200)

        self.assertIn('tags', response.json)
        self.assertTrue(isinstance(response.json['tags'], list))

    def test_predict_empty_question(self):
        empty_question = {
            "question": ""
        }

        response = self.client.post('/api/v1/predict', json=empty_question)
        self.assertIn(response.status_code, [400, 422])

    def test_predict_invalid_payload(self):
        invalid_payload = {
            "text": "How do I reverse a list in Python?"
        }

        response = self.client.post('/api/v1/predict', json=invalid_payload)

        self.assertIn(response.status_code, [400, 422])

    def test_validate_tags(self):
        sample_tags = {
            "tags": ["python", "list", "reverse"]
        }
        response = self.client.post('/api/v1/validate', json=sample_tags)

        self.assertEqual(response.status_code, 200)

    def test_predict_missing_question_key(self):
        missing_key_payload = {}

        response = self.client.post('/api/v1/predict',
                                    json=missing_key_payload)

        self.assertIn(response.status_code, [400, 422])

    def test_predict_non_string_question(self):
        non_string_question = {
            "question": 12345
        }

        response = self.client.post('/api/v1/predict',
                                    json=non_string_question)

        self.assertIn(response.status_code, [400, 422])

    def test_predict_special_characters_question(self):
        special_characters_question = {
            "question": "@#$%^&*()"
        }

        response = self.client.post('/api/v1/predict',
                                    json=special_characters_question)

        self.assertEqual(response.status_code, 200)

        self.assertIn('tags', response.json)
        self.assertTrue(isinstance(response.json['tags'], list))


if __name__ == '__main__':
    unittest.main()
