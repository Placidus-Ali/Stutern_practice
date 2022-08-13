import sqlite3
import csv
import os 

#create a connection
conn = sqlite3.connect("results.db")

#check 
print("Connection created")

#create a cursor object
cursor = conn.cursor()

#check
print("Cursor object created")


# #create a table called results
# create_table = """
# CREATE TABLE results(
#         Name TEXT,
#         English INTEGER,
#         Maths INTEGER,
#         Biology INTEGER,
#         Chemistry INTEGER,
#         Physics INTEGER,
#         Agric INTEGER,
#         Igbo INTEGER,
#         Geography INTEGER,
#         CRS INTEGER
            
#     )
#    """

# #check
# print("Table created")

# conn.commit()


# cursor.execute(create_table)

import csv

# #load existing table
with open('waecresult.csv', 'r') as opened_file:
    read_file = csv.reader(opened_file)

    #This command is used to skip header
    next(opened_file)

    cursor.executemany(""" INSERT INTO results VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""", read_file)

#check
print("data loaded into the table successfully")

conn.commit()
