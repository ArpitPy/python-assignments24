class Payment:
    def __init__(self, order_id, amount, payment_method):
        self.order_id = order_id
        self.amount = amount
        self.payment_method = payment_method
        self.status = 'Pending'

    def process_payment(self):
        # Implement payment processing logic here
        self.status = 'Completed'

    def get_payment_status(self):
        return self.status
