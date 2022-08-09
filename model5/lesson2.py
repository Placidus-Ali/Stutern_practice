import sqlite3
import csv

#create a connection
conn = sqlite3.connect("waec_result.db")

#check 
print("Connection created")

#create a cursor object
cursor = conn.cursor()

#create a table called waec_result
# create_table = """
# CREATE TABLE waec_result(
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

#check
print("Table created")

conn.commit()


cursor.execute(create_table)

#load existing table
with open('waec_result.csv', 'r') as opened_file:
    read_file = csv.reader(opened_file)

    #This command is used to skip header
    next(opened_file)

    cursor.executemany(""" INSERT INTO waec_result VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""", read_file)

#check
print("data loaded into the table successfully")

conn.commit()
