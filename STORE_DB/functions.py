# This file contains all functions used in "store.py" to navigate and change the DB

from termcolor import colored
import time    


def print_query(query, cursor):
    # Execute a SQL query
    cursor.execute(query)

    # Iterate over the results
    for result in cursor:
        print(result)

    input("Press Enter to continue...")

def change_store():
    storeID = input("Select new store to browse: ")
    return storeID

def get_store_address(cursor, storeID):

    query = "SELECT street, city, ZIP, curr_state FROM STORES WHERE store_ID = " + \
        str(storeID)
    cursor.execute(query)

    for result in cursor:
        address = str(result[0] + " " + result[1] + " " + result[2] + " " + result[3])

    print()
    print("The address of the store you are looking for is " + colored(address, 'green'))
    print()
    input("Press Enter to continue...")
    
def check_availability(cursor, storeID):
    store_ID = storeID
    product_ID = input("What is the product_ID of the item you are looking for? ")
    availability = 0

    query = "SELECT amount FROM PRODUCT WHERE product_ID = "+ str(product_ID) +" AND store_id = "+ str(storeID) +""
    cursor.execute(query)

    for result in cursor:
        availability = result[0]

    print()
    if (availability == 0):
        print(colored("This item is currently out of stock.", 'red'))
    else:
        print(colored("This item is currently in stock.", 'green'))

    print()
    input("Press Enter to continue...")

def check_availability_at_checkout(cursor, storeID, productID):
    availability = 0

    query = "SELECT amount FROM PRODUCT WHERE product_ID = "+ str(productID) +" AND store_id = "+ str(storeID) +""
    cursor.execute(query)

    for result in cursor:
        availability = result[0]

    print()
    if (availability == 0):
        print(colored("This item is currently out of stock.", 'red'))
        return 0
        print()
        input("Press Enter to continue...")


def check_item_price(cursor):
    product_ID = input("Please enter the product ID: ")

    query = "SELECT price FROM PRODUCT WHERE product_ID = "+ str(product_ID) + ""
    cursor.execute(query)
    
    for result in cursor:
        price = str(result[0])

    print()
    print("The price of the product is " + colored("$" +price, "green"))
    print()
    input("Press Enter to continue...")

def sell_item(cursor, storeID):
    customerID = input("Enter the customer ID: ")
    productID = input("Enter the product ID: ")
    availability = check_availability_at_checkout(cursor, storeID, productID)
    if(availability == 0):
        return
    print("Enter your Address information:")
    shippingAddress = input("Address: ")
    shippingZIP = input("ZIP: ")
    shippingCity = input("City: ")
    shippingState = input("State: ")
    orderNO = input("Enter Order No: ")
    shippingDate = time.strftime('%Y-%m-%d')

    query = "INSERT INTO PURCHASES VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
    cursor.execute(query, (customerID, productID, orderNO, shippingAddress,
                   shippingZIP, shippingCity, shippingState, shippingDate))

    print()
    print(colored("SHIPPING ORDER CREATED:\nShip to:"+ shippingAddress + " " + shippingZIP + " " + shippingCity + " " + shippingState +"\nCustomer: "+ customerID + "\nProduct ID: "+ productID +"\nOrder Number: "+ orderNO +"\nShipped on: " + shippingDate, "green"))
    print()
    input("Press Enter to continue...")

def view_purchased_item(cursor):
    order_ID = input("Please enter your order ID to view: ")
    
    query = "SELECT customer_ID, product_ID, order_no, shipping_street, shipping_ZIP, shipping_city, shipping_state, shipping_date FROM PURCHASES WHERE order_ID = " + \
        str(order_ID)
    cursor.execute(query)
  
    for result in cursor:
        order_info = str("Customer ID: "+ result[0] +"\nProduct ID: "+ result[1]+ "\nOrder No: " + result[2] + "\nShipping Address: " + result[3] + " " + result[4] + " " + str(result[5] +" " + result[6] + " " + result[7] + "\nDate Shipped:" + str(result[8], "green")))
        print("The customers information is:\n " + colored( order_info, 'green'))
        print()
        input("Press Enter to return home")

def get_customer_info(cursor):
    customer_ID = input("Enter the customer_ID for the customers information: ")
    query = "SELECT customer_name, street, ZIP, city, curr_state, customer_ID FROM CUSTOMER WHERE customer_ID = " + \
        str(customer_ID)
    cursor.execute(query)
  
    for result in cursor:
        customer_info = str(result[0] + " " + result[1] + " " + result[2] + " " + result[3] + " " + result[4] + " " + str(result[5]))
        print("The customers information is:\n " + colored( customer_info, 'green'))
        print()
        input("Press Enter to return home")