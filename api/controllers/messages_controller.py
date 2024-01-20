from datetime import datetime
from flask import jsonify
from api.models.message import Message
from api.models.user import User
from api.models import db


def send_message(request):
    sender_id = request.json.get('sender_id')
    receiver_id = request.json.get('receiver_id')
    message = request.json.get('message')

    if not sender_id or not receiver_id or not message:
        return jsonify({'message': 'Please provide all required fields(sender_id, receiver_id, message)'})

    date_created = request.json.get('date_created')
    if not date_created:
        date_created = datetime.now()

    message = Message(sender_id=sender_id,
                      receiver_id=receiver_id, message=message, date_created=date_created)
    db.session.add(message)
    db.session.commit()
    return jsonify({'message': 'Message sent successfully'})


def get_all_messages_for_user(request, user_id):
    user = User.query.get(user_id)
    if not user:
        return jsonify({'message': 'No user found'})

    from_date = request.args.get('from_date')
    sender_id = request.args.get('sender_id')

    messages = None

    if from_date:
        messages = Message.query.filter(Message.receiver_id == user_id,
                                        Message.date_created > from_date).all()

    if sender_id:
        sender = User.query.get(sender_id)
        if not sender:
            return jsonify({'message': 'No user found'})

        messages = Message.query.filter(Message.receiver_id == user_id,
                                        Message.sender_id == sender_id).all()

    if not messages:
        messages = Message.query.filter_by(receiver_id=user_id).all()

    messages_list = []
    for message in messages:
        message_data = {}
        message_data['id'] = message.id
        message_data['sender_id'] = message.sender_id
        message_data['receiver_id'] = message.receiver_id
        message_data['message'] = message.message
        message_data['date_created'] = message.date_created
        messages_list.append(message_data)

    return jsonify({'messages': messages_list})
