import streamlit as st

# ======== Step 1: Define Student Class ========
class Student:
    def __init__(self, student_id, name, age, grade):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.grade = grade

    def display_info(self):
        return f"ID: {self.student_id}\nName: {self.name}\nAge: {self.age}\nGrade: {self.grade}"

# ======== Step 2: Initialize Session State ========
if "students" not in st.session_state:
    st.session_state.students = []

# ======== Step 3: Title ========
st.title("🎓 Student Management System - Farhana Yousuf")

# ======== Step 4: Add Student ========
st.header("➕ Add New Student")
with st.form("add_student_form"):
    id_input = st.text_input("Student ID", value="2482006")
    name_input = st.text_input("Name", value="Farhana Yousuf")
    age_input = st.number_input("Age", min_value=1, max_value=100, value=18, step=1)
    grade_input = st.text_input("Grade")
    add_submitted = st.form_submit_button("Add Student")

    if add_submitted:
        if id_input and name_input and grade_input:
            new_student = Student(id_input, name_input, age_input, grade_input)
            st.session_state.students.append(new_student)
            st.success("✅ Student added successfully!")
        else:
            st.error("❌ Please fill all the fields.")

# ======== Step 5: View Students ========
st.header("📋 View All Students")
if st.session_state.students:
    for s in st.session_state.students:
        st.text(s.display_info())
        st.markdown("---")
else:
    st.info("No students found.")

# ======== Step 6: Delete Student ========
st.header("❌ Delete Student")
delete_id = st.text_input("Enter Student ID to delete")
if st.button("Delete"):
    found = False
    for student in st.session_state.students:
        if student.student_id == delete_id:
            st.session_state.students.remove(student)
            st.success("🗑️ Student deleted successfully.")
            found = True
            break
    if not found:
        st.warning("⚠️ Student not found.")

# ======== Step 7: Update Student ========
st.header("✏️ Update Student")
with st.form("update_form"):
    update_id = st.text_input("Enter Student ID to update")
    new_name = st.text_input("New Name")
    new_age = st.number_input("New Age", min_value=1, max_value=100, step=1)
    new_grade = st.text_input("New Grade")
    update_submitted = st.form_submit_button("Update Student")

    if update_submitted:
        updated = False
        for student in st.session_state.students:
            if student.student_id == update_id:
                student.name = new_name or student.name
                student.age = new_age or student.age
                student.grade = new_grade or student.grade
                st.success("✅ Student updated successfully.")
                updated = True
                break
        if not updated:
            st.warning("⚠️ Student not found.")

# --- Show IDs for Reference ---
st.subheader("📌 Current Student IDs:")
if st.session_state.students:
    for s in st.session_state.students:
        st.write(s.student_id)
else:
    st.write("No students available.")
