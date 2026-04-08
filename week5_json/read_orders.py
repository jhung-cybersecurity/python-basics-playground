import json

file = open("orders.json", "r")
orders = json.load(file)
file.close()

shipped_count = 0
total_amount = 0 

for order in orders:
    print("Order:", order["order_id"], "| Customer:", order["customer"])

    total_amount += order["amount"]

    if order["shipped"]:
        shipped_count += 1

print("Shipped orders:", shipped_count)
print("Total amount:", total_amount)


for unshipped in orders:
    if not unshipped["shipped"]:
        print("Unshipped order:", unshipped["order_id"])


