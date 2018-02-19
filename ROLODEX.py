import sqlite3

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


def input_entry(customerName, customerPhoneNumber, customerAddress, customerPayMethod):
    conn = sqlite3.connect("ORDERM8.db")
    c = conn.cursor()
    uniqueID = return_unique_ID()
    rolodexEntry = (uniqueID, customerName, customerPhoneNumber, customerAddress, customerPayMethod)
    c.execute('INSERT INTO rolodex VALUES (?,?,?,?,?)', rolodexEntry)
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
                      name text,
                      phoneNumber text,
                      address text,
                      payMethod text)
                      """
    c.execute(create_table)
    conn.commit()

return_unique_ID()


