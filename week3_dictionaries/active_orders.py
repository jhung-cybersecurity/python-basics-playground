orders = [
    {"order_id": 101, "item": "Keyboard", "status": "shipped"},
    {"order_id": 102, "item": "Mouse", "status": "processing"},
    {"order_id": 103, "item": "Monitor", "status": "shipped"},
    {"order_id": 104, "item": "Laptop Stand", "status": "processing"}
]

def count_processing_orders(orders):
    count = 0
    for order in orders:
        if order["status"] == "processing":
            count = count + 1
    
    return count
    
print("Processing orders:", count_processing_orders(orders))
