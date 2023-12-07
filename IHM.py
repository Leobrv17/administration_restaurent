def start_app():
    print("Bienvenue dans votre application de gestion pour votre restaurant.")
    overview()

def overview():
    while True:
        print("Quelle action souhaitez-vous réaliser ?")
        print("1. Gestion clientèle")
        print("2. Administrer la carte")
        print("3. Gestion des commendes")
        print("4. Récupération des bilans quotidiens")
        print("5. Plus d'informations")
        print("5. Quitter")

        choix = input("Entrez le numéro de votre choix -> ")

        if choix == '1':
            #fonction du menu de gestion des client
        elif choix == '2':
            #fonction du menu d'administration de la carte
        elif choix == '3':
            #fonction du menu de gestion des commendes
        elif choix == '4':
            # fonction du menu de recupertion de commendes quotidiens
        elif choix == '5':
            # fonction du menu de support utilisateur
        elif choix == '4':
            print("à demain.")
            break
        else:
            print("Choix invalide. Veuillez entrer un numéro valide.")

def menu_customer():
    while True:
        print("Quelle action souhaitez-vous réaliser ?")
        print("1. Créer un nouveau client")
        print("2. Suprimer un client existant")
        print("3. Modifier un client existant")
        print("4. afficher un client existant")
        print("5. Plus d'informations")
        print("5. Quitter")

        choix = input("Entrez le numéro de votre choix -> ")

        if choix == '1':
            #fonction du menu de nouveau client
        elif choix == '2':
            #fonction du menu de supression de client
        elif choix == '3':
            #fonction du menu de modification d'un client
        elif choix == '4':
            # fonction du menu d 'affichage de client existatant
        elif choix == '5':
            # fonction du menu de support utilisateur
        elif choix == '4':
            print("à demain.")
            break
        else:
            print("Choix invalide. Veuillez entrer un numéro valide.")