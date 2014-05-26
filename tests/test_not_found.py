from flask import json
from tests.helpers import TestTada

class TestNotFound(TestTada):

    def test_404_response_code(self):
        response = self.app.get('/')
        assert response.status_code == 404

    def test_404_response_data(self):
        response = self.app.get('/')
        assert '404 Not Found' in response.get_data(as_text = True)
