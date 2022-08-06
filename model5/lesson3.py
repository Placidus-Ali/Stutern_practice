import sqlite3

#check
print("sqlite3 imported successfully")


# create connection
conn = sqlite3.connect("music.db")

#check
print("connection created successfully")

#create a cursor object
cursor = conn.cursor()

#check
print("cursor obj created successfully")

#create a table called 
# cursor.execute(
#     """
#     CREATE TABLE track(
#         Track_id INTEGER,
#         Album_id INTEGER,
#         Track name TEXT,
#         Milliseconds INTEGER
#     )
#     """
# )

#check
print("table created successfully")

TRACKS = [
    (1, 25, 'African queeen', 25000),
    (2, 25, 'only you', 40000),
    (3, 25, 'true love', 50000),
    (1, 26, 'onyinye', 60000),
    (2, 26, 'roll it', 70000),
    (3, 26, 'get sqaured', 80000),
    (5, 27, 'happy', 90000)
]

conn.commit()


#check
print("Tracks created successfully")

cursor.executemany(
    """
    INSERT INTO track
    VALUES (?, ?, ?, ?)
    """,
    TRACKS
    )

#CHECK
print("insert successfully")

conn.commit()

print(TRACKS)
