# example_usage.py

from product_management.product import Product
from product_management.inventory import Inventory
from order_processing.order import Order
from order_processing.payment import Payment

# Create products
product1 = Product(1, "Laptop", 1000.00, 10)
product2 = Product(2, "Smartphone", 500.00, 20)

# Add products to inventory
inventory = Inventory()
inventory.add_product(product1)
inventory.add_product(product2)

print("Inventory Details:")
print(inventory.get_inventory())

# Create an order
order = Order(1, [product1.get_product_details(), product2.get_product_details()], "John Doe")

print("\nOrder Details:")
print(order.get_order_details())

# Process payment
payment = Payment(order.order_id, 1500.00, "Credit Card")
payment.process_payment()

print("\nPayment Status:")
print(payment.get_payment_status())

# Update order status
order.update_status("Shipped")

print("\nUpdated Order Details:")
print(order.get_order_details())
