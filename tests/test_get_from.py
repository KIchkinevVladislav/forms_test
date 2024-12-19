import unittest
from unittest.mock import patch

from fastapi.testclient import TestClient

from main import app
from database.mongo import get_mongo_db, get_mongo_client


class TestGetFormAPI(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.mongo_client = get_mongo_client()
        cls.db = get_mongo_db()

        cls.patcher = patch("database.mongo.get_mongo_client", return_value=cls.mongo_client)
        cls.patcher.start()

        cls.client = TestClient(app)

        cls.test_form = {
            "name": "Test Form",
            "f_name1": "text",
            "f_name2": "email",
            "f_name3": "phone",
            "f_name4": "date"
        }
        cls.db.forms.insert_one(cls.test_form)

    @classmethod
    def tearDownClass(cls):
        cls.db.forms.delete_one(cls.test_form)
        cls.patcher.stop()

        cls.mongo_client.close()

    def test_get_form_success(self):
        data = {
            "f_name1": "Ivan",
            "f_name2": "ivan@mail.ru",
            "f_name3": "+79819667979",
            "f_name4": "01.01.2024" 
        }

        response = self.client.post("/get_form", data=data)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), "Test Form")

    def test_get_form_no_match(self):
        data = {
            "f_name1": "Ivan",
            "f_name2": "ivan@mail.ru",
            "f_name3": "+79819667979",
            "f_name4": "01.01.2024",
            "f_name5": "2024-01-01",
        }

        correct_response_data = {
            "f_name1": "TEXT",
            "f_name2": "EMAIL",
            "f_name3": "PHONE",
            "f_name4": "DATE",
            "f_name5": "DATE",
        }

        response = self.client.post("/get_form", data=data)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), correct_response_data)
