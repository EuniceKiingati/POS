

import pdb
import json
from uuid import uuid4

try:
    customer_data = open('customers.json')
    customers = json.load(customer_data)
except Exception as e:
        print(e)
        customers=[] 
        print(customers)

class Customer():
    def __init__(self, user_id=None, name=None, phonenumber=None, address=None):
        self.user_id=user_id
        self.name=name
        self.phonenumber=phonenumber
        self.address=address
    
    def __str__(self):
        return ( f'{self.user_id} {self.name} {self.phonenumber} {self.address}')

def get_all_customers():
        print(customers)

def save_customer(data):

        new_customer = {}
        new_customer['user_id'] = str(uuid4())
        new_customer["name"] = data['name']
        new_customer["phonenumber"] = data['phonenumber']
        new_customer["address"] = data['address']
        
        
        customer = Customer(new_customer['user_id'], new_customer['name'], new_customer['phonenumber'], new_customer['address'])
        get_all_customers()


        customers.append(new_customer)

        with open('customers.json', 'w') as file_out:
            json.dump(customers, file_out, indent=0)

        
def add_customer():

    continue_add = True
    while continue_add:

        name =input("Enter name: ")
        phonenumber=int(input("enter phonenumber: "))
        address=str(input("enter address: "))
        data = {
            "name": name,
            "phonenumber":phonenumber,
            "address":address
            
        }
        save_customer(data)
        choice=int(input("enter 1 to add another customer or 2 to exit: "))
        if choice==2:
            continue_add=False
            print("Customer (s) added")


def update_customer():
    customer = Customer()
    customers = customer.get_all_customers()
    #calling the above function to be able to see the ids
    yourid=input("enter id: ")
    for cust in customers:
        #breakpoint()

        if cust['user_id']== yourid:

            
            
            newnumber=int(input("Enter new number: "))
             
            newaddress=str(input("Enter new address: "))
            cust['phonenumber']=newnumber
            cust['address']=newaddress
            #breakpoint()

    with open('customers.json', 'w') as file_out:
            json.dump(customers, file_out, indent=0)
            print("Customer updated successfully")


def delete_customer():
    customer = Customer()
    customers = customer.get_all_customers()
    #get_all_customers()
    yourid=input("enter customer id: ")


    for i in range(len(customers)):
        if customers[i]['user_id']==yourid:
            customers.remove(customers[i])
            break
    #breakpoint()
    with open('customers.json', 'w') as file_out:
            json.dump(customers, file_out, indent=0)
            print("Customer deleted successfully")

           
        




def customer_menu():
    print("what would you like to do?")
    print("1:add customer")
    print("2:update customer")
    print("3:Delete customer")

    selection=int(input("enter your choice: "))
    if selection==1:
        add_customer()
    elif selection==2:
        update_customer()
    elif selection==3:
        delete_customer()


        
       
        
            #print(cust)


    








        

# import pdb;
# pdb.set_trace()
        

#with open('customers.json', 'w') as file_out:
    #json.dump(customers, file_out, indent=0)
     

        


