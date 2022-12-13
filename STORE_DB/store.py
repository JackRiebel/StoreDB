# Import all necessary packages
from functions import *
import mysql.connector

# Import password
import password
pwd = password.key['password']

# Connect to the DB
cnx = mysql.connector.connect(
    user='root', password=pwd, host='localhost', database='STORE')

# Create the cursor
cursor = cnx.cursor()

# Ask the user for the store ID
storeID = input("Enter the store ID for the store you would like to query. ")

quit = False

# Loop through menu until user selects to quit
while not quit:
    # Print list of available functions
    print()
    print()
    print(colored("Store Managment Application", "grey", "on_yellow"))
    print()
    print("1. Change stores")
    print("2. Get store address")
    print("3. Check to see if item is available")
    print("4. Check item price")
    print("5. Sell item")
    print("6. View purchased items")
    print("7. Get customer's information")
    print("8. Quit")
    print()

    # Asks the user for input
    option = input("Enter your choice: ")
    print()

    # Goes to function based on user input
    if option == "1":
        storeID = change_store()
    elif option == "2":
        get_store_address(cursor, storeID)
    elif option == "3":
        check_availability(cursor, storeID)
    elif option == "4":
        check_item_price(cursor)
    elif option == "5":
        sell_item(cursor, storeID)
    elif option == "6":
        view_purchased_item(cursor)
    elif option == "7":
        get_customer_info(cursor)
    elif option == "8":
        quit = True

# Close the connection
print("Now leaving the Store Management Application...")
print()
cursor.close()
cnx.close()