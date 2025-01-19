class Customer:
    def __init__(self,customer_id,name,email,phone,address,
                 loyalty_status,total_orders,
                 total_spent,average_order_value,customer_since,order_frequency,
                 total_discount_applied,
                 preferred_contact_method,average_feedback_rating,
                 preferred_shipping_method
                 ):
        self.customer_id = customer_id
        self.name = name
        self.email = email
        self.phone = phone
        self.address = address
        self.loyalty_status = loyalty_status
        self.total_orders = total_orders
        self.total_spent = total_spent
        self.average_order_value = average_order_value
        self.customer_since = customer_since
        self.order_frequency = order_frequency
        self.total_discount_applied = total_discount_applied
        self.preferred_contact_method = preferred_contact_method
        self.average_feedback_rating = average_feedback_rating
        self.preferred_shipping_method = preferred_shipping_method
        

class Order:
    def __init__(self,order_id,customer_id,order_date,delivery_date,
                 total_amount,shipping_cost,payment_method,discount_applied,
                 status,order_duration_minutes,
                 estimated_delivery_time_minutes):
        self.order_id = order_id
        self.customer_id = customer_id
        self.order_date = order_date
        self.delivery_date = delivery_date
        self.total_amount = total_amount
        self.shipping_cost = shipping_cost
        self.payment_method = payment_method
        self.discount_applied = discount_applied
        self.status = status
        self.order_duration_minutes = order_duration_minutes
        self.estimated_delivery_time_minutes = estimated_delivery_time_minutes

class Order_Item:
    def __init__(self,order_item_id,order_id,item_id,
                 category,quantity,price_per_unit,
                 total_price,weight_kg,volume_m3,
                 product_name,product_sku):
        self.order_item_id = order_item_id
        self.order_id = order_id
        self.item_id = item_id
        self.category = category
        self.quantity = quantity
        self.price_per_unit = price_per_unit
        self.total_price = total_price
        self.weight_kg = weight_kg
        self.volume_m3 = volume_m3
        self.product_name = product_name
        self.product_sku = product_sku

class Deliveries:
    def __init__(self,vehicle_id,type,license_plate,capacity_kg,current_load_kg,status,location_lat,location_lon,last_maintenance,fuel_efficiency_l_per_km,
                 next_maintenance_due,total_distance_traveled_km):
        self.vehicle_id = vehicle_id
        self.type = type
        self.license_plate = license_plate
        self.capacity_kg = capacity_kg
        self.current_load_kg = current_load_kg
        self.status = status
        self.location_lat = location_lat
        self.location_lon = location_lon
        self.last_maintenance = last_maintenance
        self.fuel_efficiency_l_per_km = fuel_efficiency_l_per_km  # Parametreyi burada düzeltin
        self.next_maintenance_due = next_maintenance_due
        self.total_distance_traveled_km = total_distance_traveled_km

class Vehicles:
    def __init__(self,vehicle_id,type,license_plate,capacity_kg,current_load_kg,status,location_lat,location_lon,last_maintenance,fuel_efficiency_l_per_km,
                 next_maintenance_due,total_distance_traveled_km):
        self.vehicle_id = vehicle_id
        self.type = type
        self.license_plate = license_plate
        self.capacity_kg = capacity_kg
        self.current_load_kg = current_load_kg
        self.status = status
        self.location_lat = location_lat
        self.location_lon = location_lon
        self.last_maintenance = last_maintenance
        self.fuel_efficiency_l_per_km = fuel_efficiency_l_per_km
        self.next_maintenance_due = next_maintenance_due
        self.total_distance_traveled_km = total_distance_traveled_km

class Kpis:
    def __init__(self, kpi_id, total_sales, total_deliveries, average_delivery_time_minutes, total_distance_traveled_km,
                 total_fuel_consumption_liters, average_order_value, top_category, feedback_avg_rating,
                 record_date, delivery_efficiency_score, customer_satisfaction_score):
        self.kpi_id = kpi_id
        self.total_sales = total_sales
        self.total_deliveries = total_deliveries
        self.average_delivery_time_minutes = average_delivery_time_minutes
        self.total_distance_traveled_km = total_distance_traveled_km
        self.total_fuel_consumption_liters = total_fuel_consumption_liters
        self.average_order_value = average_order_value
        self.top_category = top_category
        self.feedback_avg_rating = feedback_avg_rating
        self.record_date = record_date
        self.delivery_efficiency_score = delivery_efficiency_score
        self.customer_satisfaction_score = customer_satisfaction_score

    