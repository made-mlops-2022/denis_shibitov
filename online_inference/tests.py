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
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), "{'condition': 1}")



#
#
# def test_missed_field_data():
#     request = {
#         'sex': 1,
#         'cp': 0,
#         'trestbps': 160,
#         'chol': 234,
#         'fbs': 1,
#         'restecg': 2,
#         'thalach': 131,
#         'exang': 0,
#         'oldpeak': 0.1,
#         'slope': 1,
#         'ca': 1,
#         'thal': 0,
#     }
#     response = client.post(
#         url='/predict',
#         content=json.dumps(request)
#     )
#     assert response.status_code == 422
#     assert response.json()['detail'][0]['msg'] == 'field required'
#
#
# def test_wrong_numerical_value():
#     request = {
#         'age': 500,
#         'sex': 1,
#         'cp': 0,
#         'trestbps': 160,
#         'chol': 234,
#         'fbs': 1,
#         'restecg': 2,
#         'thalach': 131,
#         'exang': 0,
#         'oldpeak': 0.1,
#         'slope': 1,
#         'ca': 1,
#         'thal': 0,
#     }
#     response = client.post(
#         url='/predict',
#         content=json.dumps(request)
#     )
#     assert response.status_code == 400
#
#
# def test_wrong_literal_value():
#     request = {
#         'age': 69,
#         'sex': 5,
#         'cp': 0,
#         'trestbps': 160,
#         'chol': 234,
#         'fbs': 1,
#         'restecg': 2,
#         'thalach': 131,
#         'exang': 0,
#         'oldpeak': 0.1,
#         'slope': 1,
#         'ca': 1,
#         'thal': 0,
#     }
#     response = client.post(
#         url='/predict',
#         content=json.dumps(request)
#     )
#     assert response.status_code == 422
#     assert response.json()['detail'][0]['msg'] == 'unexpected value; permitted: 0, 1'