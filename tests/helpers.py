import os
os.environ['TADA_SETTINGS_PATH'] = 'config/test.py'

from tada import app, db, Task
import unittest
import tempfile

class TestTada():

    def setup(self):
        self.db_fd, app.config['DATABASE'] = tempfile.mkstemp()
        self.app = app.test_client()
        db.create_all()

    def teardown(self):
        db.drop_all()
        os.close(self.db_fd)
        os.unlink(app.config['DATABASE'])

    def make_tasks(self, tasks):
        for attributes in tasks:
            self.make_task(**attributes)

    def make_task(self, **attributes):
        task = Task(**attributes)
        db.session.add(task)
        db.session.commit()
