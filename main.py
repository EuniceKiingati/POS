from customers import *
from products import *
from purchases import purchase_menu

def menu():
    print("*******Welcome to this store******")
    print("*****Please select option to continue****")
    print("1:Customer operations")
    print("2:Product operations")
    print("3:Purchases stuff")

    selection=int(input("Enter your selection: "))
    if selection==1:
        customer_menu()
    elif selection==2:
        product_menu()
    elif selection==3:
        purchase_menu()
    else:
        print("Invalid selection")
   
if __name__ =="__main__":
    menu()
    
