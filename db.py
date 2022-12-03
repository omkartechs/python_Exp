import sqlite3

def createtable():
    conn = sqlite3.connect('lite.db')
    cur = conn.cursor()
    cur.execute("CREATE TABLE data2(rollno INTEGER , name TEXT , mark REAL)")
    conn.commit()
    conn.close()

createtable()    