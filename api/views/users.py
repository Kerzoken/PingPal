from flask import Blueprint, request
from api.controllers.users_controller import register_user, get_all_users, get_user_by_id

users_bp = Blueprint('auth', __name__)


@users_bp.route('/register', methods=['POST'])
def register():
    return register_user(request)


@users_bp.route('/all', methods=['GET'])
def get_users():
    return get_all_users(request)


@users_bp.route('/user/<int:user_id>', methods=['GET'])
def get_user(user_id):
    return get_user_by_id(request, user_id)
