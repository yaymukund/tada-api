import os
from flask import Flask, jsonify
from flask.ext.sqlalchemy import SQLAlchemy

os.environ.setdefault('TADA_SETTINGS', '../config/development.py')

app = Flask(__name__)
app.config.from_object('config.shared')
app.config.from_envvar('TADA_SETTINGS')

db = SQLAlchemy(app)

@app.errorhandler(404)
def not_found(error):
    response = jsonify(error='404 Not Found')
    return response, 404
