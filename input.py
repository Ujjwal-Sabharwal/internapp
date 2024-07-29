import streamlit as st
import mysql.connector



# Function to insert data into MySQL database
def insert_into_db(data):
    try:
        data1 = tuple(data)
        connection = mysql.connector.connect(host='localhost',user='root',passwd='12345678',database='ujjwal')
        cursor = connection.cursor()
        query = """INSERT INTO data (academic_level, age_range, gender, family_member, anual_income, background,
                                                  influence_source, decision_factor, infra_importance, placement_importance,
                                                  info_source, support_frequency, confidence_level, guidance_support, knowledge_access,
                                                  informed_level, emotional_state, future_goals, overallmood, email)
                   VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
        cursor.execute(query, data1)
        connection.commit()
    except mysql.connector.Error as err:
        st.error(f"Error: {err}")
    finally:
        cursor.close()
        connection.close()


def dgif(function, name):
    st.title(f"WELCOME {name}")
    st.header('Demographic Influencing Factors')

    DGIF1 = st.selectbox("Please Select Your Academic Level",
                         (
                         "Senior Secondary", "Under Graduate", "Post Graduate", "Professional", "Working Professional"),
                         index=None, placeholder="Select Academic Level...", key='DGIF1')
    st.write("You selected:", DGIF1)

    DGIF2 = st.selectbox("Please Select Your Age Range",
                         ("Less Than 20", "More Than 25", "21-25"),
                         index=None, placeholder="Select your age...", key='DGIF2')
    st.write("You selected:", DGIF2)

    DGIF3 = st.selectbox("Please Select Your Gender",
                         ("Female", "Male"),
                         index=None, placeholder="Select your Gender...", key='DGIF3')
    st.write("You selected:", DGIF3)

    DGIF4 = st.number_input("Enter number of family member", value=None, placeholder="Type a number...", key='DGIF4', step=1)
    st.write("Number of family member is ", DGIF4)

    DGIF5 = st.number_input("Enter family anual income", value=None, placeholder="Type a number...", key='DGIF5', step=100000)
    st.write("Your anual family income is", DGIF5)

    DGIF6 = st.selectbox("Please Select Your Background",
                         ("Technical", "Non-Technical"),
                         index=None, placeholder="Select your Background...", key='DGIF6')
    st.write("You selected:", DGIF6)

    # Store data in session state
    if 'data' not in st.session_state:
        st.session_state.data = {}

    st.session_state.data.update({
        'DGIF1': DGIF1,
        'DGIF2': DGIF2,
        'DGIF3': DGIF3,
        'DGIF4': DGIF4,
        'DGIF5': DGIF5,
        'DGIF6': DGIF6
    })

    if st.button('next'):
        function('bif')


def bif(function):
    st.header('Basic Influencing Factor')

    BIF1 = st.selectbox("Please Select Who Influences You",
                        ("Family/Society", "Friends/Peer group", "Your own decision", "Teachers",
                         "Subject Matter Expert(SME)"),
                        index=None, placeholder="Select who influences you...", key='BIF1')
    st.write("You selected:", BIF1)

    BIF2 = st.selectbox("Please Select The Factor Influencing Your Decision",
                        ("Personal Interest", "Career Prospects", "Parental Expectations", "Academic Performance"),
                        index=None, placeholder="Select influencing factor...", key='BIF2')
    st.write("You selected:", BIF2)

    BIF3 = st.selectbox("Please Select Your Influence on the Basis of Infrastructure",
                        ("Unimportant", "Slightly Important", "Moderately Important", "Very Important",
                         "Extremely Important"),
                        index=None, placeholder="Select influence on infrastructure...", key='BIF3')
    st.write("You selected:", BIF3)

    BIF4 = st.selectbox("Please Select Your Influence on the Basis of Placement",
                        ("Unimportant", "Slightly Important", "Moderately Important", "Very Important",
                         "Extremely Important"),
                        index=None, placeholder="Select influence on placement...", key='BIF4')
    st.write("You selected:", BIF4)

    # Update session state
    st.session_state.data.update({
        'BIF1': BIF1,
        'BIF2': BIF2,
        'BIF3': BIF3,
        'BIF4': BIF4
    })

    if st.button('next', key='n1'):
        function('sgif')
    if st.button('previous', key='p1'):
        function('dgif')


def sgif(function):
    st.header('Support And Guidance Influencing Factor')

    SGIF1 = st.selectbox("Please Select Your Source Of Information",
                         ("Academic Advisors", "Friends and Peers", "Online Resources", "Family Members",
                          "Previous Students Experiences"),
                         index=None, placeholder="Select your source of information...", key='SGIF1')
    st.write("You selected:", SGIF1)

    SGIF2 = st.selectbox("Please Select Frequency Of Support",
                         ("Rarely or never", "Occasionally", "Sometimes", "Often", "Always"),
                         index=None, placeholder="Select frequency of support...", key='SGIF2')
    st.write("You selected:", SGIF2)

    SGIF3 = st.selectbox("Please Select Your Confidence level",
                         ("Not at all Confident", "Slightly Confident", "Somewhat Confident", "Fairly Confident",
                          "Extremely Confident"),
                         index=None, placeholder="Select your confidence level...", key='SGIF3')
    st.write("You selected:", SGIF3)

    # Update session state
    st.session_state.data.update({
        'SGIF1': SGIF1,
        'SGIF2': SGIF2,
        'SGIF3': SGIF3
    })

    if st.button('next', key='n2'):
        function('iaif')
    if st.button('previous', key='p2'):
        function('bif')


def iaif(function):
    st.header('Informative Awareness Influencing Factor')

    IAIF1 = st.selectbox("Please Select if you Received any support and guidance",
                         ("Yes", "No", 'Not Sure'), index=None, placeholder="Select your response...", key='IAIF1')
    st.write("You selected:", IAIF1)

    IAIF2 = st.selectbox("Please Select Amount of Access to Relevant Knowledge",
                         ("Not at all", "Slight Knowledge", "Moderate Knowledge", "Fair Knowledge",
                          "Complete Knowledge"),
                         index=None, placeholder="Select your response...", key='IAIF2')
    st.write("You selected:", IAIF2)

    IAIF3 = st.selectbox("Please Select How Well Informed You were",
                         ("Not at all", "Slight", "Somewhat about half", "Fair Understanding", "Complete Awareness"),
                         index=None, placeholder="Select your response...", key='IAIF3')
    st.write("You selected:", IAIF3)

    # Update session state
    st.session_state.data.update({
        'IAIF1': IAIF1,
        'IAIF2': IAIF2,
        'IAIF3': IAIF3
    })

    if st.button('next', key='n3'):
        function('esif')
    if st.button('previous', key='p3'):
        function('sgif')


def esif(function,email):
    st.header('Emotional State Influencing Factor')

    ESIF1 = st.selectbox("Please Select Your Overall Emotional State",
                         ("Not at all Confident", "Slightly Confident", "Somewhat Confident", "Fairly Confident",
                          "Extremely Confident"),
                         index=None, placeholder="Select your emotional state...", key='ESIF1')
    st.write("You selected:", ESIF1)

    ESIF2 = st.selectbox("Please Select Your Future Goals",
                         (
                         "Recent Trends", "Family Professional Goals", "Financial Stability", "Hobbies/interest areas ",
                         "Career Preferences"),
                         index=None, placeholder="Select your goals...", key='ESIF2')
    st.write("You selected:", ESIF2)

    ESIF3 = st.selectbox("Please Select Your Overall Mood",
                         ("Overwhelmed", "Happy", "Neutral", "Relieved", "Stressed"),
                         index=None, placeholder="Select your overall mood...", key='ESIF3')
    st.write("You selected:", ESIF3)

    # Update session state
    st.session_state.data.update({
        'ESIF1': ESIF1,
        'ESIF2': ESIF2,
        'ESIF3': ESIF3
    })

    if st.button('previous'):
        function('iaif')
    if st.button('submit', type='primary'):
        # Collect all data
        data = [
            st.session_state.data.get('DGIF1'),
            st.session_state.data.get('DGIF2'),
            st.session_state.data.get('DGIF3'),
            st.session_state.data.get('DGIF4'),
            st.session_state.data.get('DGIF5'),
            st.session_state.data.get('DGIF6'),
            st.session_state.data.get('BIF1'),
            st.session_state.data.get('BIF2'),
            st.session_state.data.get('BIF3'),
            st.session_state.data.get('BIF4'),
            st.session_state.data.get('SGIF1'),
            st.session_state.data.get('SGIF2'),
            st.session_state.data.get('SGIF3'),
            st.session_state.data.get('IAIF1'),
            st.session_state.data.get('IAIF2'),
            st.session_state.data.get('IAIF3'),
            st.session_state.data.get('ESIF1'),
            st.session_state.data.get('ESIF2'),
            st.session_state.data.get('ESIF3'),
            email
        ]
        insert_into_db(data)
        function('page')


def page(function):
    st.header('Response has been submitted successfully. Kindly log in to view your response.')
    if st.button('login', type='primary'):
        function('Login')


