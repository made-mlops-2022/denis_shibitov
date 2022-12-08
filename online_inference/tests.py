import json
import unittest
from fastapi.testclient import TestClient
from app import app, load_model


class AppTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.client = TestClient(app)
        load_model()

    def test_health_ok(self):
        response = self.client.get('/health')
        assert response.status_code == 200

    def test_predict_negative(self):
        request = {
            'age': 52,
            'sex': 0,
            'cp': 0,
            'trestbps': 150,
            'chol': 242,
            'fbs': 1,
            'restecg': 2,
            'thalach': 121,
            'exang': 0,
            'oldpeak': 0.15,
            'slope': 1,
            'ca': 1,
            'thal': 0
        }
        response = self.client.post(
            url='/predict',
            content=json.dumps(request)
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), "{'condition': 0}")

    def test_predict_positive(self):
        request = {
            'age': 49,
            'sex': 1,
            'cp': 2,
            'trestbps': 120,
            'chol': 188,
            'fbs': 0,
            'restecg': 0,
            'thalach': 139,
            'exang': 0,
            'oldpeak': 2.0,
            'slope': 1,
            'ca': 3,
            'thal': 2
        }
        response = self.client.post(
            url='/predict',
            content=json.dumps(request)
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), "{'condition': 1}")

    def test_wrong_sex_value_400(self):
        request = {
            'age': 49,
            'sex': 4,
            'cp': 2,
            'trestbps': 118,
            'chol': 149,
            'fbs': 0,
            'restecg': 126,
            'thalach': 0,
            'exang': 0.8,
            'oldpeak': 0,
            'slope': 3,
            'ca': 0,
            'thal': 1
        }
        response = self.client.post(
            url='/predict',
            content=json.dumps(request)
        )
        self.assertEqual(response.status_code, 400)
