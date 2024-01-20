import pytest
from api.app import create_app, db
from api.models.user import User


@pytest.fixture
def client():
    app = create_app()
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
        yield client
        with app.app_context():
            db.session.remove()
            db.drop_all()


def test_successful_user_registration(client):
    data = {'username': 'testuser', 'password': 'testpassword',
            'email': 'test@example.com'}
    response = client.post('/users/register', json=data)
    assert response.status_code == 200
    assert 'User created successfully' in response.get_data(as_text=True)

    user = User.query.filter_by(username='testuser').first()
    assert user is not None
    assert user.email == 'test@example.com'


def test_registration_with_missing_fields(client):
    data = {'username': 'testuser', 'password': 'testpassword'}
    response = client.post('/users/register', json=data)
    assert response.status_code == 400
    assert 'Please provide all required fields' in response.get_data(
        as_text=True)


def test_registration_with_existing_username(client):
    data = {'username': 'existinguser',
            'password': 'newpassword', 'email': 'email'}
    response = client.post('/users/register', json=data)
    assert response.status_code == 200
    assert 'User created successfully' in response.get_data(as_text=True)

    data = {'username': 'existinguser', 'password': 'newpassword',
            'email': 'newemail@example.com'}
    response = client.post('/users/register', json=data)
    assert response.status_code == 400
    assert 'Username already exists' in response.get_data(as_text=True)


def test_registration_with_existing_email(client):
    data = {'username': 'test', 'password': 'newpassword',
            'email': 'existingemail@example.com'}
    response = client.post('/users/register', json=data)
    assert response.status_code == 200
    assert 'User created successfully' in response.get_data(as_text=True)

    data = {'username': 'newuser', 'password': 'newpassword',
            'email': 'existingemail@example.com'}
    response = client.post('/users/register', json=data)
    assert response.status_code == 400
    assert 'Email already exists' in response.get_data(as_text=True)


def test_retrieve_all_users(client):
    response = client.get('/users/all')
    assert response.status_code == 200


def test_retrieve_user_by_valid_id(client):
    data = {'username': 'testuser', 'password': 'testpassword',
            'email': 'test@test.com'}
    response = client.post('/users/register', json=data)
    assert response.status_code == 200

    response = client.get('/users/1')
    assert response.status_code == 200
    user = response.get_json()
    assert user['id'] == 1


def test_retrieve_user_by_invalid_id(client):
    response = client.get('/users/999')
    assert response.status_code == 404
    assert 'No user found' in response.get_data(as_text=True)
