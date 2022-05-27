

import pdb
import json
from uuid import uuid4

try:
    product_data = open('products.json')
    products = json.load(product_data)
except Exception as e:
    print(e)
    products=[] 
    

class Product():

     def __init__(self, product_id=None, name=None, size=None, price=None):
        self.product_id=product_id
        self.name=name
        self.size=size
        self.price=price

     def __str__(self):
        return ( f'{self.product_id} {self.name} {self.size} {self.price}')
    

def get_all_products():
    #breakpoint()
    print(products)

def save_product(data):
        new_product = {}
        new_product['product_id'] = str(uuid4())
        new_product["name"] = data['name']
        new_product["size"] = data['size']
        new_product["price"] =data['price']
        product=Product(new_product['product_id'], new_product['name'],new_product['size'],new_product['price'])

        get_all_products()
        products.append(new_product)

        with open('products.json', 'w') as pfile_out:
            json.dump(products, pfile_out, indent=0)
    
        
        


        

        

        #print("so far so good")
        

def add_product():

    

    continue_add = True
    while continue_add:

        name =input("Enter name: ")
        size=str(input("enter size: "))
        price=int(input("enter price: "))
        data = {
            "name": name,
            "size":size,
            "price":price
            
        }
        save_product(data)
        print(products)
        choice=int(input("enter 1 to add another product or 2 to exit: "))
        if choice==2:
            continue_add=False
            print("Product (s) added")



           
        




def update_product():
    get_all_products()#calling this function to be able to see the id's
    prodid=input("enter product-id: ")
    for prod in products:
        #breakpoint()

        if prod['product_id']== prodid:

            
            
            newprice=int(input("Enter new price: "))
             
            prod['price']=newprice
            #breakpoint()

    with open('products.json', 'w') as pfile_out:
            json.dump(products, pfile_out, indent=0)
            print("Product updated successfully")


def delete_product():
    get_all_products()
    prodid=input("enter customer id: ")


    for i in range(len(products)):
        if products[i]['product_id']==prodid:
            products.remove(products[i])
            break
    #breakpoint()
    with open('products.json', 'w') as pfile_out:
            json.dump(products, pfile_out, indent=0)
            print("Product deleted successfully")

           
        




def product_menu():
    print("what would you like to do?")
    print("1:add product")
    print("2:update product")
    print("3:Delete product")

    selection=int(input("enter your choice: "))
    if selection==1:
        add_product()
    elif selection==2:
        update_product()
    elif selection==3:
        delete_product()


        
       
        
            #print(cust)


    








        

# import pdb;
# pdb.set_trace()
        

#with open('customers.json', 'w') as file_out:
    #json.dump(customers, file_out, indent=0)
     

        


    #print("working on it")