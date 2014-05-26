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
    json = request.get_json().get('task', None)

    if not json:
        return jsonify(error = 'Error: No task object found'), 400

    if 'position' in json and json['position'] != task.rank:
        results = task.move_to(json['position'])

    if 'completed_at' in json and json['completed_at'] != task.completed_at:
        task.completed_at = completed_at
        db.session.add(task)

    db.session.commit()
    response = {}

    # `results` doesn't get populated until we perform the commit.
    if results:
        response['tasks'] = []

        for result in results:
            response['tasks'].append({
                'id': result.id,
                'position': result.rank,
                'description': result.description,
                'created_at': result.created_at,
                'updated_at': result.updated_at,
            })

    response['task'] = task.as_dict()

    return jsonify(response), 200
