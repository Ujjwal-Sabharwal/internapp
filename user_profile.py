import streamlit as st
from database import getdata
from pdf import generate_pdf
from pdf import display_pdf

def show(function, name, email):
    st.title('hello ' + name)
    data1 = getdata(email)
    st.write(data1)
    if data1 is None:
        function('dgif')
    if st.button('Generate PDF'):
        # Fetch data from MySQL
        data = getdata(email)
        # Generate PDF
        pdf_buffer = generate_pdf(data)
        display_pdf(pdf_buffer)
        # Create a download link for the PDF
        st.download_button(
            label="Download PDF",
            data=pdf_buffer,
            file_name="data_report.pdf",
            mime="application/pdf"
        )
    if st.button('logout'):
        function('Login')
