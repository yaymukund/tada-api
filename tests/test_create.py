from flask import json
from tests.helpers import TestTada

class TestCreate(TestTada):

    def api_post(self, url, data):
        data = json.dumps(data)
        return self.app.post(
            url, content_type = 'application/json', data = data
        )

    def test_create_without_task(self):
        data = { 'description': None }
        response = self.api_post('/tasks', data = data)
        body = response.get_data(as_text = True)
        assert response.status_code == 400
        assert 'Description cannot be empty' in body

    def test_create_with_description(self):
        data = { 'task': { 'description': 'Get some milk' }}
        response = self.api_post('/tasks', data = data)
        task = json.loads(response.get_data())['task']

        assert task['description'] == 'Get some milk'
        assert task['position'] == 1
        assert task['created_at']
        assert task['updated_at']
        assert task['completed_at'] is None
        assert task['id']

    def test_create_position(self):
        data = { 'task': { 'description': 'Get some milk' }}
        response = self.api_post('/tasks', data = data)
        task = json.loads(response.get_data())['task']
        assert task['position'] == 1

        data = { 'task': { 'description': 'Get more milk' }}
        response = self.api_post('/tasks', data = data)
        task = json.loads(response.get_data())['task']
        assert task['position'] == 2
