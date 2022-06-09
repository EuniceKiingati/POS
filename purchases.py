from itertools import product
from products import get_all_products, edit_product
from customers import add_customer, get_all_customers, get_single_customer, customers
import json
import pdb
from uuid import uuid4
import datetime


try:
    purchase_data = open('purchases.json')
    purchases = json.load(purchase_data)
except Exception as e:
    print(e)
    purchases = []



def validate_product_quantity(products, product_id, quantity):
    is_valid = True
    product_price = 0
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
    return is_valid, product_price


def checkout(purchase):
    invalid_amount = True
    while invalid_amount:
        cashgiven = int(input(" enter cash amount to pay: "))
        invalid_amount = (cashgiven < purchase['total'])
        if invalid_amount:
            print("insufficient funds. total amount is ksh. " +
                  str(purchase['total']))
            choice = int(input("\n1.Enter another amount\n2.Exit\n"))
            if choice == 1:
                continue
            else:
                print(" checkout cancelled; redirecting to purchase menu")
                make_purchase()
        else:
            balance = cashgiven-purchase["total"]
            #breakpoint()
            print(" here's your Receipt:")
            print("***********")
            print(f"Customer ID: {purchase['user_id']}\n")
            print("********* Products purchased***********\n")
            for product in purchase['products']:
                print(f"Product ID: {product['product_id']} {product['quantity']} {product['amount']}]")
            #print("products bought"+purchase.products)
            print(f"total is {purchase['total']}\n")
            print(f"Cash given is {cashgiven}\n")
            print(f"Balance is {balance}\n")
            print("Purchase complete")
            print("Thank you for shopping with us!")



def make_purchase():
    products = get_all_products()
    get_all_customers()

    continue_add = True
    youruser_id = int(input("Enter user_id: "))
    is_valid = False
    for customer in customers:
        if customer['user_id'] == youruser_id:
            is_valid = True
    if not is_valid:

        print("customer does not exist")
        choice = int(input("""Press 1: to re-enter id or 2: to add customer """
                           ))
        if choice == 1:
            make_purchase()
        elif choice == 2:
            add_customer()
    else:
        purchase = {
            "purchase_id": str(uuid4()),
            "date": datetime.datetime.now().strftime('%d-%m-%Y %H:%M:%S'),
            "total": 0,
            "user_id": youruser_id,
            "products": []
        }

        while continue_add:
            product_id = int(input("Enter product_id: "))
            quantity = int(input("Enter quantity: "))

            product_data = {
                "product_id": product_id,
                "quantity": quantity,

            }

            is_valid, product_price = validate_product_quantity(
                products, product_id, quantity)
            if is_valid:
                amount = product_price*quantity
                purchase['total'] += amount
                product_data['amount'] = amount
                purchase['products'].append(product_data)

            choice = int(
                input("enter 1 to add another purchase or 2 proceed to checkout: "))
            if choice == 2:
                purchases.append(purchase)
                print("Total is:" + str(purchase["total"]))
                # checkout()

                with open('purchases.json', 'w') as pfile_out:
                    json.dump(purchases, pfile_out, indent=2)
                    # save_purchase(purchase)
                continue_add = False
                print("Purchase(s) added")
                # purchase_menu()

        checkout(purchase)

#checkout(purchases[0])

def get_all_purchases():
    print(purchases)
    return purchases



def get_customer_info():  # need to add ability to see name, annd product names..make UI better

    customer_id=int(input("Enter customer id to view customer: "))
    get_single_customer(user_id=customer_id)
   
    for purchase in purchases:
        if purchase['user_id']==customer_id:
            print(purchase['products'])




def purchase_menu():
    print("what would you like to do?")
    print("1:Make purchase")
    print("2:List all purchases")
    print("3:Get specific purchase")
    print("4:Get customer info")

    selection = int(input("enter your choice: "))
    if selection == 1:
        make_purchase()
    elif selection == 2:
        get_all_purchases()
    elif selection == 4:
        get_customer_info()
    
   # elif selection == 4:
        #get_customer_info()
