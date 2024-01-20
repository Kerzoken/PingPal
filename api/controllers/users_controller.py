from flask import jsonify, make_response
from api.models.user import User
from api.db import db


def register_user(request):
    username = request.json.get('username')
    password = request.json.get('password')
    email = request.json.get('email')
    bio = request.json.get('bio')

    if not username or not password or not email:
        return make_response(
            jsonify(
                {'message': 'Please provide all required fields(username, password, email)'}),
            400
        )

    user = User.query.filter_by(username=username).first()
    if user:
        return make_response(jsonify({'message': 'Username already exists'}), 400)

    user = User.query.filter_by(email=email).first()
    if user:
        return make_response(jsonify({'message': 'Email already exists'}), 400)

    user = User(username=username, password=password, email=email, bio=bio)
    db.session.add(user)
    db.session.commit()
    return make_response(jsonify({'message': 'User created successfully'}), 200)


def get_all_users(request):
    users = User.query.all()

    users_list = []
    for user in users:
        user_data = {}
        user_data['id'] = user.id
        user_data['username'] = user.username
        user_data['email'] = user.email
        user_data['bio'] = user.bio
        users_list.append(user_data)

    return make_response(jsonify({'users': users_list}), 200)


def get_user_by_id(request, user_id):
    user = User.query.get(user_id)

    if not user:
        return make_response(jsonify({'message': 'No user found'}), 404)

    user_data = {}
    user_data['id'] = user.id
    user_data['username'] = user.username
    user_data['email'] = user.email
    user_data['bio'] = user.bio

    return make_response(jsonify({'user': user_data}), 200)
