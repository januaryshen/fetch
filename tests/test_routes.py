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
        "retailer": "Target",
        "purchaseDate": "2022-01-01",
        "purchaseTime": "13:01",
        "items": [
            {
            "shortDescription": "Mountain Dew 12PK",
            "price": "6.49"
            },{
            "shortDescription": "Emils Cheese Pizza",
            "price": "12.25"
            },{
            "shortDescription": "Knorr Creamy Chicken",
            "price": "1.26"
            },{
            "shortDescription": "Doritos Nacho Cheese",
            "price": "3.35"
            },{
            "shortDescription": "   Klarbrunn 12-PK 12 FL OZ  ",
            "price": "12.00"
            }
        ],
        "total": "35.35"
    }

    response = client.post('/receipts/process', json=receipt_data)

    assert response.status_code == 200
    data = json.loads(response.data)
    assert "id" in data
    receipt_id = data.get('id') 

def test_get_receipt_points(client):
    global receipt_id 
    response = client.get(f'/receipts/{receipt_id}/points')

    assert response.status_code == 200
    data = json.loads(response.data)
    assert 'points' in data
    assert data.get('points') == 28
