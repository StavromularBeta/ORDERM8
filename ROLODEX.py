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

