from faker import Faker
import random
from datetime import datetime, timedelta
import uuid

fake = Faker()

def generate_mock_data():
    # Generate order data
    order_id = str(uuid.uuid4())
    customer_id = str(uuid.uuid4())
    order_date = datetime.now()
    delivery_date = order_date + timedelta(days=random.randint(1, 5))
    
    order_data = {
        "order_id": order_id,
        "customer_id": customer_id,
        "order_date": order_date.isoformat(),
        "delivery_date": delivery_date.isoformat(),
        "total_amount": round(random.uniform(50, 1000), 2),
        "shipping_cost": round(random.uniform(5, 50), 2),
        "payment_method": random.choice(["Credit Card", "PayPal", "Bank Transfer"]),
        "status": random.choice(["Pending", "Processing", "Shipped", "Delivered"]),
        "items": []
    }
    
    # Generate 1-5 items for the order
    for _ in range(random.randint(1, 5)):
        item = {
            "item_id": str(uuid.uuid4()),
            "product_name": fake.word(),
            "quantity": random.randint(1, 10),
            "price": round(random.uniform(10, 200), 2),
            "category": random.choice(["Electronics", "Clothing", "Books", "Food"])
        }
        order_data["items"].append(item)
    
    # Generate delivery data
    delivery_data = {
        "vehicle_id": str(uuid.uuid4()),
        "type": random.choice(["Truck", "Van", "Motorcycle"]),
        "status": random.choice(["En Route", "Delayed", "Delivered"]),
        "location": {
            "lat": float(fake.latitude()),
            "lon": float(fake.longitude())
        }
    }
    
    # Combine all data
    mock_data = {
        "timestamp": datetime.now().isoformat(),
        "order": order_data,
        "delivery": delivery_data
    }
    
    return mock_data
