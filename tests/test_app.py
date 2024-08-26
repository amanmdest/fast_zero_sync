from http import HTTPStatus

from fastapi.testclient import TestClient

from fast_zero.schemas import UserPublic


def test_read_root_deve_retornar_ok_e_ola_mundo(client):
    response = client.get('/')  # Act

    assert response.status_code == HTTPStatus.OK  # Assert
    assert response.json() == {'message': 'Olar Mundis!'}  # Assert


def test_create_user(client):
    response = client.post(
        '/users/',
        json={
            'username': 'testusername',
            'password': 'password',
            'email': 'test@test.com',
        },
    )

    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == {
        'username': 'testusername',
        'email': 'test@test.com',
        'id': 1,
    }


def test_username_already_exists(client, user):
    response = client.post(
        '/users/',
        json={
            'username': 'test',
            'password': 'testtest',
            'email': 'test@test.com',
        },
    )
    assert response.status_code == HTTPStatus.BAD_REQUEST


def test_email_already_exists(client, user):
    response = client.post(
        '/users/',
        json={
            'username': 'test',
            'password': 'testtest',
            'email': f'{user.email}',
        },
    )
    assert response.status_code == HTTPStatus.BAD_REQUEST


def test_read_users(client: TestClient, token):
    response = client.get(
        '/users/', headers={'Authorization': f'Bearer {token}'}
    )

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'users': [
            {
                'id': 1,
                'username': 'test',
                'email': 'test@test.com',
            },
        ],
    }


def test_read_users_with_user(client, user, token):
    user_schema = UserPublic.model_validate(user).model_dump()

    response = client.get(
        '/users/', headers={'Authorization': f'Bearer {token}'}
    )

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'users': [user_schema]}


# def test_get_user_by_id(client):
#    response = client.get('/users/1')
#
#    assert response.status_code == HTTPStatus.OK


def test_update_user(client, user, token):
    response = client.put(
        f'/users/{user.id}',
        headers={'Authorization': f'Bearer {token}'},
        json={
            'password': 'kerouac',
            'username': 'testusername2',
            'email': 'test@test.com',
        },
    )
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'username': 'testusername2',
        'email': 'test@test.com',
        'id': user.id,
    }


def test_update_user_raise_httpexception(client, user):
    response = client.put('/users/5')

    assert response.is_error
    # assert response.status_code == 422 and 404
    # help: Break down assertion into multiple parts


def test_delete_user(client, user, token):
    response = client.delete(
        f'/users/{user.id}',
        headers={'Authorization': f'Bearer {token}'},
    )

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'User deleted'}


def test_delete_user_raise_httpexception(client, user):
    response = client.delete('/users/10')

    assert response.is_error
    # assert response.status_code == HTTPStatus.NOT_FOUND


def test_get_token(client, user):
    response = client.post(
        '/token/',
        data={'username': user.email, 'password': user.clean_password},
    )
    token = response.json()

    assert response.status_code == HTTPStatus.OK
    assert token['token_type'] == 'bearer'
    assert 'access_token' in token
