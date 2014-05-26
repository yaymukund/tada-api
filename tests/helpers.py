import os
os.environ['TADA_SETTINGS_PATH'] = 'config/test.py'

from tada import app, db
from tasks.models import Task

class TestTada():

    def setup(self):
        self.app = app.test_client()
        db.drop_all()
        db.create_all()

    def teardown(self):
        db.session.remove()
        db.drop_all()

    def make_tasks(self, tasks):
        return [ self.make_task(**attributes) for attributes in tasks ]

    def make_task(self, **attributes):
        task = Task(**attributes)
        db.session.add(task)
        db.session.commit()
        return task
