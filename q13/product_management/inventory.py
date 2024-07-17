class Inventory:
    def __init__(self):
        self.products = {}

    def add_product(self, product):
        self.products[product.product_id] = product

    def remove_product(self, product_id):
        if product_id in self.products:
            del self.products[product_id]

    def get_inventory(self):
        return {product_id: product.get_product_details() for product_id, product in self.products.items()}
