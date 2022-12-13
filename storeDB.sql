/*
	Name: Jack Riebel
    Pawprint: jartyc
    Date: 12/6/22
    
*/
CREATE SCHEMA STORE;
USE STORE;

CREATE TABLE EMPLOYEE (
SSN INT NOT NULL,
	fname VARCHAR(50),
    minit CHAR(1),
    lname VARCHAR(50),
    birthday DATE,
    designation VARCHAR(50),
    PRIMARY KEY(SSN)
);

CREATE TABLE STORES (
manager_SSN INT NOT NULL,
store_ID INT NOT NULL,
	street VARCHAR(50),
    city VARCHAR(50),
    curr_state VARCHAR(50),
    ZIP CHAR(5),
    phone_num CHAR(10),
    PRIMARY KEY(store_ID),
    FOREIGN KEY(manager_SSN) REFERENCES EMPLOYEE(SSN)
);

CREATE TABLE PRODUCT (
product_ID INT NOT NULL,
store_ID INT NOT NULL,
	price INT,
    amount INT,
    PRIMARY KEY(product_ID),
    FOREIGN KEY(store_ID) REFERENCES STORES(store_ID)
);

CREATE TABLE CUSTOMER (
customer_ID INT NOT NULL,
	customer_name VARCHAR(50),
    street VARCHAR(50),
    ZIP CHAR(5),
    city VARCHAR(50),
    curr_state VARCHAR(50),
    PRIMARY KEY(customer_ID)
);

CREATE TABLE SUPPLIER (
supplier_ID INT NOT NULL,
	name VARCHAR(50),
    PRIMARY KEY(supplier_ID)
);

CREATE TABLE WORK_IN (
store_ID INT NOT NULL,
MSSN INT NOT NULL,
	FOREIGN KEY(store_ID) REFERENCES STORES(store_ID),
    FOREIGN KEY(MSSN) REFERENCES STORES(manager_SSN)
);

CREATE TABLE CONTAIN (
store_ID INT NOT NULL,
product_ID INT NOT NULL,
	FOREIGN KEY(store_ID) REFERENCES STORES(store_ID),
    FOREIGN KEY(product_ID) REFERENCES PRODUCT(product_ID)
);

CREATE TABLE PURCHASES (
customer_ID INT NOT NULL,
product_ID INT NOT NULL,
order_no INT NOT NULL,
    shipping_street VARCHAR(50),
    shipping_ZIP VARCHAR(50),
    shipping_city VARCHAR(50),
    shipping_state VARCHAR(50),
    shipping_date DATE,
    PRIMARY KEY(order_no),
	FOREIGN KEY(customer_ID) REFERENCES CUSTOMER(customer_ID),
    FOREIGN KEY(product_ID) REFERENCES PRODUCT(product_ID)
);

CREATE TABLE SUPPLIES (
supplier_ID INT NOT NULL,
product_ID INT NOT NULL,
	FOREIGN KEY(supplier_ID) REFERENCES SUPPLIER(supplier_ID),
    FOREIGN KEY(product_ID) REFERENCES PRODUCT(product_ID)
);

INSERT INTO EMPLOYEE VALUES 
	(412056743, "Jonathan", "A", "Riebel", 20020515, 000001);

INSERT INTO EMPLOYEE VALUES 
	(57345965, "Jane", "C", "Riley", 20010725, 000002);
    
INSERT INTO STORES VALUES
	(412056743, 000001, "6533 S OakPath Ct.", "Peoria", "Illinois", "61615", "3095446785");
    
INSERT INTO STORES VALUES
	(57345965, 000002, "7844 W WillowPath St.", "Pekin", "Missouri", "65201", "3146805670");

INSERT INTO PRODUCT VALUES
	(1, 000001, 50, 75);
    
INSERT INTO PRODUCT VALUES
	(2, 000002, 75, 0);

INSERT INTO CUSTOMER VALUES
    (268424, "John Brudder", "5673 N Trident Ln.", "54785", "Mexico", "Missouri");

INSERT INTO CUSTOMER VALUES
    (783256, "Carly Vernhask", "7894 E Wilddrive Ave.", "66522", "Los Angeles", "California");

