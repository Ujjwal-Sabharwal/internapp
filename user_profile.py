import streamlit as st
from database import getdata
from database import check_post
from pdf import generate_pdf

def show(function, name, email):
    st.title('Hello ' + name)
    # Fetch data from MySQL
    data = getdata(email)
    if data is None:
        function('dgif')
    data1 = check_post(email)
    if data1:
        st.title('Another Input')


    # Generate PDF
    pdf_buffer,table = generate_pdf(data)
    st.table(table)
    # Create a download link for the PDF
    st.download_button(
        label="Download PDF",
        data=pdf_buffer,
        file_name="data_report.pdf",
        mime="application/pdf"
    )

    if st.button('logout'):
        function('Login')
