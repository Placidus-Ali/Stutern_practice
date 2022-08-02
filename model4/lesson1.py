import sqlite3

from colorama import Cursor

#connect to a database
conn = sqlite3.connect("Workers.db")

#create a cursor object
Cursor = conn.cursor()

