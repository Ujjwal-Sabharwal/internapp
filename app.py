import streamlit as st
import mysql.connector
import input
import visulaization
import swing
import user_profile
import superuser
import verification

# Establish a connection to the MySQL database
mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='12345678',
    database='ujjwal'
)
# Create a cursor object to interact with the database
cursorObject = mydb.cursor()


def clicked(name):
    st.session_state.current_page = name
    st.rerun()


def login_page():
    st.title('Login Page')
    email = st.text_input("Enter Email: ")
    passwd = st.text_input('Enter password: ', type='password')
    col1, col2, col3, col4 = st.columns(4)
    with col2:
        if st.button("New User"):
            st.session_state.current_page = 'Register'
            st.rerun()
    with col3:
        if st.button("Forgot password"):
            st.session_state.current_page = 'Reset'
            st.rerun()
    with col1:
        if st.button('Login'):
            cursorObject.execute('SELECT * FROM user WHERE Email = %s', (email,))
            result = cursorObject.fetchone()
            cursorObject.execute('SELECT * FROM employes WHERE email = %s', (email,))
            empres = cursorObject.fetchone()
            cursorObject.execute('SELECT * FROM admin WHERE email = %s', (email,))
            adminres = cursorObject.fetchone()
            # Check if the user exists
            if (result is None) and (empres is None) and (adminres is None):
                st.error("User not found.")
                return

            if result:
                # Fetch the stored password from the result
                stored_password = result[2]
                name = result[0]

                # Verify the password
                if passwd == stored_password:
                    st.session_state.current_page = "profile"  # Redirect to 'profile' page on successful login
                    st.session_state.email = email
                    st.session_state.name = name
                    st.success('Login successful')
                    st.rerun()
                else:
                    st.error("Password does not match.")
            elif empres:
                # Fetch the stored password from the result
                stored_password = empres[2]
                name = empres[0]

                # Verify the password
                if passwd == stored_password:
                    st.session_state.admin = True
                    st.session_state.current_page = "Visulaization"  # Redirect to 'input' page on successful login
                    st.success('Login successful')
                    st.rerun()
                else:
                    st.error("Password does not match.")

            elif adminres:
                # Fetch the stored password from the result
                stored_password = adminres[1]

                # Verify the password
                if passwd == stored_password:
                    st.session_state.current_page = "admin"  # Redirect to 'input' page on successful login
                    st.success('Login successful')
                    st.rerun()
                else:
                    st.error("Password does not match.")



def register_page():
    st.title("Register Page")
    insert = "INSERT INTO user (UserName, Email, Passwd) VALUES (%s, %s, %s)"
    username = st.text_input('Enter username: ')
    email = st.text_input('Enter email: ')
    newpasswd = st.text_input('Enter password: ', type='password')
    val = (username, email, newpasswd)
    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("Register as a user"):
            st.session_state.current_page = 'verify'
            st.session_state.value = val
            st.session_state.otp = verification.otp_gen(email)
            st.rerun()
    with col2:
        if st.button("Already a user"):
            st.session_state.current_page = 'Login'
            st.rerun()
    with col3:
        if st.button('Register as authorized person'):
            if email.endswith('edu.com'):
                cursorObject.execute("INSERT INTO register (username, email, password) VALUES (%s, %s, %s)", val)
                mydb.commit()
                st.session_state.current_page = 'wait'
                st.session_state.name = username
                st.rerun()
            else:
                st.error('not a valid email')


def wait():
    st.subheader("please wait till the admin grants you access it might take one day if not done please contact authorized person")
    if st.button('Login'):
        st.session_state.current_page = 'Login'
        st.rerun()

