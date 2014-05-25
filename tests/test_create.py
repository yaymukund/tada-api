from flask import json
from tests.helpers import TestTada

class TestCreate(TestTada):

    def test_create_without_description(self):
        data = { 'description': None }
        response = self.app.post('/tasks', data = data)
        body = response.get_data(as_text = True)
        assert response.status_code == 400
        assert 'Description cannot be empty' in body

    def test_create_with_description(self):
        data = { 'description': 'Get some milk' }
        response = self.app.post('/tasks', data = data)
        task = json.loads(response.get_data())['task']

        assert task['description'] == 'Get some milk'
        assert task['rank'] == 1
        assert task['created_at']
        assert task['updated_at']
        assert task['completed_at'] is None
        assert task['id']

    def test_create_rank(self):
        data = { 'description': 'Get some milk' }
        response = self.app.post('/tasks', data = data)
        task = json.loads(response.get_data())['task']
        assert task['rank'] == 1

        data = { 'description': 'Get more milk' }
        response = self.app.post('/tasks', data = data)
        task = json.loads(response.get_data())['task']
        assert task['rank'] == 2
