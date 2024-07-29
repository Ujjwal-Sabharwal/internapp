import mysql.connector


def getdata(email):
    # Establish a connection to the MySQL database
    mydb = mysql.connector.connect(
        host='localhost',
        user='root',
        passwd='12345678',
        database='ujjwal'
    )
    # Create a cursor object to interact with the database
    cursorObject = mydb.cursor()
    cursorObject.execute('SELECT * FROM data WHERE email = %s', (email,))
    result = cursorObject.fetchone()
    return result

