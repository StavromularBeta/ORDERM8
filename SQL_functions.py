import sqlite3
import datetime

def return_unique_ID():
    conn = sqlite3.connect("ORDERM8.db")
    c = conn.cursor()
    c.execute('SELECT * FROM rolodex')
    IDs = []
    for item in c:
        ID = int(item[0])
        IDs.append(ID)
    IDs = sorted(IDs, key=int, reverse=True)
    uniqueID = IDs[0] + 1
    return str(uniqueID)

def return_unique_order_ID():
    conn = sqlite3.connect("ORDERM8.db")
    c = conn.cursor()
    c.execute('SELECT * FROM orders')
    IDs = []
    for item in c:
        ID = int(item[0])
        IDs.append(ID)
    IDs = sorted(IDs, key=int, reverse=True)
    uniqueID = IDs[0] + 1
    return str(uniqueID)


def input_entry(customerFirstName, customerLastName, customerPhoneNumber, customerAddress, customerPayMethod):
    conn = sqlite3.connect("ORDERM8.db")
    c = conn.cursor()
    uniqueID = return_unique_ID()
    rolodexEntry = (uniqueID, customerFirstName, customerLastName, customerPhoneNumber, customerAddress, customerPayMethod)
    c.execute('INSERT INTO rolodex VALUES (?,?,?,?,?,?)', rolodexEntry)
    conn.commit()


def return_all_entries():
    conn = sqlite3.connect("ORDERM8.db")
    c = conn.cursor()
    c.execute('SELECT * FROM rolodex')
    return c


def review_all_entries():
    conn = sqlite3.connect("ORDERM8.db")
    c = conn.cursor()
    c.execute('SELECT * FROM rolodex')
    for item in c:
        print item[0], item[1], item[2], item[3], item[4]


def delete_entry_by_id(uniqueID):
    conn = sqlite3.connect("ORDERM8.db")
    c = conn.cursor()
    c.execute('DELETE FROM rolodex WHERE id = ?', uniqueID)
    conn.commit()


def update_rolodex_entry(variable, variable_type, uniqueID):
    if variable_type == "name":
        update_rolodex_entry_name(variable, uniqueID)
    elif variable_type == "phoneNumber":
        update_rolodex_entry_phoneNumber(variable, uniqueID)
    elif variable_type == "address":
        update_rolodex_entry_address(variable, uniqueID)
    elif variable_type == "payMethod":
        update_rolodex_entry_payMethod(variable, uniqueID)
    else:
        print "failed to update anything."


def update_rolodex_entry_name(variable, uniqueID):
    combo = (variable, uniqueID)
    conn = sqlite3.connect("ORDERM8.db")
    c = conn.cursor()
    c.execute('''UPDATE rolodex
                    SET name = ?
                    WHERE id = ?''', combo)
    conn.commit()


def update_rolodex_entry_phoneNumber(variable, uniqueID):
    combo = (variable, uniqueID)
    conn = sqlite3.connect("ORDERM8.db")
    c = conn.cursor()
    c.execute('''UPDATE rolodex
                    SET phoneNumber = ?
                    WHERE id = ?''', combo)
    conn.commit()


def update_rolodex_entry_address(variable, uniqueID):
    combo = (variable, uniqueID)
    conn = sqlite3.connect("ORDERM8.db")
    c = conn.cursor()
    c.execute('''UPDATE rolodex
                    SET address = ?
                    WHERE id = ?''', combo)
    conn.commit()


def update_rolodex_entry_payMethod(variable, uniqueID):
    combo = (variable, uniqueID)
    conn = sqlite3.connect("ORDERM8.db")
    c = conn.cursor()
    c.execute('''UPDATE rolodex
                    SET payMethod = ?
                    WHERE id = ?''', combo)
    conn.commit()


def create_rolodex_table():
    conn = sqlite3.connect("ORDERM8.db")
    c = conn.cursor()
    create_table = """CREATE TABLE IF NOT EXISTS rolodex (
                      id integer PRIMARY KEY,
                      first_name text,
                      last_name text,
                      phone_number int,
                      address text,
                      payMethod text)
                      """
    c.execute(create_table)
    conn.commit()


