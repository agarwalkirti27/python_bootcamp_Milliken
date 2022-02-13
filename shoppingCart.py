#import necessary functions
from xml.etree.ElementInclude import DEFAULT_MAX_INCLUSION_DEPTH
from IPython.display import clear_output
import csv

#global list variable
cart = []

#create a function to add items

def saveCart(cart):
    with open("cart.csv", mode='w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(cart)

def add(item):
    clear_output()
    cart.append(item)
    print("item {} has been added".format(item))
    
#create function remove item from the cart
def remove(item):
    clear_output()
    try:
        if item.isdigit():
            item_removed = cart.pop(int(item)-1)
            print("item {} has been removed".format(item_removed))
        else:
            cart.remove(item)
            print('{} has been removed.'.format(item))
    except:
        print("Sorry, we can't remove the item".format(item_removed))
  
   
#create function to show item in the cart
def show():
    clear_output()
    if cart:
        print("Here is your cart: ")
        
        for i in range(0, len(cart)):
            print("{}) {}".format(i+1, cart[i]))
    else:
        print("Your cart is empty.")
        
    
    
#create function to clear the cart
def clearCart():
    clear_output()
    cart.clear()
    print("Your cart is empty.")
    

    
#create main function for loop until user quits
def main():
    done = False
    while not done:
        ans = input("quit/add/remove/show/clear/save : ").lower()
        
        #base case
        if ans == "quit":
            print("Thanks for using our program.")
            show()
            done = True
        elif ans == "add":
            item = input("What would you like to add? ").title()
            add(item)
        elif ans == "remove":
            show()
            item = input("What would you like to remove? ").title()
            remove(item)
        elif ans == "show":
            show()
        elif ans == "clear":
            clearCart()
        elif ans == "save":
            saveCart(cart)
        else: 
            print("Sorry, that wasn't an option")
           
            
#main() #run the program 
