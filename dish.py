import json
import uuid


class Dish:
    def __init__(self, name, description, price, category):
        self.id = uuid.uuid4()
        self.name = name
        self.description = description
        self.price = price
        self.category = category

    def __str__(self):
        return f"Dish ID: {self.id}\nName: {self.name}\nDescription: {self.description}\nPrice: {self.price}\nCategory: {self.category}"

    def to_dict(self):
        return {
            "id": str(self.id),
            "name": self.name,
            "description": self.description,
            "price": self.price,
            "category": self.category
        }

    @staticmethod
    def from_dict(data):
        dish = Dish(data['name'], data['description'], data['price'], data['category'])
        dish.id = uuid.UUID(data['id'])
        return dish


class DishManager:
    def __init__(self):
        self.dishes = []

    def create_dish(self, name, description, price, category):
        new_dish = Dish(name, description, price, category)
        self.dishes.append(new_dish)
        return new_dish

    def read_dish(self, dish_id):
        for dish in self.dishes:
            if dish.id == dish_id:
                return dish
        return None

    def update_dish(self, dish_id, name=None, description=None, price=None, category=None):
        dish = self.read_dish(dish_id)
        if dish:
            if name is not None:
                dish.name = name
            if description is not None:
                dish.description = description
            if price is not None:
                dish.price = price
            if category is not None:
                dish.category = category
            return True
        return False

    def delete_dish(self, dish_id):
        dish = self.read_dish(dish_id)
        if dish:
            self.dishes.remove(dish)
            return True
        return False

    def save_to_file(self, filename='dishes.json'):
        with open(filename, 'w') as file:
            dishes_dict = [dish.to_dict() for dish in self.dishes]
            json.dump(dishes_dict, file)

    def load_from_file(self, filename='dishes.json'):
        try:
            with open(filename, 'r') as file:
                dishes_dict = json.load(file)
                self.dishes = [Dish.from_dict(dish_data) for dish_data in dishes_dict]
        except FileNotFoundError:
            print(f"Aucun fichier trouvé nommé '{filename}'. Aucun plat chargé.")
        except json.JSONDecodeError:
            print(f"Erreur de décodage JSON dans le fichier '{filename}'.")

    def find_dishes_by_name(self, name_fragment):
        return [dish for dish in self.dishes if name_fragment.lower() in dish.name.lower()]

    def request_new_dish(self):
        print("Entrez les détails du nouveau plat.")

        name = input("Nom du plat : ")
        description = input("Description : ")
        price = float(input("Prix : "))
        category = input("Catégorie : ")

        new_dish = self.create_dish(name, description, price, category)
        self.save_to_file()
        print(f"Nouveau plat ajouté : \n{new_dish}")

    def choose_dish(self, action_description):
        name_fragment = input("Entrez un fragment du nom du plat : ").lower()
        matching_dishes = self.find_dishes_by_name(name_fragment)

        if not matching_dishes:
            print("Aucun plat trouvé avec ce fragment de nom.")
            return None

        for i, dish in enumerate(matching_dishes):
            print(f"{i + 1}: {dish}")

        try:
            choice = int(input(f"Entrez le numéro du plat à {action_description} : ")) - 1
            if 0 <= choice < len(matching_dishes):
                return matching_dishes[choice]
            else:
                print("Numéro de plat invalide.")
                return None
        except ValueError:
            print("Veuillez entrer un nombre valide.")
            return None

    def request_and_update_dish(self):
        selected_dish = self.choose_dish("modifier")
        if selected_dish:
            print("Entrez les nouvelles informations du plat (laissez vide pour ne pas modifier) :")
            new_name = input("Nouveau nom : ")
            new_description = input("Nouvelle description : ")
            new_price = input("Nouveau prix : ")
            new_category = input("Nouvelle catégorie : ")

            self.update_dish(selected_dish.id,
                             name=new_name if new_name else selected_dish.name,
                             description=new_description if new_description else selected_dish.description,
                             price=new_price if new_price else selected_dish.price,
                             category=new_category if new_category else selected_dish.category)
            self.save_to_file()
            print(f"Le plat {selected_dish.id} a été mis à jour.")

    def request_and_delete_dish(self):
        selected_dish = self.choose_dish("supprimer")
        if selected_dish:
            self.delete_dish(selected_dish.id)
            self.save_to_file()
            print(f"Le plat {selected_dish.id} a été supprimé.")

    def request_and_show_dish(self):
        selected_dish = self.choose_dish("afficher")
        if selected_dish:
            print(f"Voici les informations du plat sélectionné :\n{selected_dish}")
