

import pdb
import json
import random
import pprint

try:
    product_data = open('products.json')
    products = json.load(product_data)
except Exception as e:
    print(e)
    products = []


class Product():

    def __init__(self, product_id=None, name=None, quantity=None, price=None):
        self.product_id = product_id
        self.name = name
        self.quantity = quantity
        self.price = price

    def __str__(self):
        return (f'{self.product_id} {self.name} {self.quantity} {self.price}')


def get_all_products():
    pprint.pprint(products)
    return products

def get_single_product(product_id):
    product = {}
    for prod in products:
        if prod['product_id'] == product_id:
            product= prod
            break

    if not product:
        print(f"No customer with id: {product_id}")
    return product


def save_product(data):
    new_product = {}
    new_product['product_id'] = random.randint(20000, 90000)
    new_product["name"] = data['name']
    new_product["quantity"] = data['quantity']
    new_product["price"] = data['price']
    product = Product(new_product['product_id'], new_product['name'],
                      new_product['quantity'], new_product['price'])

    get_all_products()
    products.append(new_product)

    with open('products.json', 'w') as pfile_out:
        json.dump(products, pfile_out, indent=2)

    #print("so far so good")


def add_product():

    continue_add = True
    while continue_add:

        name = input("Enter name: ")
        quantity = int(input("enter quantity: "))
        price = int(input("enter price: "))
        data = {
            "name": name,
            "quantity": quantity,
            "price": price

        }
        save_product(data)
        print(products)
        choice = int(input("enter 1 to add another product or 2 to exit: "))
        if choice == 2:
            continue_add = False
            print("Product (s) added")

def search_product():
    prodid = input("enter product-id: ")
    for prod in products:
        # breakpoint()

        if prod['product_id'] == prodid:
            print(prod)

def edit_product(data):

    with open('products.json', 'w') as pfile_out:
        json.dump(data, pfile_out, indent=2)
        print("Product updated successfully")


def update_product():
    get_all_products()  # calling this function to be able to see the id's
    prodid = input("enter product-id: ")
    for prod in products:
        # breakpoint()

        if prod['product_id'] == prodid:

            newprice = int(input("Enter new price: "))

            prod['price'] = newprice
            # breakpoint()

    edit_product(products)


def delete_product():
    get_all_products()
    prodid = input("enter product id: ")

    for i in range(len(products)):
        if products[i]['product_id'] == prodid:
            products.remove(products[i])
            break
    # breakpoint()
    with open('products.json', 'w') as pfile_out:
        json.dump(products, pfile_out, indent=2)
        print("Product deleted successfully")


def product_menu():
    print("what would you like to do?")
    print("1:add product")
    print("2:update product")
    print("3:Delete product")
    print("4:List all customers")

    selection = int(input("enter your choice: "))
    if selection == 1:
        add_product()
    elif selection == 2:
        update_product()
    elif selection == 3:
        delete_product()
    elif selection==4:
        get_all_products()
    elif selection==5:
        search_product()

        

