import os
from flask import Flask, jsonify
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
os.environ.setdefault('TADA_SETTINGS_PATH', 'config/development.py')
app.config.from_object('config.shared')
app.config.from_envvar('TADA_SETTINGS_PATH')
db = SQLAlchemy(app)

@app.errorhandler(404)
def not_found(error):
    return jsonify(error = '404 Not Found'), 404

from tasks import tasks
app.register_blueprint(tasks)
