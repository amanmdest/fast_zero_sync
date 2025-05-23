from http import HTTPStatus

from sqlalchemy import select

from fast_zero.models import TodoState, User
from tests.factories import TodoFactory


def test_create_todo_in_user_db_relationship(user, session):
    todo = TodoFactory()

    session.add(todo)
    session.commit()
    session.refresh(todo)

    user = session.scalar(select(User).where(User.id == user.id))

    assert todo in user.todos


def test_create_todo_through_api(client, token):
    response = client.post(
        '/todos/',
        headers={'Authorization': f'Bearer {token}'},
        json={
            'title': 'Test todo',
            'description': 'Test todo description',
            'state': 'draft',
        },
    )
    assert response.status_code == HTTPStatus.OK
    resp_todo = response.json()
    expected_values = {
        'id': 1,
        'title': 'Test todo',
        'description': 'Test todo description',
        'state': 'draft',
    }
    for key, value in expected_values.items():
        assert resp_todo[key] == value

    assert 'created_at' in resp_todo.keys()
    assert 'updated_at' in resp_todo.keys()


def test_should_return_five_todos(session, client, user, token):
    expected_todos = 5
    session.bulk_save_objects(TodoFactory.create_batch(5, user_id=user.id))
    session.commit

    response = client.get(
        '/todos/',
        headers={'Authorization': f'Bearer {token}'},
    )
    assert len(response.json()['todos']) == expected_todos


def test_pagination_should_return_two_todos(session, client, user, token):
    expected_todos = 2
    session.bulk_save_objects(TodoFactory.create_batch(5, user_id=user.id))
    session.commit

    response = client.get(
        '/todos/?offset=1&limit=2',
        headers={'Authorization': f'Bearer {token}'},
    )
    assert len(response.json()['todos']) == expected_todos


def test_list_todos_filter_title_should_return_five_todos(
    session, client, user, token
):
    expected_todos = 5
    session.bulk_save_objects(
        TodoFactory.create_batch(5, user_id=user.id, title='Test title')
    )
    session.commit

    response = client.get(
        '/todos/?title=Test title',
        headers={'Authorization': f'Bearer {token}'},
    )
    assert len(response.json()['todos']) == expected_todos


def test_list_todos_filter_description_should_return_five_todos(
    session, client, user, token
):
    expected_todos = 5
    session.bulk_save_objects(
        TodoFactory.create_batch(5, user_id=user.id, description='description')
    )
    session.commit

    response = client.get(
        '/todos/?description=desc',
        headers={'Authorization': f'Bearer {token}'},
    )
    assert len(response.json()['todos']) == expected_todos


def test_list_todos_filter_state_should_return_five_todos(
    session, client, user, token
):
    expected_todos = 5
    session.bulk_save_objects(
        TodoFactory.create_batch(5, user_id=user.id, state=TodoState.draft)
    )
    session.commit

    response = client.get(
        '/todos/?state=draft',
        headers={'Authorization': f'Bearer {token}'},
    )
    assert len(response.json()['todos']) == expected_todos


def test_list_todos_filter_combined_should_return_5_todos(
    session, user, client, token
):
    expected_todos = 5
    session.bulk_save_objects(
        TodoFactory.create_batch(
            5,
            user_id=user.id,
            title='Test todo combined',
            description='combined description',
            state=TodoState.done,
        )
    )

    session.bulk_save_objects(
        TodoFactory.create_batch(
            3,
            user_id=user.id,
            title='Other title',
            description='other description',
            state=TodoState.todo,
        )
    )
    session.commit()

    response = client.get(
        '/todos/?title=Test todo combined&description=combined&state=done',
        headers={'Authorization': f'Bearer {token}'},
    )

    assert len(response.json()['todos']) == expected_todos


def test_patch_todo(client, session, token, user):
    todo = TodoFactory(user_id=user.id)
    session.add(todo)
    session.commit()
    session.refresh(todo)

    response = client.patch(
        f'/todos/{todo.id}',
        json={'title': 'Batata'},
        headers={'Authorization': f'Bearer {token}'},
    )

    assert response.status_code == HTTPStatus.OK
    assert response.json()['title'] == 'Batata'
    assert response.json()['description'] == todo.description


def test_delete_todo(client, session, token, user):
    todo = TodoFactory(user_id=user.id)
    session.add(todo)
    session.commit()
    session.refresh(todo)

    response = client.delete(
        f'/todos/{todo.id}', headers={'Authorization': f'Bearer {token}'}
    )
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'message': 'Task has been deleted successfully.'
    }


def test_patch_todo_error(client, token):
    response = client.patch(
        '/todos/10', json={}, headers={'Authorization': f'Bearer {token}'}
    )

    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {'detail': 'Task not found.'}


def test_delete_todo_error(client, token):
    response = client.delete(
        '/todos/10', headers={'Authorization': f'Bearer {token}'}
    )

    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {'detail': 'Task not found.'}
