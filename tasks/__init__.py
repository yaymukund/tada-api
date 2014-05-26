from flask import Blueprint
tasks = Blueprint('tasks', __name__)

from tasks import models, views
