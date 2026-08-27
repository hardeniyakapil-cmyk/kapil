from config.db_config import get_connection

def delete_student(stu_id):
    connnection=get_connection()
    cursor=connnection.cursor()
    try:
        query="DELETE FROM all_students WHERE id=%s"
        cursor.execute(query,(stu_id))
        connnection.commit()
        return cursor.rowcount>0
    except Exception as e:
        connnection.rollback()
    finally:
        cursor.close()
        connnection.close()