import os

DEBUG = False
SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']

print('Production mode configuration loaded.')
