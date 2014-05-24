import os
from flask import Flask, jsonify
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)

os.environ.setdefault('TADA_SETTINGS', 'config/development.py')
app.config.from_object('config.shared')
app.config.from_envvar('TADA_SETTINGS')

db = SQLAlchemy(app)

from task import Task

@app.errorhandler(404)
def not_found(error):
    response = jsonify(error='404 Not Found')
    return response, 404

@app.route('/tasks', methods=['GET'])
def index():
    tasks = Task.query.all()
    tasks = [ task.as_dict() for task in tasks ]
    return jsonify(tasks=tasks)
