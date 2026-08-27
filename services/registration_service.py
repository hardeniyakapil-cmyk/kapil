from config.db_config import get_connection

def insert_student(stu_name,stu_age,stu_reg_no):
    connnection=get_connection()
    if connnection is None:
        return False ,"Could Not connect to Database"
    
    try:
        with connnection.cursor() as cursor:
            cursor.execute("INSERT INTO all_students (stu_name,stu_age,stu_reg_no) VALUES (%s,%s,%s)",(stu_name,stu_age,stu_reg_no))
            connnection.commit()
        return True , "Student Regiseter"

    except Exception as e:
        connnection.rollback()
        return False , str(e)
    finally:
        connnection.close()