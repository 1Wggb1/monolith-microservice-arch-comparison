import os
from fastapi import FastAPI
from bson import json_util
from pymongo import MongoClient

app = FastAPI()
uri = os.getenv("MONGO_DB", "mongodb://localhost:27017")
client = MongoClient(uri)
database = client.get_database("main_db")

@app.get("/orders")
def find_orders():
    return find("order")

def find(collection_name):
    try:
        print("Finding order...")
        entity_collection = database.get_collection(collection_name)
        entities = entity_collection.find({})
        return json_util.dumps(entities)
    except Exception as e:
        raise Exception("Unable to find the document due to the following error: ", e)

@app.post("/orders")
def create_order(order_dto):
    print("Creating order...")
    return create("order", order_dto)

def create(collection_name, entity_dto):
    try:
        entity_collection = database.get_collection(collection_name)
        entity_collection.insert_one(entity_dto)
    except Exception as e:
        raise Exception("Unable to save the document due to the following error: ", e)

@app.get("/products")
def find_products():
    print("Finding product...")
    return find("product")

@app.post("/products")
def create_product(product_dto):
    print("Creating product...")
    return create("product", product_dto)