import sqlite3
from sqlite3 import Error

def create_connection(database):
    try:
        conn = sqlite3.connect(database)
        return conn
    except Error as e:
        print(e)

def insert_name(conn, name):
    add_name = "INSERT INTO names VALUES (?, ?)"
    cur = conn.cursor()
    cur.execute(add_name, name)
    conn.commit()   
    return cur.lastrowid

def insert_data(conn, data):
    add_data = "INSERT INTO data VALUES (?, ?)"
    cur = conn.cursor()
    cur.execute(add_data, data)
    conn.commit()
    return cur.lastrowid

def main():
    database = "contacts.db"
    conn = create_connection(database)

    if conn is not None:
        print("Database opened.\n")

        name = []
        name.append(input("Enter first name: "))
        name.append(input("Enter last name: "))
        insert_name(conn, tuple(name))

        data = []
        data.append(input("Enter phone number: "))
        data.append(input("Enter email address: "))
        insert_data(conn, tuple(data))  
        conn.close()      
    else:
        print("Connection to database failed.")

if __name__ == "__main__":
    main()