import pytest
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../app'))

from unittest.mock import patch, MagicMock
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_index(client):
    """Prueba que la ruta raíz responde correctamente"""
    response = client.get('/')
    assert response.status_code == 200
    data = response.get_json()
    assert "GlowSkin" in data["mensaje"]

def test_salud(client):
    """Prueba el endpoint de salud"""
    response = client.get('/salud')
    assert response.status_code == 200
    data = response.get_json()
    assert data["estado"] == "activo"

@patch('app.get_db')
def test_get_productos(mock_db, client):
    """Prueba obtener lista de productos"""
    mock_conn = MagicMock()
    mock_cursor = MagicMock()
    mock_cursor.fetchall.return_value = [
        {"id": 1, "nombre": "Crema Hidratante", "precio": 45000}
    ]
    mock_conn.cursor.return_value = mock_cursor
    mock_db.return_value = mock_conn

    response = client.get('/productos')
    assert response.status_code == 200
    data = response.get_json()
    assert isinstance(data, list)

@patch('app.get_db')
def test_crear_producto(mock_db, client):
    """Prueba creación de un nuevo producto"""
    mock_conn = MagicMock()
    mock_cursor = MagicMock()
    mock_conn.cursor.return_value = mock_cursor
    mock_db.return_value = mock_conn

    nuevo = {
        "nombre": "Tónico Rosas",
        "descripcion": "Tónico calmante con agua de rosas",
        "precio": 32000,
        "categoria": "Tónicos"
    }
    response = client.post('/productos', json=nuevo)
    assert response.status_code == 201

@patch('app.get_db')
def test_producto_no_encontrado(mock_db, client):
    """Prueba que retorna 404 si el producto no existe"""
    mock_conn = MagicMock()
    mock_cursor = MagicMock()
    mock_cursor.fetchone.return_value = None
    mock_conn.cursor.return_value = mock_cursor
    mock_db.return_value = mock_conn

    response = client.get('/productos/999')
    assert response.status_code == 404
