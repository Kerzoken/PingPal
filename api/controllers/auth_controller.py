from flask import jsonify
from api.models.user import User
from api.models import db


def register_user(request):
    username = request.json.get('username')
    password = request.json.get('password')

    user = User.query.filter_by(username=username).first()
    if user:
        return jsonify({'message': 'User already exists'})

    user = User(username=username, password=password)
    db.session.add(user)
    db.session.commit()
    return jsonify({'message': 'User created successfully'})


def login_user(request):
    username = request.json.get('username')
    password = request.json.get('password')
    user = User.query.filter_by(username=username).first()

    if not user:
        return jsonify({'message': 'User does not exist'})

    if user.password != password:
        return jsonify({'message': 'Incorrect password'})

    return jsonify({'message': 'Logged in successfully'})
