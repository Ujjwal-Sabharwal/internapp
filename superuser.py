import streamlit as st
import mysql.connector
import pandas as pd
from mysql.connector import Error


def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="12345678",
        database="ujjwal"
    )


def fetch_data():
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


def transfer_data(row_id):
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


def show(function):
    st.title("Admin Page")

    # Fetch data from MySQL
    data = fetch_data()

    # Display data in a table
    for index, row in data.iterrows():
        col1,col2 = st.columns(2)
        with col1:
            st.table(row)
        with col2:
            if st.button("Allow",key=index):
                transfer_data(row['email'])
                st.rerun()

    if st.button('logout'):
        function('Login')

