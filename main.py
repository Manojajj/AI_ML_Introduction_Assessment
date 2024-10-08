import streamlit as st
from fpdf import FPDF
from PyPDF2 import PdfWriter
import re

# Define the questions, options, and correct answers
# (Same as before)

# Function to remove or replace special characters
def sanitize_text(text):
    # Replace common special characters
    text = text.replace("’", "'").replace("“", '"').replace("”", '"')
    # Remove any remaining non-latin characters
    text = re.sub(r'[^\x00-\x7F]+', ' ', text)
    return text

# Create a Streamlit form for the quiz
st.title("AI & ML Quiz")
user_answers = []  # To store user answers

# Create the quiz interface
for i, question in enumerate(questions):
    sanitized_question = sanitize_text(question)
    st.write(f"**Q{i+1}.** {sanitized_question}")
    sanitized_options = [sanitize_text(option) for option in options[i]]
    answer = st.radio("Select your answer:", sanitized_options, key=f"q{i}")
    user_answers.append(sanitize_text(answer))

# Generate the PDF when the user submits the quiz
if st.button("Submit and Download Quiz Results"):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    # Write the questions, user answers, and correct answers to the PDF
    for i, question in enumerate(questions):
        pdf.cell(200, 10, f"Q{i+1}: {sanitize_text(question)}", ln=True)
        pdf.cell(200, 10, f"Your Answer: {sanitize_text(user_answers[i])}", ln=True)
        pdf.cell(200, 10, f"Correct Answer: {sanitize_text(correct_answers[i])}", ln=True)
        pdf.cell(200, 10, " ", ln=True)  # Add a space between questions

    # Save the document
    pdf_filename = "quiz_results.pdf"
    pdf.output(pdf_filename)

    # Password protection using PyPDF2
    with open(pdf_filename, "rb") as file:
        writer = PdfWriter()
        writer.appendPagesFromReader(file)
        writer.encrypt("your_password")  # Set your desired password here
        with open("protected_quiz_results.pdf", "wb") as protected_file:
            writer.write(protected_file)

    # Provide a download button for the password-protected PDF
    with open("protected_quiz_results.pdf", "rb") as protected_file:
        st.download_button("Download Password-Protected Quiz Results", protected_file, file_name="protected_quiz_results.pdf")
