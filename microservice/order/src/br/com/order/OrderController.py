import os

from fastapi import FastAPI
from bson import json_util
from pymongo import MongoClient

app = FastAPI()
uri = os.getenv("MONGO_DB", "mongodb://localhost:27017")
client = MongoClient(uri)
database = client.get_database("order_db")

@app.get("/orders")
def orders():
    return find_orders()

def find_orders():
    try:
        order = database.get_collection("order")
        results = order.find({})
        return json_util.dumps(results)
    except Exception as e:
        raise Exception("Unable to find the document due to the following error: ", e)

@app.post("/orders")
def create_order(order_dto):
    return do_create_order(order_dto)

def do_create_order(order_dto):
    try:
        order = database.get_collection("order")
        order.insert_one(order_dto)
    except Exception as e:
        raise Exception("Unable to save the document due to the following error: ", e)