def verify(val):
    st.subheader(f'OTP has been send to your email {val[1]}')
    # otp = verification.otp_gen(val[1])
    input_otp = st.text_input("Enter OTP")
    if st.button('verify'):
        if input_otp == st.session_state.otp:
            cursorObject.execute("INSERT INTO user (UserName, Email, Passwd) VALUES (%s, %s, %s)", val)
            mydb.commit()
            st.session_state.name = val[0]
            st.session_state.email = val[1]
            st.session_state.current_page = 'dgif'
            st.rerun()

        else:
            st.error('enter a valid otp')

def reset_page():
    st.title("Reset Page")
    email = st.text_input('Enter email: ')
    newpasswd = st.text_input('Enter new password: ', type='password')
    col1, col2 = st.columns(2)
    with col1:
        if st.button('reset password'):
            cursorObject.execute('SELECT * FROM user WHERE Email = %s', (email,))
            result = cursorObject.fetchone()

            # Check if the user exists
            if result is None:
                st.error("User not found.")
                return

            # Update the password in the database
            cursorObject.execute('UPDATE user SET Passwd = %s WHERE Email = %s', (newpasswd, email))
            mydb.commit()
            st.success("record(s) updated")
    with col2:
        if st.button("Login"):
            st.session_state.current_page = 'Login'
            st.rerun()


# def delete_page():
#     st.title('Delete Page')
#     email = st.text_input("Enter Email: ")
#     passwd = st.text_input('Enter password: ', type='password')
#     col1, col2 = st.columns(2)
#     with col1:
#         if st.button('Delete'):
#             cursorObject.execute('SELECT * FROM user WHERE Email = %s', (email,))
#             result = cursorObject.fetchone()
#
#             # Check if the user exists
#             if result is None:
#                 st.error("User not found.")
#                 return
#             stored_password = result[2]
#
#             # Verify the password
#             if passwd == stored_password:
#                 # Delete the user from the database
#                 cursorObject.execute('DELETE FROM user WHERE Email = %s', (email,))
#                 mydb.commit()
#                 st.success("User deleted successfully.")
#             else:
#                 st.error("Password does not match.")
#     with col2:
#         if st.button("Register"):
#             st.session_state.current_page = 'Register'
#             st.rerun()





pages = {
    "Visulaization": visulaization,  # 'visulaization' page module/component (typo in the module name)
    "Swing": swing  # 'swing' page module/component
}

if 'current_page' not in st.session_state:
    st.session_state.current_page = "Login"
if 'admin' not in st.session_state:
    st.session_state.admin = False

# Sidebar for navigation
if st.session_state.admin:
    st.sidebar.title("Navigation")
    selection = st.sidebar.radio("Go to", list(pages.keys()), index=list(pages.keys()).index(st.session_state.current_page))
    st.session_state.current_page = selection
    if st.sidebar.button('Logout'):
        st.session_state.admin = False
        st.session_state.current_page = 'Login'
        st.rerun()
 

# st.header('Hello')

if st.session_state.current_page == "Login":
    login_page()
elif st.session_state.current_page == "Register":
    register_page()
elif st.session_state.current_page == "Reset":
    reset_page()
elif st.session_state.current_page == "verify":
    verify(st.session_state.value)
elif st.session_state.current_page == "wait":
    wait()
# elif st.session_state.current_page == "Delete":
#     delete_page()
elif st.session_state.current_page == "dgif":
    input.dgif(clicked, st.session_state.name)
elif st.session_state.current_page == "bif":
    input.bif(clicked)
elif st.session_state.current_page == "sgif":
    input.sgif(clicked)
elif st.session_state.current_page == "iaif":
    input.iaif(clicked)
elif st.session_state.current_page == "esif":
    input.esif(clicked,st.session_state.email)
elif st.session_state.current_page == "page":
    input.page(clicked)
elif st.session_state.current_page == "admin":
    superuser.show(clicked)
elif st.session_state.current_page == "profile":
    user_profile.show(clicked,st.session_state.name,st.session_state.email)
else:
    # Render the selected page based on the current_page value
    if st.session_state.current_page in pages:
        pages[st.session_state.current_page].show()