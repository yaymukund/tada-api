import os
from flask import Flask, jsonify
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__, static_folder = 'static', static_url_path = '')
os.environ.setdefault('TADA_SETTINGS_PATH', 'config/development.py')
app.config.from_object('config.shared')
app.config.from_envvar('TADA_SETTINGS_PATH')
db = SQLAlchemy(app)

from tasks.views import blueprint
app.register_blueprint(blueprint)

@app.errorhandler(404)
def not_found(error):
    return jsonify(error = '404 Not Found'), 404

@app.route('/')
def root():
    return app.send_static_file('index.html')
