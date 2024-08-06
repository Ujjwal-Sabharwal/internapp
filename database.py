import mysql.connector
import os
from dotenv import load_dotenv

def getdata(email):
    load_dotenv()

    db_host = os.getenv("DB_HOST")
    db_user = os.getenv("DB_USER")
    db_password = os.getenv("DB_PASSWORD")
    db_name = os.getenv("DB_NAME")
    # Establish a connection to the MySQL database
    mydb = mysql.connector.connect(
        host=db_host,
        user=db_user,
        passwd=db_password,
        database=db_name
    )
    # Create a cursor object to interact with the database
    cursorObject = mydb.cursor()
    cursorObject.execute('SELECT * FROM data WHERE email = %s', (email,))
    result = cursorObject.fetchone()
    return result


def check_post(email):
    load_dotenv()

    db_host = os.getenv("DB_HOST")
    db_user = os.getenv("DB_USER")
    db_password = os.getenv("DB_PASSWORD")
    db_name = os.getenv("DB_NAME")
    # Establish a connection to the MySQL database
    mydb = mysql.connector.connect(
        host=db_host,
        user=db_user,
        passwd=db_password,
        database=db_name
    )
    cursorObject = mydb.cursor()
    cursorObject.execute('SELECT * FROM postenroll WHERE email = %s', (email,))
    result = cursorObject.fetchone()
    return result