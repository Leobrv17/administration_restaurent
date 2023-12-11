def get_str():
    while True:
        chaine = input(">>>")
        if isinstance(chaine, str) and chaine :
            return chaine
        else:
            print("Entrée invalide, veuillez réessayer.")

def get_phone_numb():
    while True:
        numero = input(">>>")
        numero_sans_espaces = numero.replace(" ", "")
        if numero_sans_espaces.isdigit() and len(numero_sans_espaces) == 10:
            return numero_sans_espaces
        else:
            print("Format invalide. Le numéro doit contenir 10 chiffres.")