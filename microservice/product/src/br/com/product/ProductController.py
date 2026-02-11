import os
from fastapi import FastAPI, Response
from pydantic import BaseModel
from bson import json_util
from pymongo import MongoClient
from typing import List

app = FastAPI()
uri = os.getenv("MONGO_DB", "mongodb://localhost:27017")
client = MongoClient(uri)
database = client.get_database("product_db")

class ProductDto(BaseModel):
    name: str
    description: str
    price: float
    createAt: int

@app.get("/products")
def find_products():
    print("Finding product...")
    return Response(content=find(), media_type='application/json')

def find():
    try:
        product = database.get_collection("product")
        results = product.find({})
        return json_util.dumps(results)
    except Exception as e:
        raise Exception("Unable to find the document due to the following error: ", e)

@app.post("/products")
def create_product(product_dto: ProductDto):
    print(f"Creating product...")
    create(product_dto)
    return Response(content=None, media_type='application/json', status_code=201)

def create(product_dto):
    try:
        product = database.get_collection("product")
        product.insert_one(product_dto.__dict__)
    except Exception as e:
        raise Exception("Unable to save the document due to the following error: ", e)