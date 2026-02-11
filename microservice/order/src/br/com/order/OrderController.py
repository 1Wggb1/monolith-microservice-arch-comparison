import os
from fastapi import FastAPI, Response
from pydantic import BaseModel
from bson import json_util
from pymongo import MongoClient
from typing import List


app = FastAPI()
uri = os.getenv("MONGO_DB", "mongodb://localhost:27017")
client = MongoClient(uri)
database = client.get_database("order_db")

class OrderDto(BaseModel):
    productIds: List
    total: float
    userId: int
    createAt: int

@app.get("/orders")
def orders():
    return Response(content=find(), media_type='application/json')

def find():
    try:
        order = database.get_collection("order")
        results = order.find({})
        return json_util.dumps(results)
    except Exception as e:
        raise Exception("Unable to find the document due to the following error: ", e)

@app.post("/orders")
def create_order(order_dto: OrderDto):
    create(order_dto)
    return Response(content=None, media_type='application/json', status_code=201)

def create(order_dto):
    try:
        order = database.get_collection("order")
        order.insert_one(order_dto.__dict__)
    except Exception as e:
        raise Exception("Unable to save the document due to the following error: ", e)