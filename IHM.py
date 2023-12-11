from datetime import datetime
import asking
from customer import CustomerManager
from order import OrderManager
from dish import DishManager

def print_invalid_choice():
    print("Choix invalide. Veuillez entrer un numéro valide.")

def overview():
    print("Bienvenu dans votre menu pour gestion de commandes de votre restaurent")
    manager_cust = CustomerManager()
    manager_cust.load_from_file()
    manager_dish = DishManager()
    manager_dish.load_from_file()
    manager_order = OrderManager()
    manager_order.load_from_file(manager_cust, manager_dish)

    while True:
        print("\nQuelle action souhaitez-vous réaliser ?")
        print("1. Gestion clientèle\n2. Gestion de la carte\n3. Gestion des commandes\n4. Quitter")
        choix = input("Entrez le numéro de votre choix -> ")

        if choix == '1':
            menu_customer(manager_cust)
        elif choix == '2':
            menu_dish(manager_dish)
        elif choix == '3':
            menu_bill(manager_cust, manager_dish, manager_order)
        elif choix == '4':
            print("À demain.")
            break
        else:
            print_invalid_choice()

def menu_customer(manager):
    while True:
        print("\nOverview -> Gestion Clientèle\nQuelle action souhaitez-vous réaliser ?")
        print("1. Créer un nouveau client\n2. Supprimer un client existant\n3. Modifier un client existant\n4. Afficher un client existant\n5. Quitter")
        choix = input("Entrez le numéro de votre choix -> ")

        if choix == '1':
            manager.request_new_customer()
        elif choix == '2':
            manager.request_and_delete_customer()
        elif choix == '3':
            manager.request_and_update_customer()
        elif choix == '4':
            manager.request_and_show_customer()
        elif choix == '5':
            break
        else:
            print_invalid_choice()

def menu_dish(manager_dish):
    while True:
        print("\nOverview -> Gestion de la carte\nQuelle action souhaitez-vous réaliser ?")
        print("1. Créer un nouveau plat\n2. Supprimer un plat existant\n3. Modifier un plat existant\n4. Afficher un plat existant\n5. Quitter")
        choix = input("Entrez le numéro de votre choix -> ")

        if choix == '1':
            manager_dish.request_new_dish()
        elif choix == '2':
            manager_dish.request_and_delete_dish()
        elif choix == '3':
            manager_dish.request_and_update_dish()
        elif choix == '4':
            manager_dish.request_and_show_dish()
        elif choix == '5':
            break
        else:
            print_invalid_choice()

def menu_bill(manager_customer, manager_dish, manager_order):
    while True:
        print("\nOverview -> Gestion des commandes\nQuelle action souhaitez-vous réaliser ?")
        print("1. Créer une nouvelle commande\n2. Afficher les commandes d'un client\n3. Télécherger CSV\n4. Quitter")
        choix = input("Entrez le numéro de votre choix -> ")

        if choix == '1':
            manager_order.request_new_order(manager_customer, manager_dish)
        elif choix == '2':
            manager_order.show_customer_orders(manager_customer)
        elif choix == '3':
            manager_order.download_orders_as_csv()
        elif choix == '4':
            break
        else:
            print_invalid_choice()
