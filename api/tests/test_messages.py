import pytest
from datetime import datetime
from api.app import create_app, db
from api.models.user import User
from api.models.message import Message


@pytest.fixture
def app_client():
    app = create_app()
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
            # Creating test users for message sending/receiving
            user1 = User(username='user1', password='pass1',
                         email='user1@example.com')
            user2 = User(username='user2', password='pass2',
                         email='user2@example.com')
            db.session.add(user1)
            db.session.add(user2)
            db.session.commit()
        yield app, client
        with app.app_context():
            db.session.remove()
            db.drop_all()


def test_successful_message_sending(app_client):
    app, client = app_client
    data = {'sender_id': 1, 'receiver_id': 2, 'message': 'Hello'}
    response = client.post('/messages/send', json=data)
    assert response.status_code == 201
    assert 'Message sent successfully' in response.get_data(as_text=True)


def test_sending_message_with_missing_fields(app_client):
    app, client = app_client
    data = {'sender_id': 1, 'message': 'Hello'}
    response = client.post('/messages/send', json=data)
    assert response.status_code == 400
    assert 'Please provide all required fields' in response.get_data(
        as_text=True)


def test_retrieve_messages_for_existing_user(app_client):
    app, client = app_client
    response = client.get('/messages/user/2')
    assert response.status_code == 200
    messages = response.get_json()
    assert isinstance(messages, list)


def test_retrieve_messages_for_non_existing_user(app_client):
    app, client = app_client
    response = client.get('/messages/user/9999')
    assert response.status_code == 404
    assert 'No user found' in response.get_data(as_text=True)
