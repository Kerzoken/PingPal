from . import db


class Message(db.Model):
    """
    Represents a message in the system.
    """
    id = db.Column(db.Integer, primary_key=True)
    message = db.Column(db.String(80), unique=True)
    reciever_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    sender_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return f'<Message {self.message}>'
