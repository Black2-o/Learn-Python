from fastapi import FastAPI
from redis_om import get_redis_connection, HashModel
from fastapi.middleware.cors import CORSMiddleware
from fastapi.background import BackgroundTasks
from dotenv import load_dotenv
from starlette.requests import Request
import requests
import os
import time

load_dotenv()

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# This should be different database. Each Microservice should have its own database but for now redis give one so use one now.
redis = get_redis_connection(
    host=os.getenv("R_HOST"),
    port=int(os.getenv("R_PORT")),
    password=os.getenv("R_PWD"),
    decode_responses=True,
)

class Order(HashModel):
    product_id: str
    price: float
    fee: float
    total: float
    quantity: int
    status: str  # pending, completed, refunded

    class Meta:
        database = redis



@app.get("/order/{pk}")
def get_order(pk: str):
    return Order.get(pk)


@app.post("/orders/")
async def create_order(request: Request, background_tasks: BackgroundTasks):
    body = await request.json()
    req = requests.get("http://localhost:8000/products/%s" % body["product_id"])
    product = req.json()

    order = Order(
        product_id=body["product_id"],
        price=product["price"],
        fee=0.5 * product["price"],
        total=1.5 * product["price"],
        quantity=body["quantity"],
        status="pending",
    )
    order.save()

    background_tasks.add_task(order_completed, order)

    return order

def order_completed(order:Order):
    time.sleep(20)
    order.status = "completed"
    order.save()
