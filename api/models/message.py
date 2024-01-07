from . import db


class Message(db.Model):
    """
    Represents a message in the system.
    """
    id = db.Column(db.Integer, primary_key=True)

    message = db.Column(db.String(80), nullable=False)
    date_created = db.Column(
        db.DateTime, default=db.func.current_timestamp(), nullable=False)

    receiver_id = db.Column(
        db.Integer, db.ForeignKey('user.id'), nullable=False)
    sender_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f'<Message {self.message}>'
