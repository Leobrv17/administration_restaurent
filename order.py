from datetime import datetime
import uuid

class Order:
    def __init__(self, customer, dishes):
        self.id = uuid.uuid4()
        self.customer = customer  # Suppose que customer est un objet Customer
        self.dishes = dishes  # Liste d'objets Dish
        self.created_at = datetime.now()

    def __str__(self):
        dishes_str = ', '.join(dish.name for dish in self.dishes)
        return (f"Order ID: {self.id}\nCustomer: {self.customer.first_name} {self.customer.last_name}\n"
                f"Dishes: {dishes_str}\nCreated At: {self.created_at.strftime('%Y-%m-%d %H:%M:%S')}")

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
