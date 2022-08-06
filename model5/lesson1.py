import sqlite3

#check
print("sqlite3 imported successfully")

#connect a database
conn = sqlite3.connect("student.db")


#check
print("Connection successful")

#create cursor object
cursor = conn.cursor()

#check
print("Cuursor created successfful")

#querying the databsae using ORDER BY
item = cursor.execute("""SELECT * FROM students_data
                    WHERE last_name like J&
                    ORDER BY first_name:
""")

for row in item:
    print(row)

