from http import HTTPStatus
from fast_madr.model import UserModel

user = UserModel


def test_retorno_get(client):
    response = client.get("/")

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {"Hello": "Wold"}


def test_adicionado_usuario(client):
    response = client.post(
        "/user/",
        json={
            "username": "test",
            "email": "test@test.com",
            "password": "test",
        },
    )

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        "username": "test",
        "email": "test@test.com",
        "password": "test",
    }


def test_atualizando_usuario(client_with_user):
    response = client_with_user.put(
        "/user/1",
        json={
            "username": "test_modificated",
            "email": "modificated@test.com",
            "password": "test",
        },
    )

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        "id": 1,
        "username": "test_modificated",
        "email": "modificated@test.com",
        "password": "test",
    }


def test_deletando_usuario(client_with_user):
    response = client_with_user.delete("/user/1")

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {"detail": "User deleted."}
