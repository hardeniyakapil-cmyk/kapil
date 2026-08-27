from config.db_config import get_connection

def get_all_students():
    connnection=get_connection()
    if connnection is None:
        return False ,"Could Not connect to Database"
    try:
        with connnection.cursor() as cursor:
            cursor.execute("SELECT * FROM all_students")
            return cursor.fetchall()

    except Exception as e:
        return False , str(e)
    finally:
        connnection.close()