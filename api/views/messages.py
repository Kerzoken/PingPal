from flask import Blueprint, request
import api.controllers.messages_controller as messages_controller

messages_bp = Blueprint('messages', __name__)


@messages_bp.route('/send', methods=['POST'])
def send_message():
    return messages_controller.send_message(request)


@messages_bp.route('/all/<int:user_id>', methods=['GET'])
def get_all_messages_for_user(user_id):
    return messages_controller.get_all_messages_for_user(request, user_id)
