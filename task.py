from datetime import datetime
from tada import db

__all__ = ['Task']

class Task(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    description = db.Column(db.Text)
    rank = db.Column(db.Integer, unique = True,
                                 nullable = False)
    completed_at = db.Column(db.DateTime)
    created_at = db.Column(db.DateTime, nullable = False,
                                        default = datetime.now)
    updated_at = db.Column(db.DateTime, nullable = False,
                                        default = datetime.now,
                                        onupdate = datetime.now)

    def as_dict(self):
        completed_at = to_json_datetime(self.completed_at)
        created_at = to_json_datetime(self.created_at)
        updated_at = to_json_datetime(self.updated_at)

        return {
            "id": self.id,
            "description": self.description,
            "rank": self.rank,
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
def to_json_datetime(datetime):
    if datetime is not None:
        return datetime.isoformat()
    else:
        return None
