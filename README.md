# CS 3380 Database Appliation and Informational Systems Final Project

About

I have created a application which utilizes a database for a store. With this applications you can do various different functions which can retrieve data, add data, and show data, from the database.

# Prerequisites

Install termcolor with pip3 install --upgrade termcolor

Install mysql.connector with pip3 install mysql-connector-python

After cloning the repo, you will need to create a file to hold your password (DO NOT PUT THIS FILE INTO YOUR REPO). this file will retrieve your password each time you use the application and will log you into it.

ex. 

# password is stored here

password is kept inside this
key = {
    'password': 'enter-password-here'
}

# HOW TO INIT THE SERVER ON MAC
start server
System Prefrences->MySQL->Turn on Server
connect to DB using mysql -uroot -p
Enter password
Execute source ./storeDB.sql

Note: To drop the schema, execute DROP DATABASE STORE_SCHEMA; in mysql.
