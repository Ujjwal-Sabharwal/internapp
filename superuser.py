import streamlit as st
import mysql.connector
import pandas as pd
from mysql.connector import Error
import os
from dotenv import load_dotenv

def get_db_connection():
    load_dotenv()

    db_host = os.getenv("DB_HOST")
    db_user = os.getenv("DB_USER")
    db_password = os.getenv("DB_PASSWORD")
    db_name = os.getenv("DB_NAME")

    return mysql.connector.connect(
        host=db_host,
        user=db_user,
        passwd=db_password,
        database=db_name
    )

def fetch_data_employees():
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM register")
        rows = cursor.fetchall()
        columns = [desc[0] for desc in cursor.description]
        data = pd.DataFrame(rows, columns=columns)
        conn.close()
        return data
    except Error as e:
        st.error(f"Error: {e}")
        return pd.DataFrame()
def fetch_data_student():
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM user")
        rows = cursor.fetchall()
        columns = [desc[0] for desc in cursor.description]
        data = pd.DataFrame(rows, columns=columns)
        conn.close()
        return data
    except Error as e:
        st.error(f"Error: {e}")
        return pd.DataFrame()


def transfer_data_employees(row_id):
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO employes (username, email, password) SELECT username, email, password FROM register WHERE email = %s", (row_id,))
        conn.commit()
        cursor.execute("DELETE FROM register WHERE email = %s", (row_id,))
        conn.commit()
        conn.close()
        st.success("Data transferred successfully!")
    except Error as e:
        st.error(f"Error: {e}")


def transfer_data_student(row_id):
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO postenroll (username, email, password) SELECT UserName, Email, Passwd FROM user WHERE Email = %s", (row_id,))
        conn.commit()
        conn.close()
        st.success("Data transferred successfully!")
    except Error as e:
        st.error(f"Error: {e}")


def employees(function):
    st.title("Admin Page")
    st.sidebar.title("Navigation")
    if st.sidebar.button('Employees'):
        function('admin-employees')
    if st.sidebar.button('Student'):
        function('admin-student')
    # Fetch data from MySQL
    data = fetch_data_employees()
    if len(data) == 0:
        st.subheader('No More Request Pending At a Moment')
    # Display data in a table
    for index, row in data.iterrows():
        col1,col2 = st.columns(2)
        with col1:
            st.table(row)
        with col2:
            if st.button("Allow",key=index):
                transfer_data_employees(row['email'])
                st.rerun()

    if st.button('logout'):
        function('Login')


def student(function):
    st.title("Admin Page")
    st.sidebar.title("Navigation")
    if st.sidebar.button('Employees'):
        function('admin-employees')
    if st.sidebar.button('Student'):
        function('admin-student')
    data  = fetch_data_student()
    for index, row in data.iterrows():
        col1,col2 = st.columns(2)
        with col1:
            st.table(row)
        with col2:
            if st.button("Allow",key=index):
                transfer_data_student(row['Email'])
                st.rerun()

    if st.button('logout'):
        function('Login')



