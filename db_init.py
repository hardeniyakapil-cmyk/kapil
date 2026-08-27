import os
import pymysql
import json
from dotenv import load_dotenv

load_dotenv()

with open(f"database/schema.json","r") as f:
        data=json.load(f)

def db_connect():
    conn=pymysql.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        port=int(os.getenv("DB_PORT"))
    )
    return conn

def db_creation():
    conn=db_connect()
    cur=conn.cursor()
    try:
        cur.execute(F"CREATE DATABASE {data['database']}")
        print(f"Database {data['database']} Created ✅")
        conn.commit()
    except Exception as e:
        print("Exist :",e)

db_creation()

table=data['table']
cols=" ,".join([f"{col} {dcol}" for col,dcol in data['columns'].items()])
print(cols)

def create_table():
    conn=db_connect()
    cur=conn.cursor()
    cur.execute(f"USE {data['database']}")
    cur.execute(f"CREATE TABLE IF NOT EXISTS {table} ({cols});")
    print(f"TABLE CREATED {table}")


create_table()
