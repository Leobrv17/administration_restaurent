import json
import uuid

import asking


class Customer:
    def __init__(self, last_name, first_name, phone_number):
        self.id = uuid.uuid4()  # Génère un UUID unique pour l'ID du client
        self.last_name = last_name
        self.first_name = first_name
        self.phone_number = phone_number

    def __str__(self):
        return f"Customer ID: {self.id}\nLast Name: {self.last_name}\nFirst Name: {self.first_name}\nPhone Number: {self.phone_number}"


class CustomerManager:
    def __init__(self):
        self.customers = []

    def create_customer(self, last_name, first_name, phone_number):
        new_customer = Customer(last_name, first_name, phone_number)
        self.customers.append(new_customer)
        return new_customer

    def read_customer(self, customer_id):
        for customer in self.customers:
            if customer.id == customer_id:
                return customer
        return None

    def update_customer(self, customer_id, last_name=None, first_name=None, phone_number=None):
        customer = self.read_customer(customer_id)
        if customer:
            if last_name is not None:
                customer.last_name = last_name
            if first_name is not None:
                customer.first_name = first_name
            if phone_number is not None:
                customer.phone_number = phone_number
            return True
        return False

    def delete_customer(self, customer_id):
        customer = self.read_customer(customer_id)
        if customer:
            self.customers.remove(customer)
            return True
        return False

    def save_to_file(self, filename='customers.json'):
        with open(filename, 'w') as file:
            customers_dict = []
            for customer in self.customers:
                customer_data = customer.__dict__.copy()
                customer_data['id'] = str(customer.id)  # Convertir UUID en chaîne de caractères
                customers_dict.append(customer_data)

            json.dump(customers_dict, file)

    def load_from_file(self, filename='customers.json'):
        try:
            with open(filename, 'r') as file:
                customers_dict = json.load(file)
                for customer_data in customers_dict:
                    # Reconstruire chaque client à partir des données du dictionnaire
                    customer = Customer(customer_data['last_name'], customer_data['first_name'],
                                        customer_data['phone_number'])
                    customer.id = uuid.UUID(customer_data['id'])  # Convertir la chaîne de caractères en objet UUID
                    self.customers.append(customer)
        except FileNotFoundError:
            print(f"Aucun fichier trouvé nommé '{filename}'. Aucun client chargé.")
        except json.JSONDecodeError:
            print(f"Erreur de décodage JSON dans le fichier '{filename}'.")

    def request_new_customer(self):
        print("Entre le nom du client")
        last_name = asking.get_str()

        print("Entre le prénom du client")
        first_name = asking.get_str()

        print("Entre le numéro de téléphone du client")
        phone_numb = asking.get_phone_numb()

        self.create_customer(last_name, first_name, phone_numb)
        self.save_to_file()

    def request_and_delete_customer(self):
        prefix = input("Entrez les trois premières lettres du nom de famille du client : ").lower()
        matching_customers = []

        for i, customer in enumerate(self.customers):
            if customer.last_name.lower().startswith(prefix):
                print(
                    f"{i + 1}: Customer ID: {customer.id}, Last Name: {customer.last_name}, First Name: {customer.first_name}, Phone Number: {customer.phone_number}")
                matching_customers.append(customer)

        if not matching_customers:
            print("Aucun client trouvé avec ces lettres.")
            return

        try:
            choice = int(input("Entrez le numéro du client à supprimer : ")) - 1
            if 0 <= choice < len(matching_customers):
                selected_customer = matching_customers[choice]
                self.delete_customer(selected_customer.id)
                self.save_to_file()
                print(f"Le client {selected_customer.id} a été supprimé.")
            else:
                print("Numéro de client invalide.")
        except ValueError:
            print("Veuillez entrer un nombre valide.")

    def request_and_update_customer(self):
        prefix = input("Entrez les trois premières lettres du nom de famille du client : ").lower()
        matching_customers = []

        # Trouver les clients correspondants
        for i, customer in enumerate(self.customers):
            if customer.last_name.lower().startswith(prefix):
                print(
                    f"{i + 1}: Customer ID: {customer.id}, Last Name: {customer.last_name}, First Name: {customer.first_name}, Phone Number: {customer.phone_number}")
                matching_customers.append(customer)

        if not matching_customers:
            print("Aucun client trouvé avec ces lettres.")
            return

        try:
            choice = int(input("Entrez le numéro du client à modifier : ")) - 1
            if 0 <= choice < len(matching_customers):
                selected_customer = matching_customers[choice]

                # Demander les nouvelles informations du client
                print("Entrez les nouvelles informations du client (laissez vide pour ne pas modifier) :")
                new_last_name = input("Nouveau nom de famille : ")
                new_first_name = input("Nouveau prénom : ")
                new_phone_number = input("Nouveau numéro de téléphone : ")

                # Mise à jour du client
                self.update_customer(selected_customer.id,
                                     last_name=new_last_name if new_last_name else selected_customer.last_name,
                                     first_name=new_first_name if new_first_name else selected_customer.first_name,
                                     phone_number=new_phone_number if new_phone_number else selected_customer.phone_number)
                self.save_to_file()
                print(f"Le client {selected_customer.id} a été mis à jour.")
            else:
                print("Numéro de client invalide.")
        except ValueError:
            print("Veuillez entrer un nombre valide.")
