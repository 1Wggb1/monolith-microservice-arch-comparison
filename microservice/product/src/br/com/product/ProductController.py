import os
from fastapi import FastAPI
from bson import json_util
from pymongo import MongoClient

app = FastAPI()
uri = os.getenv("MONGO_DB", "mongodb://localhost:27017")
client = MongoClient(uri)
database = client.get_database("product_db")

@app.get("/products")
def find_product():
    return find()

def find():
    try:
        product = database.get_collection("product")
        results = product.find({})
        return json_util.dumps(results)
    except Exception as e:
        raise Exception("Unable to find the document due to the following error: ", e)

@app.post("/products")
def create_order(product_dto):
    return create(product_dto)

def create(product_dto):
    try:
        product = database.get_collection("product")
        product.insert_one(product_dto)
    except Exception as e:
        raise Exception("Unable to save the document due to the following error: ", e)