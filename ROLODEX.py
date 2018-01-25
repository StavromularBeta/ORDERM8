import sqlite3
conn = sqlite3.connect("ORDERM8.db")
c = conn.cursor()

c.execute("SELECT * FROM rolodex")
for item in c.fetchone():
    print item

