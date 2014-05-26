from flask import json
from tests.helpers import TestTada

class TestUpdate(TestTada):
    def api_put(self, url, data):
        data = json.dumps(data)
        return self.app.put(
            url, content_type = 'application/json', data = data
        )

    def test_update_invalid_id(self):
        data = { 'task': { 'position': 2 }}
        response = self.api_put('/tasks/22', data)

        assert response.status_code == 404
        assert '404 Not Found' in response.get_data(as_text = True)

    def test_2_tasks(self):
        self.make_task(description = 'Down to the left', rank = 1)
        task = self.make_task(description = 'Take it back now', rank = 2)
        url = '/tasks/{id}'.format(id = task.id)

        response = self.api_put(url, { 'task': { 'position': 1 }})
        assert response.status_code == 200
