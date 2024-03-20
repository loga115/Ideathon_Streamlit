import streamlit as st
from openpyxl import Workbook

def write_to_xlsx(data):
    wb = Workbook()
    sheet = wb.active
    sheet.append(data)
    wb.save('test.xlsx')

def main():
    
    st.title("Streamlit Form")
    name = st.text_input("Name")
    email = st.text_input("Email")
    age = st.number_input("Age")
    gender = st.selectbox("Gender", ["Male", "Female", "Other"])

    if st.button("Submit"):
        data = [name, email, age]
        write_to_xlsx(data)
        st.success("Data written to test.xlsx")

if __name__ == "__main__":
    main()
