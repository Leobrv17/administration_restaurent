import uuid
import json


class Order:
    def __init__(self, last_name, first_name, phone_number):
        self.id = uuid.uuid4()  # Génère un UUID unique pour l'ID de la commande
        self.last_name = last_name
        self.first_name = first_name
        self.phone_number = phone_number

    def __str__(self):
        return f"Order ID: {self.id}\nLast Name: {self.last_name}\nFirst Name: {self.first_name}\nPhone Number: {self.phone_number}"

class OrderManager:
    def __init__(self):
        self.orders = []

    def create_order(self, last_name, first_name, phone_number):
        new_order = Order(last_name, first_name, phone_number)
        self.orders.append(new_order)
        return new_order

    def read_order(self, order_id):
        for order in self.orders:
            if order.id == order_id:
                return order
        return None

    def update_order(self, order_id, last_name=None, first_name=None, phone_number=None):
        order = self.read_order(order_id)
        if order:
            if last_name is not None:
                order.last_name = last_name
            if first_name is not None:
                order.first_name = first_name
            if phone_number is not None:
                order.phone_number = phone_number
            return True
        return False

    def delete_order(self, order_id):
        order = self.read_order(order_id)
        if order:
            self.orders.remove(order)
            return True
        return False

    def save_to_file(self, filename='orders.json'):
        with open(filename, 'w') as file:
            orders_dict = []
            for order in self.orders:
                order_data = order.__dict__.copy()
                order_data['id'] = str(order.id)  # Convertir UUID en chaîne de caractères
                orders_dict.append(order_data)

            json.dump(orders_dict, file)
    def load_from_file(self, filename='orders.json'):
        try:
            with open(filename, 'r') as file:
                orders_dict = json.load(file)
                for order_data in orders_dict:
                    # Reconstruire chaque commande à partir des données du dictionnaire
                    order = Order(order_data['last_name'], order_data['first_name'], order_data['phone_number'])
                    order.id = uuid.UUID(order_data['id'])  # Convertir la chaîne de caractères en objet UUID
                    self.orders.append(order)
        except FileNotFoundError:
            print(f"Aucun fichier trouvé nommé '{filename}'. Aucune commande chargée.")
        except json.JSONDecodeError:
            print(f"Erreur de décodage JSON dans le fichier '{filename}'.")