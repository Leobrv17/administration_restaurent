import json
import uuid
import asking

class Customer:
    def __init__(self, last_name, first_name, phone_number):
        self.id = uuid.uuid4()
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
            customers_dict = [customer.__dict__ for customer in self.customers]
            for customer in customers_dict:
                customer['id'] = str(customer['id'])
            json.dump(customers_dict, file)

    def load_from_file(self, filename='customers.json'):
        try:
            with open(filename, 'r') as file:
                customers_dict = json.load(file)
                for customer_data in customers_dict:
                    customer = Customer(customer_data['last_name'], customer_data['first_name'],
                                        customer_data['phone_number'])
                    customer.id = uuid.UUID(customer_data['id'])
                    self.customers.append(customer)
        except FileNotFoundError:
            print(f"Aucun fichier trouvé nommé '{filename}'. Aucun client chargé.")
        except json.JSONDecodeError:
            print(f"Erreur de décodage JSON dans le fichier '{filename}'.")

    def find_customers_by_name_prefix(self, prefix):
        return [customer for customer in self.customers if customer.last_name.lower().startswith(prefix)]

    def choose_customer(self, action_description):
        prefix = input("Entrez les trois premières lettres du nom de famille du client : ").lower()
        matching_customers = self.find_customers_by_name_prefix(prefix)

        if not matching_customers:
            print("Aucun client trouvé avec ces lettres.")
            return None

        for i, customer in enumerate(matching_customers):
            print(f"{i + 1}: {customer}")

        try:
            choice = int(input(f"Entrez le numéro du client à {action_description} : ")) - 1
            if 0 <= choice < len(matching_customers):
                return matching_customers[choice]
            else:
                print("Numéro de client invalide.")
                return None
        except ValueError:
            print("Veuillez entrer un nombre valide.")
            return None

    def request_new_customer(self):
        print("Entre le nom du client")
        last_name = asking.get_str()

        print("Entre le prénom du client")
        first_name = asking.get_str()

        print("Entre le numéro de téléphone du client")
        phone_number = asking.get_phone_numb()

        self.create_customer(last_name, first_name, phone_number)
        self.save_to_file()

    def request_and_delete_customer(self):
        selected_customer = self.choose_customer("supprimer")
        if selected_customer:
            self.delete_customer(selected_customer.id)
            self.save_to_file()
            print(f"Le client {selected_customer.id} a été supprimé.")

    def request_and_update_customer(self):
        selected_customer = self.choose_customer("modifier")
        if selected_customer:
            print("Entrez les nouvelles informations du client (laissez vide pour ne pas modifier) :")
            new_last_name = input("Nouveau nom de famille : ")
            new_first_name = input("Nouveau prénom : ")
            new_phone_number = input("Nouveau numéro de téléphone : ")

            self.update_customer(selected_customer.id,
                                 last_name=new_last_name if new_last_name else selected_customer.last_name,
                                 first_name=new_first_name if new_first_name else selected_customer.first_name,
                                 phone_number=new_phone_number if new_phone_number else selected_customer.phone_number)
            self.save_to_file()
            print(f"Le client {selected_customer.id} a été mis à jour.")

    def request_and_show_customer(self):
        selected_customer = self.choose_customer("afficher")
        if selected_customer:
            print(f"Voici les informations du client sélectionné :\n{selected_customer}")
