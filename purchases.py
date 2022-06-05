import json
import pdb
from time import strftime
from uuid import uuid4
import datetime


from customers import get_all_customers
from products import get_all_products, edit_product






try:
    purchase_data = open('purchases.json')
    purchases = json.load(purchase_data)
except Exception as e:
    print(e)
    purchases = []


class Purchase:
    def __init__(self, purchase_id, user_id=None, product_id=None, quantity=None, date=None, amount=None):
        self.user_id = user_id
        self.product_id = product_id
        self.quantity = quantity
        self.purchase_id = purchase_id
        self.date=date
        self.amount=amount

    def __repr__(self) -> str:
        pass
        return f"{self.purchase_id}, {self.product_id}, {self.user_id}, {self.quantity}, {self.amount}, {self.date}, "


def save_purchase(data):
    #breakpoint()
    new_purchase = {
        'purchase_id': str(uuid4()),
        'user_id': data['user_id'],
        'product_id': data['product_id'],
        'quantity': data['quantity'],
        'date':datetime.datetime.now().strftime('%d-%m-%Y %H:%M:%S'),
        'amount':data['amount']
    }

    purchase = Purchase(purchase_id=new_purchase['purchase_id'], user_id=new_purchase['user_id'],
                        product_id=new_purchase['product_id'], quantity=new_purchase['quantity'], amount=new_purchase['amount'])

    purchases.append(new_purchase)
    with open('purchases.json', 'w') as pfile_out:
        json.dump(purchases, pfile_out, indent=2)


def validate_product_quantity(products, product_id, quantity):
    is_valid = True
    product_price=0
    for product in products:
        if product['product_id'] == product_id:
            if product['quantity'] < quantity:
                print("Quantity more than available stock")
                is_valid = False
                break
            else:
                product['quantity'] -= quantity
                product_price = product['price']
                edit_product(products)
    return is_valid,product_price


def add_purchase():
    products = get_all_products()
    customers = get_all_customers()


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
        choicepr=int(input("enter 1 to add another product or 2 to exit"))
            
        is_valid, product_price = validate_product_quantity(products, product_id, quantity)
        if is_valid:
            data['amount']= product_price*quantity
            
            save_purchase(data)
            print(purchases)
        choice = int(input("enter 1 to add another purchase or 2 to exit: "))
        if choice == 2:
            continue_add = False
            print("Purchase(s) added")


def purchase_menu():
    print("what would you like to do?")
    print("1:add purchase")
    print("2:see customer purchases")
    print("3:something else")

    selection = int(input("enter your choice: "))
    if selection == 1:
        add_purchase()
    elif selection == 2:
        pass
    elif selection == 3:
        pass






