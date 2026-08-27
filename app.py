import streamlit as st
from config.db_config import check_health
from services.registration_service import insert_student
from services.all_stu_service import get_all_students
from services.delete_stu_service import delete_student

st.set_page_config(page_title="Student Management System",layout="wide")
st.title("📚 Student Management System")

health=check_health()

if health["status"]=="healthy":
    st.success(f"✅ {health['detail']}")
else:
    st.error(f"❌ {health['detail']}")
    st.stop()

st.write("Welcome ! 🌐")

if "edit_student" not in st.session_state:
    st.session_state.edit_student=None

col1,col2=st.columns(2)

# LEFT COLUMNS

with col1:
    st.subheader("📝Register Student")

    with st.form("stu_reg_form",clear_on_submit=True):
        stu_name=st.text_input("Student Name")

        stu_age=st.number_input("Student Age",min_value=1,max_value=100,value=None)

        stu_reg_no=st.text_input("Registaion No")

        submmited=st.form_submit_button("Register Now",use_container_width=True)
        if submmited:
            try:
                success= insert_student(stu_name.strip(),int(stu_age),stu_reg_no.strip())
                if success:
                    st.success(f"✅ {stu_name} Registered suceessfully")
                    st.rerun()
            except Exception as e:
                st.error("Error :",str(e))

if st.session_state.edit_student:
    student=st.session_state.edit_student
    st.divider()
    st.subheader("📝 Update Student Details")

    with st.form("update_form"):
        u_name=st.text_input("Student Name",value=student['stu_name'])

        u_age=st.text_input("Student Age",value=int(student['stu_age']))

        u_reg_no=st.text_input("Student Reg No",value=student['stu_reg_no'])

        c1,c2=st.columns(2)

        save=c1.form_submit_button("💾 Save Changes",use_container_width=True)
        cancel=c2.form_submit_button("Cancel",use_container_width=True)
    
    if save:
        st.success("Update succesfully ")
        st.session_state.edit_student=None
        st.rerun()

    if cancel:
        st.success("Cancelled succesfully ")
        st.session_state.edit_student=None
        st.rerun()


# RIGHT COLUMN
with col2:
    st.subheader("📂 Registered Student")

    try:
        students=get_all_students()
        if students:
            header=st.columns([0.7,2.5,1,2.5,1.2])
            header[0].markdown("ID")
            header[1].markdown("NAME")
            header[2].markdown("AGE")
            header[3].markdown("REG NO")
            header[4].markdown("ACTIONS")

            with st.container(height=300):
                for student in students:
                    with st.container(border=True):
                        c1,c2,c3,c4,c5=st.columns(
                            [0.7,2.5,1,2.5,2],
                            vertical_alignment="center"
                            )
                        c1.write(f"{student['id']}")
                        c2.write(f"{student['stu_name']}")
                        c3.write(f"{student['stu_age']}")
                        c4.write(f"{student['stu_reg_no']}")
                        delete_col1,edit_col1=c5.columns(2)


                        with delete_col1:
                            if st.button("🗑️",key=F"delete_{student['id']}",use_container_width=True):
                                delete_student(student['id'])
                                st.rerun()
                                

                        with edit_col1:
                            if st.button("📝",key=F"edit_{student['id']}",use_container_width=True):
                                # edit_student(student['id'])
                                st.session_state.edit_student=student
                                st.rerun()
                                # st.success(f" {student['stu_name']} Updated Successfully ")
        else:
            st.info("No Student Registered yet")
    except Exception as e:
        st.error(f"Could not load student {e}")