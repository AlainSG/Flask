import pytest

from src.app import app
from unittest.mock import patch


@pytest.fixture
def client():
    app.testing = True
    return app.test_client()


# Prueba suma
def test_suma(client):
    respuesta = client.get("/suma/5/3")
    assert respuesta.status_code == 200
    assert respuesta.get_json()["Resultado"] == 8


# Prueba resta
def test_resta(client):
    respuesta = client.get("/resta/5/3")
    assert respuesta.status_code == 200
    assert respuesta.get_json()["Resultado"] == 2


# Prueba multiplicacion
def test_multiplicacion(client):
    respuesta = client.get("/multiplicacion/5/3")
    assert respuesta.status_code == 200
    assert respuesta.get_json()["Resultado"] == 15


# Prueba division
def test_division(client):
    with patch("src.app.division", return_value={"Resultado": 2.5}):
        respuesta = client.get("division/5/2")
        assert respuesta.status_code == 200
        assert respuesta.get_json()["Resultado"] == 2.5
