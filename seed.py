from shell import *
from tasks.models import Task

db.drop_all()
db.create_all()

tasks = [
    { 'description': 'Get some milk', 'rank': 1 },
    { 'description': 'Buy some clothes', 'rank': 2 },
    { 'description': 'Feed the cow', 'rank': 3 },
    { 'description': 'Save your friend from death', 'rank': 4 }
]

for task in tasks:
    model = Task(**task)
    db.session.add(model)

db.session.commit()
exit()
