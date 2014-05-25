from flask import json
from tests.helpers import TestTada

class TestIndex(TestTada):

    def test_empty_index(self):
        response = self.app.get('/tasks')
        assert response.status_code == 200

        data = json.loads(response.get_data())
        assert not data['tasks']

    def test_1_task_index(self):
        self.make_task(description = 'Get some milk', rank = 0)
        response = self.app.get('/tasks')

        tasks = json.loads(response.get_data())['tasks']
        assert len(tasks) == 1
        assert tasks[0]['description'] == 'Get some milk'
        assert tasks[0]['rank'] == 0
        assert tasks[0]['created_at']
        assert tasks[0]['updated_at']
        assert tasks[0]['id']

    def test_5_tasks_index(self):
        fixtures = [
            { 'description': 'Get more milk', 'rank': 0 },
            { 'description': 'Feed a cow', 'rank': 1 },
            { 'description': 'Purchase a CD', 'rank': 2 },
            { 'description': 'Drink some more milk', 'rank': 3 },
            { 'description': 'Take up goat farming', 'rank': 4 },
        ]

        self.make_tasks(fixtures)
        response = self.app.get('/tasks')
        data = json.loads(response.get_data())
        descriptions = [ task['description'] for task in data['tasks'] ]
        expected_descriptions = [ task['description'] for task in fixtures ]

        assert sorted(descriptions) == sorted(expected_descriptions)
