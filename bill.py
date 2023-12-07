import uuid
from datetime import date

class Bill:
    def __init__(self, client, date, dishes=[]):
        self.id = uuid.uuid4()  # Génère un UUID unique pour l'ID de la facture
        self.client = client
        self.date = date
        self.dishes = dishes

    def __str__(self):
        return f"Bill ID: {self.id}\nClient: {self.client}\nDate: {self.date}\nDishes: {', '.join(self.dishes)}"

class BillManager:
    def __init__(self):
        self.bills = []

    def create_bill(self, client, date, dishes=[]):
        new_bill = Bill(client, date, dishes)
        self.bills.append(new_bill)
        return new_bill

    def read_bill(self, bill_id):
        for bill in self.bills:
            if bill.id == bill_id:
                return bill
        return None

    def update_bill(self, bill_id, client=None, date=None, dishes=None):
        bill = self.read_bill(bill_id)
        if bill:
            if client is not None:
                bill.client = client
            if date is not None:
                bill.date = date
            if dishes is not None:
                bill.dishes = dishes
            return True
        return False

    def delete_bill(self, bill_id):
        bill = self.read_bill(bill_id)
        if bill:
            self.bills.remove(bill)
            return True
        return False
