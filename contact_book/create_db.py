import sqlite3
from sqlite3 import Error

def create_connection(database):
    try:
        conn = sqlite3.connect(database)
        return conn
    except Error as e:
        print(e)

def create_tables(conn, create_sql_table):
    cur = conn.cursor()
    cur.execute(create_sql_table)
    cur.close()

def main():
    database = "contacts.db"

    name_table = """CREATE TABLE IF NOT EXISTS names (
	            first_name text,
                last_name text);"""

    data_table = """CREATE TABLE IF NOT EXISTS data (
                phone text,
                email text);"""
    
    conn = create_connection(database)
    if conn is not None:
        print("Connection is created.")
        create_tables(conn, name_table)
        create_tables(conn, data_table)
    else:
        print("Connection failed.")

if __name__ == "__main__":
    main()



