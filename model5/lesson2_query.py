import sqlite3

#connect a connection
conn = sqlite3.connect("waec_result.db")

#check 
print("Connection created")

#create a cursor object
cursor = conn.cursor()

#check
print("cursor object created")

#query
query = """
SELECT * FROM waec_result
"""

cursor.execute(query)

#check
print("Query executed")

#fectch items
items = cursor.fetchall()


#format output
# print(items)

# format output to display in a tabular form
print("Name"+ "\t\t Eng"+ "\tMaths"+ "\tBio"+"\tChem"+ "\tPhy"+ "\tAgric"+ "\tIgbo"+ "\tGeo"+ "\tCRS \n" f"{'.' * 100}" )

# Loop through the items
for item in items:
    Name, English, Maths, Biology, Chemistry, Physics, Agric, Igbo, Geography, CRS = item
    print(f"{Name:12}{English:7}{Maths:8}{Biology:7}{Chemistry:9}{Physics:8}{Agric:8}{Igbo:8}{Geography:7}{CRS:9}")



#commiit changes
conn.commit()

#close connection
conn.close()