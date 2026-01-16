from fastapi import FastAPI
from redis_om import get_redis_connection, HashModel
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
import os

load_dotenv()

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_methods=["*"],
    allow_headers=["*"],
)

redis = get_redis_connection(
    host=os.getenv("R_HOST"),
    port=int(os.getenv("R_PORT")),
    password=os.getenv("R_PWD"),
    decode_responses=True,
)

class Product(HashModel):
    name: str
    price: float
    quantity: int

    class Meta:
        database = redis


@app.get("/products/")
def get_products():
    return [format(pk) for pk in Product.all_pks()]

def format(pk: str):
    product = Product.get(pk)
    return {
        "id": product.pk,
        "name": product.name,
        "price": product.price,
        "quantity": product.quantity,
    }

@app.post("/products/")
def create_product(product: Product):
    return product.save()


@app.get("/products/{pk}")
def get_product(pk: str):
    print(Product.get(pk))
    return Product.get(pk)


@app.delete("/products/delete/{pk}")
def delete_product(pk: str):
    return Product.delete(pk)