from tada import db
from tasks.models import Task
from flask import jsonify, request, Blueprint
from sqlalchemy import func

blueprint = Blueprint('tasks', __name__)

@blueprint.route('/tasks', methods = ['GET'])
def index():
    tasks = Task.query.all()
    tasks = [ task.as_dict() for task in tasks ]
    return jsonify(tasks = tasks)

@blueprint.route('/tasks', methods = ['POST'])
def create():
    description = request.form.get('description', '')
    description = description.strip()

    if not description:
        return jsonify(error = 'Description cannot be empty'), 400

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

@blueprint.route('/tasks/<int:task_id>', methods = ['PUT'])
def update(task_id):
    task = Task.query.get_or_404(task_id)

    try:
        json = request.get_json()
        new_position = json['task']['position']
    except KeyError:
        new_position = None

    if not new_position:
        return jsonify(error = 'Task position cannot be empty'), 400

    results = task.move_to(new_position)
    db.session.commit()
    tasks = []

    for result in results:
        tasks.append({
            'id': result.id,
            'position': result.rank,
            'description': result.description,
            'created_at': result.created_at,
            'updated_at': result.updated_at,
        })

    return jsonify(tasks = tasks, task = task.as_dict()), 200
