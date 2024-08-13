import sqlite3
import os
os.system('Clear')
connection = sqlite3.connect("Customer db")
cursor = connection.cursor()

command1 = """CREATE TABLE IF NOT EXISTS
    customer (first_name text, last_name text, email text)"""

cursor.execute(command1)

cursor.execute()