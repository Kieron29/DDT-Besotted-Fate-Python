import sqlite3
import os
os.system('Clear')
connection = sqlite3.connect("Customer db")
cursor = connection.cursor()

command1 = '''CREATE TABLE IF NOT EXISTS users (
                      id INTEGER PRIMARY KEY AUTOINCREMENT,
                      username TEXT NOT NULL UNIQUE,
                      password TEXT NOT NULL)'''
    connection.commit()
    connection.close()
