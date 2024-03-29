from api.db import db


class User(db.Model):
    """
    Represents a user in the system.
    """
    id = db.Column(db.Integer, primary_key=True)

    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(80), unique=True, nullable=False)
    bio = db.Column(db.String(80))

    def __repr__(self):
        return f'<User {self.username}>'
