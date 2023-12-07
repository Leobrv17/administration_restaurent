import uuid

class Dish:
    def __init__(self, name, description, price, category):
        self.id = uuid.uuid4()  # Génère un UUID unique pour l'ID du plat
        self.name = name
        self.description = description
        self.price = price
        self.category = category

    def __str__(self):
        return f"Dish ID: {self.id}\nName: {self.name}\nDescription: {self.description}\nPrice: {self.price}\nCategory: {self.category}"

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
