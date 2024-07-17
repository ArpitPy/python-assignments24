class Order:
    def __init__(self, order_id, products, customer):
        self.order_id = order_id
        self.products = products
        self.customer = customer
        self.status = 'Pending'

    def get_order_details(self):
        return {
            'Order ID': self.order_id,
            'Products': self.products,
            'Customer': self.customer,
            'Status': self.status
        }

    def update_status(self, status):
        self.status = status
