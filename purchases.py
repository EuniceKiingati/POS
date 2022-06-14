from itertools import product
from products import get_all_products, edit_product
from customers import add_customer, get_all_customers, get_single_customer, customers
import json
import pdb
from uuid import uuid4
import datetime
from pprint import pprint


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

           

        
            # breakpoint()
            print("\t****Here's your Receipt***")
            print("\t***********")
            print(f"\tCustomer ID: {purchase['user_id']}")
            print("\t--Products purchased are-- ")
            for product in purchase['products']:
                print(
                    f"\t\tProduct ID: {product['product_id']} {product['quantity']} {product['amount']}]")
            
            print(f"\tTotal is {purchase['total']}")
            print(f"\tCash given is {cashgiven}")
            print(f"\tBalance is {balance}")
            print("\t***Purchase complete***")
            print("\t***Thank you for shopping with us!***\n")


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
               

                with open('purchases.json', 'w') as pfile_out:
                    json.dump(purchases, pfile_out, indent=2)
                   
                continue_add = False
                print("Purchase(s) added")
                

        checkout(purchase)


#function to get all purchases
def get_all_purchases():
    print(purchases)
    return purchases

#reusable function to get purchase by customer id
def get_purchases_by_cust_id(user_id):
    purchaselist = []
    for purchase in purchases:
        if purchase['user_id'] == user_id:
            purchaselist.append(purchase)
    if not purchaselist:
        print(f"No purchase with id: {user_id}")
    return purchaselist

#reusable function to get purchase by purchase id 
def get_purchase_by_purchase_id():
    pprint(get_all_purchases())
    purchaseid=input("enter purchase-id: ")
    for purchase in purchases:
        if purchase['purchased_id']==purchaseid:
            return purchase

#function to search purchase buy customer id or purchase id
def search_purchase():
    print("How do you want to search")
    selection=int(input("Enter 1 to search by product_id or 2 to search by customer_id: "))
    if selection==1:
        yourproductid=int(input("Enter the purchasee id to view purchase: "))
        purchase=get_purchase_by_purchase_id(product_id=yourproductid)
        if not purchase:
            return
    elif selection==2:
        yourcustomerid=int(input("Enter customer id to view purchase: "))
        purchasecust=pprint(get_purchases_by_cust_id(user_id=yourcustomerid))
        if not purchasecust:
             return

def purchase_menu():
    print("\t***Purchase Menu***")
    print("\t1:Make purchase")
    print("\t2:List all purchases")
    print("\t3:Get specific purchase")
    print("\t4:Back to main menu")

    try:
        selection = int(input("enter your choice: "))
        if selection == 1:
            make_purchase()
            purchase_menu()
        elif selection == 2:
            get_all_purchases()
            purchase_menu()
        elif selection == 3:
            search_purchase()
            purchase_menu()
        elif selection==4:
            from main import menu
            menu()
    except:
        print("\tInvalid input!! ")
  




