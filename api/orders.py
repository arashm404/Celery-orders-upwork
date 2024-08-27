from celery import Celery
from models import SessionLocal, MyPizza
from sqlalchemy import desc
import time
import redis
import logging

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',level=logging.INFO)

logger = logging.getLogger('Orders')

# Configure the Celery application
app = Celery(
    "worker",
    broker="redis://redis:6379/0",
    backend="redis://redis:6379/0",
)

rdb = redis.Redis(host='redis', port=6379, db=0)

# Example Celery task
@app.task(time_limit=120)
def submit_orders(
    data : dict
):
    db = SessionLocal()
    
    #Select pizzas who are usable right now and order by less used
    
    pizzas = db.query(
        MyPizza 
    ).filter(
        MyPizza.not_usable_till < time.time()
    ).order_by(
        desc(MyPizza.total_used),
        desc(MyPizza.last_used)
    ).limit(
        data['quantity']
    )
    
    for pizza in pizzas:
        
        logger.info(f'Selected pizza is number {pizza.id}')
        
        if not rdb.get(pizza.id): # if not used last 360 seconds
            
            rdb.set(pizza.id,360) # now put 360 seconds limit
            
            pizza.last_used = int(time.time())
            
        else:
            
            logger.warning(f'Repeated Select!') #repeated select!
            
    db.commit()
    
    db.close()
    
    return True
