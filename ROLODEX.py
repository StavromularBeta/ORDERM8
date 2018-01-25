import sqlite3


def input_entry(customerName, customerPhoneNumber, customerAddress, customerPayMethod):
    conn = sqlite3.connect("ORDERM8.db")
    c = conn.cursor()
    uniqueID = 3
    rolodexEntry = (uniqueID, customerName, customerPhoneNumber, customerAddress, customerPayMethod)
    c.execute('INSERT INTO rolodex VALUES (?,?,?,?,?)', rolodexEntry)
    conn.commit()


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

review_all_entries()


