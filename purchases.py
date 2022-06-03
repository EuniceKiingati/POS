import json
import pdb
from uuid import uuid4

from customers import get_all_customers
from products import get_all_products, edit_product

products = get_all_products()
customers = get_all_customers()

try:
    purchase_data = open('purchases.json')
    purchases = json.load(purchase_data)
except Exception as e:
    print(e)
    purchases = []


class Purchase:
    def __init__(self, purchase_id, user_id=None, product_id=None, quantity=None):
        self.user_id = user_id
        self.product_id = product_id
        self.quantity = quantity
        self.purchase_id = purchase_id

    def __repr__(self) -> str:
        pass
        return f"{self.purchase_id}, {self.product_id}, {self.user_id}, {self.quantity}"


def save_purchase(data):
    new_purchase = {
        'purchase_id': str(uuid4()),
        'user_id': data['user_id'],
        'product_id': data['product_id'],
        'quantity': data['quantity']
    }

    purchase = Purchase(purchase_id=new_purchase['purchase_id'], user_id=new_purchase['user_id'],
                        product_id=new_purchase['product_id'], quantity=new_purchase['quantity'])

    purchases.append(new_purchase)
    with open('purchases.json', 'w') as pfile_out:
        json.dump(purchases, pfile_out, indent=2)


def validate_product_quantity(product_id, quantity):
    is_valid = True
    for product in products:
        if product['product_id'] == product_id:
            if product['quantity'] < quantity:
                print("Quantity more than available")
                is_valid = False
                break
            else:
                product['quantity'] -= quantity
                edit_product(products)
    return is_valid


def add_purchase():

    continue_add = True
    while continue_add:
        user_id = input("Enter user_id: ")
        product_id = str(input("Enter product_id: "))
        quantity = int(input("Enter quantity: "))
        data = {
            "user_id": user_id,
            "product_id": product_id,
            "quantity": quantity
        }
        if validate_product_quantity(product_id, quantity):
            save_purchase(data)
            print(purchases)
        choice = int(input("enter 1 to add another purchase or 2 to exit: "))
        if choice == 2:
            continue_add = False
            print("Purchase(s) added")


add_purchase()
