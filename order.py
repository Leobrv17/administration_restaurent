import uuid
from datetime import datetime


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

    def request_new_order(self, customer_manager, dish_manager):
        # Sélection du client
        print("Sélectionnez un client pour la commande.")
        selected_customer = customer_manager.choose_customer("choisir pour la commande")
        if not selected_customer:
            print("Aucun client sélectionné.")
            return

        # Sélection des plats
        dishes = []
        print("Sélectionnez les plats pour la commande. Tapez 'fin' pour terminer la sélection.")
        while True:
            dish_name_fragment = input("Entrez un fragment du nom du plat (ou 'fin' pour terminer) : ")
            if dish_name_fragment.lower() == 'fin':
                break
            matching_dishes = dish_manager.find_dishes_by_name(dish_name_fragment)
            if not matching_dishes:
                print("Aucun plat trouvé avec ce fragment de nom.")
                continue
            for i, dish in enumerate(matching_dishes):
                print(f"{i + 1}: {dish}")
            dish_choice = int(input("Choisissez le numéro du plat à ajouter : ")) - 1
            if 0 <= dish_choice < len(matching_dishes):
                dishes.append(matching_dishes[dish_choice])
                print(f"Plat '{matching_dishes[dish_choice].name}' ajouté à la commande.")

        if not dishes:
            print("Aucun plat sélectionné pour la commande.")
            return

        # Création de la commande
        new_order = self.create_order(selected_customer, dishes)
        print(f"Nouvelle commande créée :\n{new_order}")
