import streamlit as st
from config.db_config import check_health
from services.registration_service import insert_student
from services.get_all_student import get_all_students

st.set_page_config(page_title="Student Management System",layout="wide")
st.title("📚 Student Management System")

health=check_health()

if health["status"]=="healthy":
    st.success(f"✅ {health['detail']}")
else:
    st.error(f"❌ {health['detail']}")
    st.stop()

st.write("Welcome ! 🌐")

col1,col2=st.columns(2)

# LEFT COLUMNS

with col1:
    st.subheader("📝Register Student")

    with st.form("stu_reg_form",clear_on_submit=True):
        stu_name=st.text_input("Student Name")

        stu_age=st.number_input("Student Age",min_value=1,max_value=100,value=None)

        stu_reg_no=st.text_input("Registaion No")

        # stu_email=st.text_input("Email ID")

        submmited=st.form_submit_button("Register Now",use_container_width=True)
        if submmited:
            try:
                success= insert_student(stu_name.strip(),int(stu_age),stu_reg_no.strip())
                if success:
                    st.success(f"✅ {stu_name} Registered suceessfully")
                # success, message = insert_student(stu_name.strip(),int(stu_age),stu_reg_no.strip(),stu_email.strip())
                # if success:
                #     st.success(message)
                # else:
                #     st.error(message)
            except Exception as e:
                st.error(f"Error: {e}")

# RIGHT COLUMN
with col2:
    st.subheader("📂 Registered Student")

    try:
        students=get_all_students()

        if students:
            st.dataframe(students,width="stretch",hide_index=True)
        else:
            st.info("No Student Registered yet")
    except Exception as e:
        st.error(f"Could not load student {e}")