import sqlite3
from tabnanny import check

#check
print("Sqlite3 imported successfully")

# create connection
conn = sqlite3.connect("Workers.db")
 
#check
print("connection created successfully") ;print(type(conn))

#create a cursor object
cursor = conn.cursor()

#check
print("cursor object creating successfully")

#create a table
# cursor.execute(
#     """
#     CREATE TABLE workers_salary(
#         first_name text,
#         last_name text,
#         email text,
#         department text
#     )
#     """
# )

#check
print("Table created successfully")

# Insert statement
cursor.execute(
    """
    INSERT INTO workers_salary 
    VALUES('Abubakar', 'Adisa', 'adisaabubakar@gmail.com', 'Data Science'), ('Adebisi', 'Afolabi', 'wasola.afolabi@yahoo.com', 'Data Science')
    """
    )

#check
print("Table inserted successfully")

cursor.execute(
    """
    INSERT INTO workers_salary 
    VALUES('Babajide', 'Adesugba', 'jide_ade@hotmail.com', 'Data Science'), ('Bukola', 'Ajayi', 'bukolam.ajayi@gmail.com', 'Data Science')
    """
    )

#check
print("Table inserted successfully")

#add multiple info
workers_list = [
                     ('Eke', 'Ihuoma', 'ihuomaeke28@gmail.com', 'Data Science'), ('Esther', 'Akpanowo', 'estherakpanowo@gmail.com', 'Data Science'), 
                     ('Eniola', 'Osadare', 'dorcasosadare@gmail.com', 'Data Science'), ('Etariemi', 'Louis', 'etariemilouis@gmail.com', 'Data Science'),
                     ('Faith', 'Amure', 'amuretalodabif@gmail.com', 'Data Science'), ('Ganiyat', 'Shittu', 'ganiyatas@gmail.com', 'Data Science'), 
                     ('Gideon', 'Uko', 'ukogideon13@gmail.com', 'Data Science'), ('Idowu', 'Adesanya', 'idsworld22@yahoo.com', 'Data Science'), 
                     ('Joyce', 'Ezeonwu', 'joyceokore@gmail.com', 'Data Science'), ('Kehinde', 'Orolade', 'kehindeorolade@gmail.com', 'Data Science'),
                     ('Kafayat', 'Ibrahim', 'kafayatadenike10@gmail.com', 'Data Science'), ('Lawrence', 'Aneshimokha', 'anelawrence1@gmail.com', 'Data Science'),
                     ('Mariam', 'Adeoti', 'adetutuadebola28@gmail.com', 'Data Science'), ('Ogechi', 'Njemanze', 'ogenjemz@gmail.com', 'Data Science')
]

cursor.executemany(
    """
    INSERT INTO workers_salary
    VALUES (?, ?, ?, ?)
    """,
    workers_list
    )

#check
print("inserted multiple info")

#query data
cursor.execute(
    """
    SELECT * FROM workers_salary
    """
    )

items = cursor.fetchall()

# format output to display in a tabular form
print("first_name"+ "\t last_name"+ "\t\t email:"+ "\t\t\t department \n" f"{'.' * 100}" )

# Loop through the items
for item in items:
    first_name, last_name, email, department = item
    print(f"{first_name:16}{last_name:16}{email:30}{department}")


#check
print("Query executed successfully")

