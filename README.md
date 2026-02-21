## Retirement Saver API

Simple FastAPI service.

## Retirement Saver API

Simple FastAPI service.

This is a small FastAPI project that converts raw transaction text into structured data.

Example:

Input
`Swiggy Rs 350 UPI`

Output

{
  "merchant": "Swiggy",
  "amount": 350,
  "category": "food",
  "channel": "upi"
}

## In this project

In real life, transaction data is messy (SMS, bank alerts, emails).
This API cleans that text and makes it usable for tracking spending and planning savings.

It can be used inside a retirement planning system to understand where money is going.


## Working

* Extracts merchant name
* Detects amount
* Assigns a simple category (food, travel, groceries, etc.)
* Detects payment mode (UPI, card, cash)


## Technologies used

* Python
* FastAPI
* Uvicorn
* Docker


## Localhost details

pip install -r requirements.txt
python -m uvicorn app.main:app --reload --port 8000


Open:
http://localhost:8000/docs


## Docker


docker build -t retirement-parser .
docker run -p 8000:8000 retirement-parser


## Links

GitHub:
https://github.com/Vyankatesh1/retirement-saver-api

Docker Image:
https://hub.docker.com/r/Vyankatesh16/retirement-parser

## By:
Vyankatesh Shahapurkar
