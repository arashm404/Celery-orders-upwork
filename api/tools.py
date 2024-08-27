import random
import string
import time
from sqlalchemy.orm import Session
from models import MyPizza  # Assuming models.py is in the api directory

def generate_random_pizza(db: Session, count: int = 10000):
    
    pizzas = []
    
    for _ in range(count):
        # Generate a random 6-character string for the name
        name = ''.join(random.choices(string.ascii_letters, k=6))
        
        # Generate a random integer between 1 and 5 for total_used
        total_used = random.randint(1, 5)
        
        # Generate a random time offset for not_usable_till
        not_usable_till = time.time() + random.choice([1000, -1000])
        
        last_used = time.time() + random.randint(-1100,-1000)
        
        # Create a new MyPizza instance
        new_pizza = MyPizza(
            name=name,
            total_used=total_used,
            not_usable_till=int(not_usable_till),
            last_used=last_used
        )
        
        pizzas.append(new_pizza)
    
    # Add all new pizzas to the session and commit
    db.add_all(pizzas)
    db.commit()
    
    # Refresh the instances to get updated data (optional)
    for pizza in pizzas:
        db.refresh(pizza)
    
    return pizzas

