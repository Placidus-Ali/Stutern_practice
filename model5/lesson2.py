import sqlite3
import csv

#create a connection
conn = sqlite3.connect("weac_result.db")

#check 
print("Connection created")

#create a cursor object
cursor = conn.cursor()

#create a table called waec_result
# create_table = """
# CREATE TABLE waec_result(
#         name text,
#         english integer,
#         maths integer,
#         biology integer,
#         chemistry integer,
#         physics integer,
#         agric integer,
#         igbo integer,
#         geography integer,
#         crs integer
            
#     )
#    """

#check
print("Table created")

cursor.execute(create_table)

#load existing table
with open('waec_result.csv', 'r') as open_file:
    read_file = csv.reader(open_file)

    cursor.executemany(
        """
        INSERT INTO waec_result VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, 
        read_file
    )

#check
print("data loaded into the table successfully")
