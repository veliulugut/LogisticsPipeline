from faker import Faker
from faker_vehicle import VehicleProvider
from datetime import datetime
import random
from .Logisctics import Customer, Order, Order_Item, Deliveries, Vehicles, Kpis
import json

fake = Faker()
fake.add_provider(VehicleProvider)

def generate_mock_data():
    # Generate customers
    customers = [
        Customer(
            customer_id=fake.uuid4(),
            name=fake.name(),
            email=fake.email(),
            phone=fake.phone_number(),
            address=fake.address(),
            loyalty_status=random.choice(['Gold', 'Silver', 'Bronze']),
            total_orders=random.randint(10, 50),
            total_spent=random.uniform(100, 5000),
            average_order_value=random.uniform(10, 1000),
            customer_since=fake.date_this_decade().strftime('%Y-%m-%d'),
            order_frequency=random.choice(['Weekly', 'Monthly', 'Quarterly']),
            total_discount_applied=random.uniform(0, 500),
            preferred_contact_method=random.choice(['Email', 'Phone']),
            average_feedback_rating=random.uniform(1, 5),
            preferred_shipping_method=random.choice(['Standard', 'Express', 'Overnight'])
        )
        for _ in range(5)
    ]

    # Generate orders
    orders = [
        Order(
            order_id=fake.uuid4(),
            customer_id=customer.customer_id,
            order_date=fake.date_this_year().strftime('%Y-%m-%d'),
            delivery_date=fake.date_this_year().strftime('%Y-%m-%d'),
            total_amount=random.uniform(50, 200),
            shipping_cost=random.uniform(5, 50),
            payment_method=random.choice(['Credit Card', 'PayPal', 'Bank Transfer']),
            discount_applied=random.uniform(0, 50),
            status=random.choice(['Pending', 'Shipped', 'Delivered']),
            order_duration_minutes=random.randint(30, 120),
            estimated_delivery_time_minutes=random.randint(10, 90)
        )
        for customer in customers
        for _ in range(random.randint(1, 3))
    ]

    # Generate order items
    order_items = [
        Order_Item(
            order_item_id=fake.uuid4(),
            order_id=order.order_id,
            item_id=fake.uuid4(),
            category=random.choice(['Electronics', 'Clothing', 'Home Appliances']),
            quantity=random.randint(1, 5),
            price_per_unit=random.uniform(10, 500),
            total_price=random.uniform(10, 2500),
            weight_kg=random.uniform(0.5, 20),
            volume_m3=random.uniform(0.01, 1.5),
            product_name=fake.word(),
            product_sku=fake.uuid4()
        )
        for order in orders
        for _ in range(random.randint(1, 3))
    ]

    # Generate vehicles
    vehicles = [
        Vehicles(
            vehicle_id=fake.uuid4(),
            type=random.choice(['Truck', 'Van', 'Car']),
            license_plate=fake.license_plate(),
            capacity_kg=random.randint(500, 5000),
            current_load_kg=random.randint(100, 3000),
            status=random.choice(['Active', 'Idle', 'Under Maintenance']),
            location_lat=fake.latitude(),
            location_lon=fake.longitude(),
            last_maintenance=fake.date_this_year().strftime('%Y-%m-%d'),
            fuel_efficiency_l_per_km=random.uniform(5, 15),
            next_maintenance_due=fake.date_this_year().strftime('%Y-%m-%d'),
            total_distance_traveled_km=random.uniform(1000, 50000)
        )
        for _ in range(5)
    ]

    # Generate deliveries
    deliveries = [
        Deliveries(
            vehicle_id=vehicle.vehicle_id,
            type=vehicle.type,
            license_plate=vehicle.license_plate,
            capacity_kg=vehicle.capacity_kg,
            current_load_kg=vehicle.current_load_kg,
            status=vehicle.status,
            location_lat=vehicle.location_lat,
            location_lon=vehicle.location_lon,
            last_maintenance=vehicle.last_maintenance,
            fuel_efficiency_l_per_km=vehicle.fuel_efficiency_l_per_km,
            next_maintenance_due=vehicle.next_maintenance_due,
            total_distance_traveled_km=vehicle.total_distance_traveled_km
        )
        for vehicle in vehicles
    ]

    # Generate KPIs
    kpis = [
        Kpis(
            kpi_id=fake.uuid4(),
            total_sales=random.uniform(5000, 20000),
            total_deliveries=random.randint(100, 500),
            average_delivery_time_minutes=random.uniform(30, 120),
            total_distance_traveled_km=random.uniform(1000, 10000),
            total_fuel_consumption_liters=random.uniform(200, 1000),
            average_order_value=random.uniform(10, 1000),
            top_category=random.choice(['Electronics', 'Clothing', 'Home Appliances']),
            feedback_avg_rating=random.uniform(1, 5),
            record_date=fake.date_this_year().strftime('%Y-%m-%d'),
            delivery_efficiency_score=random.uniform(50, 100),
            customer_satisfaction_score=random.uniform(60, 90)
        )
        for _ in range(3)
    ]

    # Compile all data
    mock_data = {
        "customers": [customer.__dict__ for customer in customers],
        "orders": [order.__dict__ for order in orders],
        "order_items": [order_item.__dict__ for order_item in order_items],
        "deliveries": [delivery.__dict__ for delivery in deliveries],
        "vehicles": [vehicle.__dict__ for vehicle in vehicles],
        "kpis": [kpi.__dict__ for kpi in kpis]
    }

    return mock_data