def search_by_customer_first_name(customer_name):
    conn = sqlite3.connect("ORDERM8.db")
    c = conn.cursor()
    customer_name = (customer_name,)
    c.execute('''SELECT * FROM rolodex WHERE first_name = (?)''', customer_name)
    return c

def search_by_customer_last_name(customer_name):
    conn = sqlite3.connect("ORDERM8.db")
    c = conn.cursor()
    customer_name = (customer_name,)
    c.execute('''SELECT * FROM rolodex WHERE last_name = (?)''', customer_name)
    return c

def search_by_customer_phone_number(customer_phone_number):
    conn = sqlite3.connect("ORDERM8.db")
    c = conn.cursor()
    customer_phone_number = (customer_phone_number,)
    c.execute('''SELECT * FROM rolodex WHERE phone_number = (?)''', customer_phone_number)
    return c


def create_orders_table():
    conn = sqlite3.connect("ORDERM8.db")
    c = conn.cursor()
    create_table = """CREATE TABLE orders (
                      id integer PRIMARY KEY,
                      custid SMALLINT,
                      orderlist text,
                      time_stamp text)
                      """
    c.execute(create_table)
    conn.commit()


def create_customerprefs_table():
    conn = sqlite3.connect("ORDERM8.db")
    c = conn.cursor()
    create_table = """CREATE TABLE IF NOT EXISTS customerprefs (
                      id integer PRIMARY KEY,
                      customer_id integer,
                      field_id integer,
                      description text)
                      """
    c.execute(create_table)
    conn.commit()


def new_customer_delivery_preference(customerID, customer_delivery_preference):
    conn = sqlite3.connect("ORDERM8.db")
    c = conn.cursor()
    uniqueID = return_unique_customerpreference_ID()
    orderEntry = (uniqueID, customerID, 10, customer_delivery_preference)
    c.execute('INSERT INTO customerprefs VALUES (?,?,?,?)', orderEntry)
    conn.commit()

def return_unique_customerpreference_ID():
    conn = sqlite3.connect("ORDERM8.db")
    c = conn.cursor()
    c.execute('SELECT * FROM customerprefs')
    IDs = []
    for item in c:
        ID = int(item[0])
        IDs.append(ID)
    IDs = sorted(IDs, key=int, reverse=True)
    uniqueID = IDs[0] + 1
    return str(uniqueID)


def input_new_order(customerID, order_list):
    conn = sqlite3.connect("ORDERM8.db")
    c = conn.cursor()
    uniqueID = return_unique_order_ID()
    orderEntry = (uniqueID, 1, order_list, datetime.datetime.now())
    c.execute('INSERT INTO orders VALUES (?,?,?,?)', orderEntry)
    conn.commit()


#def drop_rolodex_table():
#    conn = sqlite3.connect("ORDERM8.db")
#    c = conn.cursor()
#    c.execute('DROP table rolodex')
#    for item in c:
#        orderlist = item[2].split()
#        print item[0], item[1], orderlist, item[3]

def return_all_customerprefs_entries():
    conn = sqlite3.connect("ORDERM8.db")
    c = conn.cursor()
    c.execute('SELECT * FROM customerprefs')
    return c


def get_latest_customerprefs(customer_id):
    conn = sqlite3.connect("ORDERM8.db")
    c = conn.cursor()
    customer_id_tuple = (customer_id,)
    c.execute('SELECT * FROM customerprefs WHERE customer_id=(?) AND field_id = 10 ORDER BY id DESC LIMIT 1',
              customer_id_tuple)
    for item in c:
        return item


def get_latest_foodprefs(customer_id):
    conn = sqlite3.connect("ORDERM8.db")
    c = conn.cursor()
    customer_id_tuple = (customer_id,)
    c.execute('SELECT * FROM customerprefs WHERE customer_id=(?) AND field_id = 20 ORDER BY id DESC LIMIT 1',
              customer_id_tuple)
    for item in c:
        return item

def new_customer_food_preference(customerID, customer_food_preference):
    conn = sqlite3.connect("ORDERM8.db")
    c = conn.cursor()
    uniqueID = return_unique_customerpreference_ID()
    orderEntry = (uniqueID, customerID, 20, customer_food_preference)
    c.execute('INSERT INTO customerprefs VALUES (?,?,?,?)', orderEntry)
    conn.commit()

for item in return_all_customerprefs_entries():
    print item