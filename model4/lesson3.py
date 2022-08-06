import sqlite3
from tkinter import INSERT

#check
print("Successful")

#connect to a database
conn = sqlite3.connect("student.db")

#check
print("connection successful")

#create a cursor object
cursor = conn.cursor()

#check
print("cursor object created successfully")

#create a table called students_data
# cursor.execute(
#     """
#     CREATE TABLE students_data(
#         first_name text,
#         last_name text,
#         email text
#     )
#     """
# )

#check
# print("Table created successfully")

#commit to database 
conn.commit()

#check
# print("successfully")

# #insert values into your table
students_list = [
                    ('Will', 'Johnson', 'willjohnson@stutern.com'),
                    ('John', 'Smith', 'Johnsmith@stutern.com'),
                    ('Katy', 'Brown', 'Katybrown@stutern.com'),
                ]
#check
print("list created successfully")

#cursor.executemany ("INSERT INTO students_data VALUES(?, ?, ?)", students_list)

# conn.commit()

#check
# print("List inserted successfully")

#query the database
# cursor.execute("SELECT * FROM students_data")

# items = cursor.fetchall()
# print("First Name"+ "\t Last Name"+ "\t\t E-mail \n" f"{'.' * 100}" )

# # Loop through the items
# for item in items:
#     first_name, last_name, email, course = item
#     print(f"{first_name:16}{last_name:20}{email:35}")

conn.commit()

# Alter table
#change the tabel name

# cursor.execute("ALTER TABLE student_data RENAME student_info")

#Alter column name
# cursor.execute("ALTER TABLE students_data ADD COLUMN Course")

# #check
print("Column added successfully")

#update statement
cursor.execute(
    """
    UPDATE students_data SET Course = 'data science'
    """
)
#check
print("update done successfully")

conn.commit()

#query the database
cursor.execute("SELECT * FROM students_data")

items = cursor.fetchall()
print("First Name"+ "\t Last Name"+ "\t\t E-mail"+ "\t\t\t\t Course \n" f"{'.' * 100}" )

# Loop through the items
for item in items:
    first_name, last_name, email, course = item
    print(f"{first_name:16}{last_name:20}{email:35}{course:20}")



