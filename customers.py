

import pdb
import json
import random
from pprint import pprint


try:
    customer_data = open('customers.json')
    customers = json.load(customer_data)
except Exception as e:
    print(e)
    customers = []
    print(customers)


class Customer():
    def __init__(self, user_id=None, name=None, phonenumber=None, address=None):
        self.user_id = user_id
        self.name = name
        self.phonenumber = phonenumber
        self.address = address

    def __str__(self):
        return (f'{self.user_id} {self.name} {self.phonenumber} {self.address}')


# reusable function to retrieve all customers
def get_all_customers():

    return customers

# reusable function to get single customer by Id


def get_single_customer(user_id):
    customer = {}
    for cust in customers:
        if cust['user_id'] == user_id:
            customer = cust
            break

    if not customer:
        print(f"No customer with id: {user_id}")
    return customer

# save customer function called after inputing customer details


def save_customer_to_file(data):

    new_customer = {}
    new_customer['user_id'] = random.randint(1000, 10000)
    new_customer["name"] = data['name']
    new_customer["phonenumber"] = data['phonenumber']
    new_customer["address"] = data['address']

    customer = Customer(new_customer['user_id'], new_customer['name'],
                        new_customer['phonenumber'], new_customer['address'])
    get_all_customers()

    customers.append(new_customer)

    with open('customers.json', 'w') as file_out:
        json.dump(customers, file_out, indent=0)

# adding a customer to db


def add_customer():

    continue_add = True
    while continue_add:

        name = input("Enter name: ")
        phonenumber = int(input("enter phonenumber: "))
        address = str(input("enter address: "))
        data = {
            "name": name,
            "phonenumber": phonenumber,
            "address": address

        }
        save_customer_to_file(data)
        choice = int(input("enter 1 to add another customer or 2 to exit: "))
        if choice == 2:
            continue_add = False
            print("Customer (s) added")

# updating customer details


def update_customer():
    pprint(get_all_customers())
    # calling the above function to be able to see the ids
    yourid = int(input("enter id: "))
    for cust in customers:
        # breakpoint()

        if cust['user_id'] == yourid:

            selection = int(
                input("enter 1 to change number or 2 to change address: "))
            # breakpoint()
            if selection == 1:
                newnumber = int(input("Enter new number: "))
                cust['phonenumber'] = newnumber

            elif selection == 2:

                newaddress = str(input("Enter new address: "))
                cust['address'] = newaddress
    # breakpoint()

    with open('customers.json', 'w') as file_out:
        json.dump(customers, file_out, indent=0)
        print("Customer updated successfully")

# deleting a customer


def delete_customer():
    get_all_customers()
    continue_delete = True
    while continue_delete:
        # get_all_customers()
        yourid = input("enter customer id: ")

        for i in range(len(customers)):
            if customers[i]['user_id'] == yourid:
                customers.remove(customers[i])
            break

        with open('customers.json', 'w') as file_out:
            json.dump(customers, file_out, indent=2)
            print("Customer deleted successfully")
        choice = int(
            input("enter 1 to delete another customer or 2 to exit: "))
        if choice == 2:
            continue_delete = False
            print("Customer (s) deleted")


# viewing customers in db and the total number of customers
def customers_in_db():
    pprint(get_all_customers())
    print(f"Total number of customers is: {(len(customers))}")


# function to get customer info(name, products bought and amount spent)
def get_customer_info():
    from purchases import get_purchases_by_cust_id
    from products import get_single_product

    cust_id = int(input("Enter customer id to view details: "))

    customer = get_single_customer(user_id=cust_id)
    if not customer:
        return
    customer_purchases = get_purchases_by_cust_id(cust_id)
    if not customer_purchases:
        return
    total_spent = 0
    products_bought = {}

    for purchase in customer_purchases:
        total_spent += purchase['total']

        for product in purchase['products']:
            product_info = get_single_product(product['product_id'])
            quantity = products_bought.get(product_info['name'], 0)
            quantity += product['quantity']
            products_bought.update({product_info['name']: quantity})
    print(f"Customer: {customer['name']}\n")
    print(f"Total spent: {total_spent}\n")
    print(f"Products bought\n")
    print(f"Name ----- Quantity\n")
    for key, value in products_bought.items():
        print(f"{key}     {value}")


# the submenu to navigate customer operations

def customer_menu():
    print("---------------------------")
    print("what would you like to do?")
    print("1:add customer")
    print("2:update customer")
    print("3:Delete customer")
    print("4:List all customers")
    print("5:Get customer information")
    print("6:Back to main menu")

    try:

        selection = int(input("enter your choice: "))
        if selection == 1:
            add_customer()
            customer_menu()
        elif selection == 2:
            update_customer()
            customer_menu()
        elif selection == 3:
            delete_customer()
            customer_menu()
        elif selection == 4:
            customers_in_db()
            customer_menu()
        elif selection == 5:
            get_customer_info()
            customer_menu()
        elif selection == 6:
            from main import menu
            menu()

        else:
            print("\n\tInvalid selection! Please try again.\t\t")
            from main import menu
            menu()
    except:
        print("\n\tInvalid input! Please enter a valid value.\t\t")
