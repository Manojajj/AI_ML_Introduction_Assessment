import streamlit as st
from fpdf import FPDF  # For PDF generation

# Define questions, options, and correct answers
questions = [
    "What is Artificial Intelligence (AI)?",
    "Which of the following is an example of Narrow AI?",
    # Add all other questions here
]
options = [
    ["A subset of computer science that focuses on visual data analysis.",
     "A field focused on creating machines that mimic human intelligence.",
     "A technology for building physical robots.",
     "A programming language used for automation."],
    ["A machine capable of reasoning like a human.",
     "A general-purpose robot capable of any intellectual task.",
     "A voice assistant like Siri or Alexa.",
     "A self-aware autonomous agent."],
    # Add options for other questions
]
correct_answers = [
    "A field focused on creating machines that mimic human intelligence.",
    "A voice assistant like Siri or Alexa.",
    # Add correct answers for other questions
]

# Create a Streamlit form for the quiz
st.title("AI & ML Quiz")
user_answers = []  # To store user answers
score = 0  # To keep track of scores

for i, question in enumerate(questions):
    st.write(f"**Q{i+1}.** {question}")
    answer = st.radio("Select your answer:", options[i], key=f"q{i}")
    user_answers.append(answer)

# Calculate the score and display it
if st.button("Submit Quiz"):
    for i, answer in enumerate(user_answers):
        if answer == correct_answers[i]:
            score += 1
    st.success(f"Your Score: {score}/{len(questions)}")

    # Generate the quiz result document (using FPDF or another library)
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    for i, question in enumerate(questions):
        pdf.cell(200, 10, f"Q{i+1}: {question}", ln=True)
        pdf.cell(200, 10, f"Your Answer: {user_answers[i]}", ln=True)
        pdf.cell(200, 10, f"Correct Answer: {correct_answers[i]}", ln=True)
        pdf.cell(200, 10, " ", ln=True)  # Add a space between questions

    # Save the document
    pdf_file = "quiz_results.pdf"
    pdf.output(pdf_file)
    st.success("Quiz Results saved successfully!")
    
    # Provide a download button
    with open(pdf_file, "rb") as file:
        st.download_button("Download Quiz Results", file, file_name=pdf_file)
