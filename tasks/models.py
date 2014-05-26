from datetime import datetime
from tada import db
from sqlalchemy.sql import expression

__all__ = ['Task']

class Task(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    description = db.Column(db.Text)
    rank = db.Column(db.Integer, nullable = False)
    completed_at = db.Column(db.DateTime)
    created_at = db.Column(db.DateTime, nullable = False,
                                        default = datetime.now)
    updated_at = db.Column(db.DateTime, nullable = False,
                                        default = datetime.now,
                                        onupdate = datetime.now)

    __mapper_args__ = { 'eager_defaults': True, }
    __table_args__ = ( db.UniqueConstraint('rank', deferrable = True), )

    def move_to(self, position):
        db.session.execute('SET CONSTRAINTS task_rank_key DEFERRED')

        query = (
            expression.update(Task)
            .where(Task.rank >= position)
            .where(Task.id != self.id)
            .values(rank = Task.rank + 1)
            .returning(
                Task.id,
                Task.created_at,
                Task.updated_at,
                Task.completed_at,
                Task.rank,
                Task.description,
            )
        )

        results = db.session.execute(query)

        self.rank = position
        db.session.add(self)
        return results

    def as_dict(self):
        completed_at = _to_json_datetime(self.completed_at)
        created_at = _to_json_datetime(self.created_at)
        updated_at = _to_json_datetime(self.updated_at)

        return {
            "id": self.id,
            "description": self.description,
            "position": self.rank,
            "completed_at": completed_at,
            "created_at": created_at,
            "updated_at": updated_at,
        }

    def __init__(self, description=None, completed_at=None, rank=None):
        self.description = description
        self.completed_at = completed_at

        if rank is not None:
            self.rank = rank

    def __repr__(self):
        return '<Task id={id}>'.format(id = self.id)

# Helpers
def _to_json_datetime(datetime):
    if datetime is not None:
        return datetime.isoformat()
    else:
        return None
