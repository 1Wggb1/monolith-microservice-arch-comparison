import os
import json
from fastapi import FastAPI, Response
from pydantic import BaseModel
from bson import json_util
from pymongo import MongoClient
from typing import List

app = FastAPI()
uri = os.getenv("MONGO_DB", "mongodb://localhost:27017")
client = MongoClient(uri)
database = client.get_database("main_db")

@app.get("/orders")
def find_orders():
    return Response(content=find("order"), media_type='application/json')

def find(collection_name):
    try:
        print("Finding order...")
        entity_collection = database.get_collection(collection_name)
        entities = entity_collection.find({})
        return json_util.dumps(entities)
    except Exception as e:
        raise Exception("Unable to find the document due to the following error: ", e)

class OrderDto(BaseModel):
    productIds: List
    total: float
    userId: int
    createAt: int

@app.post("/orders")
def create_order(order_dto: OrderDto):
    print("Creating order...")
    create("order", order_dto)
    return Response(content=None, media_type='application/json', status_code=201)

def create(collection_name, entity_dto):
    try:
        entity_collection = database.get_collection(collection_name)
        entity_collection.insert_one(entity_dto.__dict__)
    except Exception as e:
        raise Exception("Unable to save the document due to the following error: ", e)

@app.get("/products")
def find_products():
    print("Finding product...")
    return Response(content=find("product"), media_type='application/json')

class ProductDto(BaseModel):
    name: str
    description: str
    price: float
    createAt: int

@app.post("/products")
def create_product(product_dto: ProductDto):
    print(f"Creating product...")
    create("product", product_dto)
    return Response(content=None, media_type='application/json', status_code=201)