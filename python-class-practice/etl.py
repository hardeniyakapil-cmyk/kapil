import json
import pymysql
from function_db import *

with open("table.json") as file:
    schema = json.load(file)
    # print(schema)

with open("student_profile.json","r") as file:
    st_schema = json.load(file)
    # print(st_schema)

db_name = schema["database"]
mydb=db_conn()
cursor=mydb.cursor()

# 


cursor.execute(f"USE {db_name}")
# print("Database selected.")

col_def=",".join([f"{col} {dtype}" for  col,dtype in schema['columns'].items()])
cursor.execute(f" CREATE TABLE IF NOT EXISTS {schema['table_name']} ({col_def})")

print("table created succesfully")

students = st_schema["students"]

columns =students[0].keys()

col_names = ",".join(columns)
placeholders = ",".join(["%s"] * len(columns))

query = f"""
INSERT INTO {schema['table_name']} ({col_names})
VALUES ({placeholders})
"""

for student in students:
    values = tuple(student.values())
    cursor.execute(query, values)

print("Data inserted successfully.")

mydb.commit()
cursor.close()
mydb.close()