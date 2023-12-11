from datetime import datetime

import asking
from order import OrderManager


def overview():
    print("Bienvenu dans votre menu pour gestion de commandes de votre restaurent")
    while True:
        print("Quelle action souhaitez-vous réaliser ?")
        print("1. Gestion clientèle")
        print("2. Gestion de la carte")
        print("3. Gestion des commandes")
        print("4. Récupération des bilans quotidiens")
        print("5. Plus d'informations")
        print("6. Quitter")

        choix = input("Entrez le numéro de votre choix -> ")

        if choix == '1':
            menu_customer()
        elif choix == '2':
            menu_dish()
        elif choix == '3':
            menu_bill()
        elif choix == '4':
            get_bills_per_day_csv()
        elif choix == '5':
            print("Option 'Plus d'informations' vous permet d'en savoir plus sur les fonctionnalités.")
        elif choix == '6':
            print("À demain.")
            break
        else:
            print("Choix invalide. Veuillez entrer un numéro valide.")


def menu_customer():
    while True:
        print("Overview -> Gestion Clientèle")
        print("Quelle action souhaitez-vous réaliser ?")
        print("1. Créer un nouveau client")
        print("2. Supprimer un client existant")
        print("3. Modifier un client existant")
        print("4. Afficher un client existant")
        print("5. Plus d'informations")
        print("6. Quitter")

        choix = input("Entrez le numéro de votre choix -> ")

        if choix == '1':
            manager = OrderManager()
            print("Entre le nom du client")
            last_name = asking.get_str()

            print("Entre le prénom du client")
            first_name = asking.get_str()

            print("Entre le numéro de téléphone du client")
            phone_numb = asking.get_phone_numb()

            new_order = manager.create_order(last_name, first_name, phone_numb)
            print(new_order)

            pass
        elif choix == '2':
            # Fonction du menu de suppression de client
            pass
        elif choix == '3':
            # Fonction du menu de modification d'un client
            pass
        elif choix == '4':
            # Fonction du menu d'affichage de client existant
            pass
        elif choix == '5':
            print(
                "Option 'Plus d'informations' vous permet d'en savoir plus sur les fonctionnalités de gestion clientèle.")
        elif choix == '6':
            print("Retour à l'overview")
            break
        else:
            print("Choix invalide. Veuillez entrer un numéro valide.")


def menu_dish():
    while True:
        print("Overview -> Gestion de la carte")
        print("Quelle action souhaitez-vous réaliser ?")
        print("1. Créer un nouveau plat")
        print("2. Supprimer un plat existant")
        print("3. Modifier un plat existant")
        print("4. Afficher un plat existant")
        print("5. Plus d'informations")
        print("6. Quitter")

        choix = input("Entrez le numéro de votre choix -> ")

        if choix == '1':
            # Fonction du menu de nouveau plat
            pass
        elif choix == '2':
            # Fonction du menu de suppression de plat
            pass
        elif choix == '3':
            # Fonction du menu de modification d'un plat
            pass
        elif choix == '4':
            # Fonction du menu d'affichage de plat existant
            pass
        elif choix == '5':
            print(
                "Option 'Plus d'informations' vous permet d'en savoir plus sur les fonctionnalités de gestion de la carte.")
        elif choix == '6':
            print("Retour à l'overview")
            break
        else:
            print("Choix invalide. Veuillez entrer un numéro valide.")


def menu_bill():
    while True:
        print("Overview -> Gestion des commandes")
        print("Quelle action souhaitez-vous réaliser ?")
        print("1. Créer une nouvelle commande")
        print("2. Supprimer une commande existante")
        print("3. Clôturer une commande existante")
        print("4. Afficher une commande existante")
        print("5. Plus d'informations")
        print("6. Quitter")

        choix = input("Entrez le numéro de votre choix -> ")

        if choix == '1':
            # Fonction du menu de création d'une nouvelle commande
            pass
        elif choix == '2':
            # Fonction du menu de suppression d'une commande
            pass
        elif choix == '3':
            # Fonction du menu de clôture d'une commande
            pass
        elif choix == '4':
            # Fonction du menu d'affichage des commandes
            pass
        elif choix == '5':
            print(
                "Option 'Plus d'informations' vous permet d'en savoir plus sur les fonctionnalités de gestion des commandes.")
        elif choix == '6':
            print("Retour à l'overview")
            break
        else:
            print("Choix invalide. Veuillez entrer un numéro valide.")


def get_bills_per_day_csv():
    while True:
        date_str = input("Veuillez entrer une date au format YYYY-MM-DD : ")

        try:
            date_obj = datetime.strptime(date_str, "%Y-%m-%d")
            print("Vous avez entré la date :", date_obj)

            # Demander la confirmation de la date
            confirmation = input("Confirmez-vous la date ? (O/N) : ").strip().lower()
            if confirmation == 'o':
                return date_obj
            else:
                print("Saisie annulée.")
        except ValueError:
            print("Format de date incorrect. Assurez-vous d'utiliser le format YYYY-MM-DD.")
