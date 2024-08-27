from fastapi import FastAPI , Depends
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session
from models import SessionLocal, OrdersList
from tools import generate_random_pizza
from schema import OrderValidator
from orders import submit_orders

app = FastAPI(docs_url='/api')

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/")
async def main_page():
    return RedirectResponse(url="/api")

@app.post("/v2/generate")
async def create_random_pizza(db: Session = Depends(get_db)):
    pizza = generate_random_pizza(db)
    return {'message' : f'{len(pizza)} random pizzas created.'}

@app.post("/v2/orders")
async def submit_order(order: OrderValidator,db: Session = Depends(get_db)):
    
    new_order = OrdersList(
        status='pending',
        quantity=order.quantity,
    )
    
    db.add(new_order)
    db.commit()
    
    data = {
        'order_id' : new_order.id,
        'quantity' : new_order.quantity,
    }
    
    for i in range(10): # send 10 orders for simulate multi orders
    
        submit_orders.apply_async(args=[data])
    
    return {'message' : 'Order sent.'}


