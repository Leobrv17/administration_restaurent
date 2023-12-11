import uuid

class Order:
    def __init__(self, customer, dishes=None):
        self.id = uuid.uuid4()
        self.customer = customer
        self.dishes = dishes if dishes is not None else []

    def __str__(self):
        dishes_str = ', '.join([dish.name for dish in self.dishes])
        return f"Order ID: {self.id}\nCustomer: {self.customer.last_name}, {self.customer.first_name}\nDishes: {dishes_str}"

class OrderManager:
    def __init__(self):
        self.orders = []

    def create_order(self, customer, dishes):
        new_order = Order(customer, dishes)
        self.orders.append(new_order)
        return new_order

    def read_order(self, order_id):
        for order in self.orders:
            if order.id == order_id:
                return order
        return None

    def update_order(self, order_id, customer=None, dishes=None):
        order = self.read_order(order_id)
        if order:
            if customer is not None:
                order.customer = customer
            if dishes is not None:
                order.dishes = dishes
            return True
        return False

    def delete_order(self, order_id):
        order = self.read_order(order_id)
        if order:
            self.orders.remove(order)
            return True
        return False

    def list_orders(self):
        for order in self.orders:
            print(order)
