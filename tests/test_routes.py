import json
import pytest
from app import app

receipt_id = ''

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_process_receipt(client):
    global receipt_id 
    receipt_data = {
        "retailer": "M&M Corner Market",
        "purchaseDate": "2022-03-21",
        "purchaseTime": "14:33",
        "items": [
            {
            "shortDescription": "Gatorade1",
            "price": "2.25"
            },{
            "shortDescription": "Gatorade",
            "price": "2.25"
            },{
            "shortDescription": "Gatorade",
            "price": "2.25"
            },{
            "shortDescription": "Gatorade",
            "price": "2.25"
            }
        ],
        "total": "9.00"
    }

    response = client.post('/receipts/process', json=receipt_data)
    data = json.loads(response.data)
    receipt_id = data.get('id') 

    assert response.status_code == 200
    assert "id" in data

def test_invalid_process_receipt(client):
    global receipt_id 
    receipt_data = {
        "retailer": "Target",
        "purchaseDate": "2022-01-01",
        "items": [
            {
            "shortDescription": "Mountain Dew 12PK",
            "price": "6.49"
            }
        ],
        "total": "35.35"
    }

    response = client.post('/receipts/process', json=receipt_data)
    assert response.status_code == 400

def test_get_receipt_points(client):
    global receipt_id 
    response = client.get(f'/receipts/{receipt_id}/points')
    data = json.loads(response.data)

    assert response.status_code == 200
    assert 'points' in data
    assert data.get('points') == 116


def test_invalid_get_receipt_points(client):
    response = client.get(f'/receipts/123/points')
    data = json.loads(response.data)

    assert response.status_code == 404