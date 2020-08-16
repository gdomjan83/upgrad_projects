import sqlite3
from sqlite3 import Error

def create_connection(database):
    try:
        conn = sqlite3.connect(database)
        return conn
    except Error as e:
        print(e)

def print_all_data(conn):
    cur = conn.cursor()
    cur.execute("SELECT * FROM names")
    all_name = cur.fetchall()
    cur.execute("SELECT * FROM data")
    all_data = cur.fetchall()
    
    for i, row in enumerate(all_name):
        print("=============================================================")
        print(" ".join(row) + " - Tel: " + all_data[i][0] + " - Email: " + all_data[i][1])

def main():
    database = "contacts.db"
    conn = create_connection(database)

    if conn is not None:
        print("Connection is created.")
        print_all_data(conn) 
    else:
        print("Connection failed.")

if __name__ == "__main__":
    main()