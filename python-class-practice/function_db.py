import pymysql
import json
def db_conn():
    mydb=pymysql.connect(
        host="localhost",
        user="root",
        password="root",
        
    )
    print("connection done")
    return mydb


def create_db(database_name):
    connection=db_conn()
    cursor=connection.cursor()
    cursor.execute(f"CREATE DATABASE {database_name}")
    print("database created")
    

database_name=input("enter database name : ")
create_db(database_name)

def table_create():
    connection=db_conn()
    cursor=connection.cursor()

    cursor.execute(f"USE {database_name}")
    cursor.execute(("""
"""))