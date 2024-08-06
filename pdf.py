from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
import io
import streamlit as st


def generate_pdf(data):
    buffer = io.BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=letter)
    elements = []

    # Data labels
    data_labels = [
        "Academic Level", "Age", "Gender", "No of family member", "Family annual income",
        "Background", "Who influence", "Factor Influencing",
        "Infrastructure", "Placement", "Source of information", "Frequency of support",
        "Confidence Level", "Adequate support", "Access to information", "Awareness",
        "Emotional state", "Future goal", "Overall mood"
    ]

    # Create table data with an additional column for labels
    table_data = [["Label", "Value"]]
    for label, item in zip(data_labels, data):
        table_data.append([label, str(item)])

    # Create a Table
    table = Table(table_data)
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 12),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('GRID', (0, 0), (-1, -1), 1, colors.black)
    ]))

    elements.append(table)
    doc.build(elements)

    buffer.seek(0)
    return buffer,table_data

