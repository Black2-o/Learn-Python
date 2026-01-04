from fastapi import FastAPI
from redis_om import get_redis_connection, HashModel
from dotenv import load_dotenv
import os

load_dotenv()

app = FastAPI()

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
    return Product.all_pks()

@app.post("/products/")
def create_product(product: Product):
    return product.save()