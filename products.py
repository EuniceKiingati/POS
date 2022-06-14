

import pdb
import json
import random
from pprint import pprint

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

#reusable function  to get all products
def get_all_products():
    return products

#reusable function to get single product
def get_single_product(product_id):
    product = {}
    for prod in products:
        if prod['product_id'] == product_id:
            product = prod

    if not product:
        print(f"No product with id: {product_id}")
    return product

#function to save product data to file
def save_product_to_file(data):
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

    # print("so far so good")

#function to add product details
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
        save_product_to_file(data)
        print(products)
        choice = int(input("enter 1 to add another product or 2 to exit: "))
        if choice == 2:
            continue_add = False
            print("Product (s) added")

#function to view product by id
def search_product():
    prodid = input("enter product-id to view product: ")
    print(get_single_product(product_id=prodid))

#edits data in file
def edit_product(data):

    with open('products.json', 'w') as pfile_out:
        json.dump(data, pfile_out, indent=2)
        print("Product updated successfully")

# function to update product details
def update_product():
    pprint(get_all_products())  # calling this function to be able to see the id's
    prodid = input("enter product-id: ")
    for prod in products:
        

        if prod['product_id'] == prodid:

            newprice = int(input("Enter new price: "))

            prod['price'] = newprice
            # breakpoint()

    edit_product(products)

#function to delete product
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

#function to view products and number of products in db
def products_in_db():
    pprint(get_all_products())
    print(f"Total number of products is: {(len(products))}")

#product submenu
def product_menu():
    print("***What would you like to do?***")
    print("\t1:add product")
    print("\t2:update product")
    print("\t3:Delete product")
    print("\t4:List all products")
    print("\t5:Search for product")
    print("\t6:Back to main menu")

    try:
        selection = int(input("enter your choice: "))
        if selection == 1:
            add_product()
            product_menu()
        elif selection == 2:
            update_product()
            product_menu()
        elif selection == 3:
            delete_product()
            product_menu()
        elif selection == 4:
            products_in_db()
            product_menu()
        elif selection == 5:
            search_product()
            product_menu()
        elif selection==6:
            from main import menu
            menu()
        else:
            print("\n\tInvalid selection! Please try again.\t\t")

    except:
        print("\n\tInvalid input! Please enter a valid value.\t\t")
