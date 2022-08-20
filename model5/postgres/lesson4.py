import pandas as pd
import sqlalchemy
from sqlalchemy import create_engine

#creat a connection
engine = create_engine("postgresql+psycopg2://postgres:postgres@localhost:5432/demo_db", pool_recycle= -1)
db_engine = engine.connect()

print("enine created successfully")

#let's query the table in the database
# define a function
def query_db(query, db_conn):
    df = pd.read_sql(query, db_conn)
    print(df)
    return df

query_db("SELECT * FROM courses LIMIT 10", db_engine)

#close connection
db_engine.close()