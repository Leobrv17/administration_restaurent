import json
import uuid
from datetime import datetime
import csv


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

    def save_to_file(self, filename='orders.json'):
        with open(filename, 'w') as file:
            orders_data = []
            for order in self.orders:
                order_data = {
                    "id": str(order.id),
                    "customer_id": str(order.customer.id),
                    "dishes_ids": [str(dish.id) for dish in order.dishes],
                    "created_at": order.created_at.strftime('%Y-%m-%d %H:%M:%S')
                }
                orders_data.append(order_data)
            json.dump(orders_data, file)

    def load_from_file(self, customer_manager, dish_manager, filename='orders.json'):
        try:
            with open(filename, 'r') as file:
                orders_data = json.load(file)
                for data in orders_data:
                    customer = customer_manager.read_customer(uuid.UUID(data['customer_id']))
                    dishes = [dish_manager.read_dish(uuid.UUID(dish_id)) for dish_id in data['dishes_ids']]
                    order = Order(customer, dishes)
                    order.id = uuid.UUID(data['id'])
                    order.created_at = datetime.strptime(data['created_at'], '%Y-%m-%d %H:%M:%S')
                    self.orders.append(order)
        except FileNotFoundError:
            print(f"Aucun fichier trouvé nommé '{filename}'. Aucune commande chargée.")
        except json.JSONDecodeError:
            print(f"Erreur de décodage JSON dans le fichier '{filename}'.")

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
        self.save_to_file()
        print(f"Nouvelle commande créée :\n{new_order}")

    def show_customer_orders(self, customer_manager):
        # Utilisation de la méthode de sélection de client
        selected_customer = customer_manager.choose_customer("voir les commandes")
        if not selected_customer:
            print("Aucun client sélectionné.")
            return

        # Filtrer et afficher les commandes pour le client sélectionné
        customer_orders = [order for order in self.orders if order.customer.id == selected_customer.id]
        if not customer_orders:
            print(
                f"Aucune commande trouvée pour le client {selected_customer.first_name} {selected_customer.last_name}.")
            return

        print(f"Commandes pour {selected_customer.first_name} {selected_customer.last_name}:")
        for order in customer_orders:
            print(order)

    def download_orders_as_csv(self):
        date_str = input("Entrez la date pour laquelle télécharger les commandes (format YYYY-MM-DD) : ")
        try:
            selected_date = datetime.strptime(date_str, '%Y-%m-%d').date()
        except ValueError:
            print("Format de date invalide.")
            return

        filtered_orders = [order for order in self.orders if order.created_at.date() == selected_date]

        if not filtered_orders:
            print("Aucune commande trouvée pour cette date.")
            return

        filename = f"orders_{date_str}.csv"
        with open(filename, mode='w', newline='', encoding='utf-8') as file:
            csv_writer = csv.writer(file)
            headers = ['Order ID', 'Customer Name', 'Dishes', 'Total Price', 'Created At']
            csv_writer.writerow(headers)

            for order in filtered_orders:
                # Collecter les informations de la commande
                order_id = str(order.id)
                customer_name = f"{order.customer.first_name} {order.customer.last_name}"
                dishes = ', '.join([dish.name for dish in order.dishes])
                total_price = sum(dish.price for dish in order.dishes)
                created_at = order.created_at.strftime('%Y-%m-%d %H:%M:%S')

                # Écrire la ligne dans le fichier CSV
                csv_writer.writerow([order_id, customer_name, dishes, total_price, created_at])

        print(f"Les commandes ont été téléchargées dans '{filename}'.")
