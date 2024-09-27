from http import HTTPStatus
from fast_madr.schema import UserModel

user = UserModel


def test_retorno_get(client):
    response = client.get("/")

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {"Hello": "Wold"}


def test_adicionar_usuario(client):
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


def test_adicionar_usuario_existente(client_with_user):
    response = client_with_user.post(
        "/user/",
        json={
            "username": "test",
            "email": "test@test.com",
            "password": "test",
        },
    )

    assert response.status_code == HTTPStatus.BAD_REQUEST
    assert response.json() == {"detail": "User already exists."}


def test_atualizar_usuario(client_with_user):
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


def test_atualizar_usuario_nao_encontrado(client_with_user):
    response = client_with_user.put(
        "/user/2",
        json={
            "username": "test_modificated",
            "email": "modificated@test.com",
            "password": "test",
        },
    )

    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {"detail": "User not found."}


def test_deletar_usuario(client_with_user):
    response = client_with_user.delete("/user/1")

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {"detail": "User deleted."}


def test_deletar_usuario_nao_encontrado(client_with_user):
    response = client_with_user.delete("/user/2")

    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {"detail": "User not found."}
