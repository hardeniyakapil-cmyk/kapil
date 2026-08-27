import os
import pymysql
from pymysql import Error
from dotenv import load_dotenv

load_dotenv()

DB_CONFIG={
    "host":os.getenv("DB_HOST"),
    "port":int(os.getenv("DB_PORT",3306)),
    "database":os.getenv("DB_NAME"),
    "user":os.getenv("DB_USER"),
    "password":os.getenv("DB_PASSWORD"),
    "cursorclass":pymysql.cursors.DictCursor,
}

def get_connection():
    try:
        connection=pymysql.connect(**DB_CONFIG)
        return connection
    except Error as e:
        print(f"Connection Error : {e}")
        return None
    
def check_health():
    connection=get_connection()
    if connection is None:
        return {"status":"Unhealthy","detail":"Connection Failed ❌"}
    
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT 1")
            cursor.fetchone()
            return {"status":"healthy","detail":"DB Connection OK ✅"}
    except Error as e:
        return {"status":"Unhealthy","detail":str(e)}
    
    finally:
        connection.close()