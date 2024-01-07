from . import db


class User(db.Model):
    """
    Represents a user in the system.
    """
    id = db.Column(db.Integer, primary_key=True)

    username = db.Column(db.String(80), unique=True)
    email_address = db.Column(db.String(80), unique=True)
    bio = db.Column(db.String(80), unique=True)
    password = db.Column(db.String(80), unique=True)

    def __repr__(self):
        return f'<User {self.username}>'
