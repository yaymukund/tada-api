from flask import json
from tests.helpers import TestTada

class TestIndex(TestTada):

    def test_empty_index(self):
        response = self.app.get('/tasks')
        assert response.status_code == 200

        data = json.loads(response.get_data())
        assert not data['tasks']

    def test_1_task_index(self):
        self.make_task(description='Get some milk', rank=0)
        response = self.app.get('/tasks')

        data = json.loads(response.get_data())
        assert len(data['tasks']) == 1

        task = data['tasks'][0]
        assert task['description'] == 'Get some milk'
        assert task['rank'] == 0
        assert task['created_at']
        assert task['updated_at']
        assert task['id']

    def test_5_tasks_index(self):
        self.make_tasks([
            { 'description': 'Get more milk', 'rank': 0 },
            { 'description': 'Feed a cow', 'rank': 1 },
            { 'description': 'Purchase a CD', 'rank': 2 },
            { 'description': 'Drink some more milk', 'rank': 3 },
            { 'description': 'Take up goat farming', 'rank': 4 },
        ])

        response = self.app.get('/tasks')
        data = json.loads(response.get_data())
        descriptions = [ task['description'] for task in data['tasks'] ]

        assert sorted(descriptions) == sorted([
            'Get more milk',
            'Feed a cow',
            'Purchase a CD',
            'Drink some more milk',
            'Take up goat farming',
        ])
