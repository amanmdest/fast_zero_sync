from http import HTTPStatus

from fastapi.testclient import TestClient

from fast_zero.batatinha import app


def test_batatinha_deve_retornar_ola_mundo_no_html():
    client = TestClient(app)

    response = client.get('/batatinha')  # Act

    assert response.status_code == HTTPStatus.OK  # Assert
    assert ('Olá Mundo') in response.text  # Assert
