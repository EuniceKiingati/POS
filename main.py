from customers import *
from products import *
from purchases import *

def menu():
    print("*******Welcome to this store******")
    print("*****Please select option to continue****")
    print("1:Customer operations")
    print("1:Product operations")
    print("1:Purchases stuff")

    selection=int(input("Enter your selection: "))
    if selection==1:
        customer_menu()
    elif selection==2:
        product_stuff()
    elif selection==3:
        purchases_stuff()
    else:
        print("Invalid selection")
   
if __name__ =="__main__":
    menu()
    
