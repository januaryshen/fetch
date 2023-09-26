# Receipt Processor
The receipt processor calculates the points of a receipt. The project is based on [Fetch's take-home assessment](https://github.com/fetch-rewards/receipt-processor-challenge/tree/main).

## Installing

Install requirements:
```
pip install -r requirements.txt
```
## Run the app 
Under `/fetch`, run
```
python app.py
```
After the app is started, in terminal or postman, run query against the endpoint:


Path 1: `/receipts/process`

```bash
curl --location 'http://localhost:5000/receipts/process' \
--header 'Content-Type: application/json' \
--data '{
    "retailer": "Target",
    "purchaseDate": "2022-01-01",
    "purchaseTime": "13:01",
    "items": [
        {
            "shortDescription": "Mountain Dew 12PK",
            "price": "6.49"
        }
    ],
    "total": "35.35"
}'
```
Example response:
```
{"id":"6dc1dacb-7fe4-413a-ada3-a1185b2f564a"}
```

Path 2: `/receipts/{id}/points`
```bash
curl --location 'http://localhost:5000/receipts/<id>/points'
```

Example response:
```
{"point":28}
```
## Test
To run the test with `pytest`:
``````
python -m venv venv
source venv/bin/activate
pytest tests
``````
To leave the virtual environment:
```
deactivate
```