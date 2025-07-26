import pytest
from django.urls import reverse
from django.contrib.auth import get_user_model

User = get_user_model()


@pytest.mark.django_db
def test_registro(client):
    response = client.post(reverse("index"), {
        "form_type": "registro",
        "nome": "Teste",
        "email": "teste@example.com",
        "senha": "Senha123!",
        "confirmar_senha": "Senha123!",
    })

    assert response.status_code == 302
    assert User.objects.filter(email="teste@example.com").exists()


@pytest.mark.django_db
def test_login(client):
    user = User.objects.create_user(email="login@example.com", nome="Login Teste", password="Senha123!")
    
    response = client.post(reverse("index"), {
        "form_type": "login",
        "username": "login@example.com",
        "password": "Senha123!",
    })

    assert response.status_code == 302
    assert response.url == reverse("calculadora")


@pytest.mark.django_db
def test_soma(client):
    user = User.objects.create_user(email="soma@example.com", nome="Soma Teste", password="Senha123!")
    client.login(username="soma@example.com", password="Senha123!")

    response = client.post(reverse("calculadora"), {
        "valor1": 5,
        "valor2": 3,
        "operacao": "soma",
    })

    assert b"5.0 + 3.0" in response.content
    assert b"= 8.0" in response.content


@pytest.mark.django_db
def test_subtracao(client):
    user = User.objects.create_user(email="sub@example.com", nome="Sub Teste", password="Senha123!")
    client.login(username="sub@example.com", password="Senha123!")

    response = client.post(reverse("calculadora"), {
        "valor1": 10,
        "valor2": 4,
        "operacao": "subtracao",
    })

    assert b"10.0 - 4.0" in response.content
    assert b"= 6.0" in response.content


@pytest.mark.django_db
def test_multiplicacao(client):
    user = User.objects.create_user(email="mul@example.com", nome="Mul Teste", password="Senha123!")
    client.login(username="mul@example.com", password="Senha123!")

    response = client.post(reverse("calculadora"), {
        "valor1": 2,
        "valor2": 6,
        "operacao": "multiplicacao",
    })

    assert b"2.0 \xc3\x97 6.0" in response.content
    assert b"= 12.0" in response.content


@pytest.mark.django_db
def test_divisao(client):
    user = User.objects.create_user(email="div@example.com", nome="Div Teste", password="Senha123!")
    client.login(username="div@example.com", password="Senha123!")

    response = client.post(reverse("calculadora"), {
        "valor1": 10,
        "valor2": 2,
        "operacao": "divisao",
    })

    assert b"10.0 \xc3\xb7 2.0" in response.content  # ÷
    assert b"= 5.0" in response.content
