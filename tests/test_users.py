import pytest
from jose import jwt
from app import schemas
from .database import client, session
from app.config import settings


def test_create_user(client):
    res = client.post(
        "/users/", json={"email": "hello@gmail.com", "password": "password13"}
    )
    new_User = schemas.UserOut(**res.json())
    assert new_User.email == "hello@gmail.com"
    assert res.status_code == 201


def test_login_user(test_login_user, client):
    res = client.post(
        "/login/",
        data={"username": test_login_user.email, "password": test_login_user.password},
    )
    login_res = schemas.Token(**res.json())
    payload = jwt.decode(
        login_res.access_token, settings.secret_key, algorithms=[settings.algorithm]
    )
    id = payload.get("user_id")
    assert id == test_login_user.id
    assert login_res.token_type == "bearer"
    assert res.status_code == 200
