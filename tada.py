import os
from flask import Flask, jsonify, request
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
os.environ.setdefault('TADA_SETTINGS_PATH', 'config/development.py')
app.config.from_object('config.shared')
app.config.from_envvar('TADA_SETTINGS_PATH')
db = SQLAlchemy(app)

from sqlalchemy import func
from task import Task

@app.errorhandler(404)
def not_found(error):
    return jsonify(error = '404 Not Found'), 404

@app.route('/tasks', methods = ['GET'])
def index():
    tasks = Task.query.all()
    tasks = [ task.as_dict() for task in tasks ]
    return jsonify(tasks = tasks)

@app.route('/tasks', methods = ['POST'])
def create():
    description = request.form.get('description', '')
    description = description.strip()

    if not description:
        response = jsonify(error = 'Description cannot be empty')
        response.status_code = 400
        return response

    max_rank = db.session.query(
        func.coalesce(
            func.max(Task.rank), 0
        )
    ).as_scalar()

    task = Task(description = description, rank = max_rank + 1)

    db.session.add(task)
    db.session.commit()
    response = jsonify(task = task.as_dict())
    return response, 201
