import streamlit as st
from fpdf import FPDF
from PyPDF2 import PdfWriter
import re

# Define the questions, options, and correct answers
questions = [
    "What is Artificial Intelligence (AI)?",
    "Which of the following is an example of Narrow AI?",
    "What is the main difference between Narrow AI and General AI?",
    "Which of the following areas is NOT part of AI’s core areas?",
    "What is Machine Learning (ML)?",
    "What are the three main types of Machine Learning?",
    "Which machine learning type involves learning from labeled data?",
    "Which of the following is a real-world application of Reinforcement Learning?",
    "Which machine learning algorithm is used for classification and regression tasks?",
    "What is the goal of clustering in unsupervised learning?",
    "What is the primary use of Natural Language Processing (NLP)?",
    "Which of the following describes a decision tree?",
    "What technique does Logistic Regression use to model binary outcomes?",
    "Which of the following best describes Ridge Regression?",
    "What is the primary purpose of the support vector machine (SVM) algorithm?",
    "Which feature does Random Forest leverage to improve its performance over individual decision trees?",
    "What is the role of the agent in Reinforcement Learning?",
    "Which of the following algorithms is best suited for text classification problems?",
    "Which is NOT an ethical consideration in the use of AI?",
    "What is the ultimate goal of General AI according to AI researchers?"
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
    ["Narrow AI can learn, whereas General AI cannot.",
     "General AI can perform any intellectual task, while Narrow AI is limited to specific tasks.",
     "Narrow AI refers to future theoretical systems.",
     "General AI focuses on a single specialized function."],
    ["Machine Learning", "Natural Language Processing", "Quantum Computing", "Computer Vision"],
    ["A subset of AI focused on building systems that learn from data.",
     "A technique for programming chatbots.",
     "An algorithm used exclusively for predictive analytics.",
     "A way to design data storage systems."],
    ["Structured, Unstructured, and Reinforced Learning.",
     "Supervised, Unsupervised, and Reinforcement Learning.",
     "Deep Learning, Semi-supervised, and Transfer Learning.",
     "Heuristic, Genetic, and Logical Learning."],
    ["Unsupervised Learning", "Supervised Learning", "Reinforcement Learning", "Transfer Learning"],
    ["Sorting emails into spam and non-spam categories.",
     "Predicting house prices based on previous data.",
     "An AI playing chess and improving through experience.",
     "Grouping customers based on their shopping behavior."],
    ["K-Means Clustering", "Random Forest", "Principal Component Analysis (PCA)", "Gradient Descent"],
    ["To predict the next state of the environment.",
     "To classify new data points into predefined categories.",
     "To group similar data points together based on features.",
     "To optimize parameters based on feedback."],
    ["Managing large datasets for machine learning.",
     "Analyzing and understanding human language.",
     "Recognizing objects in images.",
     "Calculating numerical results in large-scale computations."],
    ["A linear function for modeling continuous data.",
     "A flowchart-like structure used for decision-making in both classification and regression tasks.",
     "A neural network with multiple hidden layers.",
     "A clustering algorithm for segmenting data points."],
    ["The linear regression function.", "Polynomial functions.", "The sigmoid function.", "The decision boundary concept."],
    ["A regularization technique that penalizes large coefficients to reduce overfitting.",
     "A clustering technique for large datasets.",
     "An algorithm for decision-making using a tree structure.",
     "A technique that uses ensemble methods for classification."],
    ["To find a hyperplane that separates data into different classes.",
     "To classify data points into clusters based on distance.",
     "To find relationships between independent and dependent variables.",
     "To rank the importance of features in a dataset."],
    ["Dimensionality reduction", "Principal component analysis", "Ensemble learning", "Data augmentation"],
    ["To act as a mediator between supervised and unsupervised learning.",
     "To perform actions in an environment to maximize cumulative rewards.",
     "To classify data points based on probability distributions.",
     "To reduce error by minimizing variance."],
    ["K-Means", "Naive Bayes", "K-Nearest Neighbors (k-NN)", "Principal Component Analysis (PCA)"],
    ["Bias in training data", "Job displacement", "Transparency of the AI’s decision-making process",
     "The number of iterations in model training"],
    ["To replace human intelligence with machine intelligence.",
     "To create machines that can perform any intellectual task that a human can.",
     "To design AI systems that are only good at narrow, specific tasks.",
     "To enhance visual data recognition for automated systems."]
]

correct_answers = [
    "A field focused on creating machines that mimic human intelligence.",
    "A voice assistant like Siri or Alexa.",
    "General AI can perform any intellectual task, while Narrow AI is limited to specific tasks.",
    "Quantum Computing",
    "A subset of AI focused on building systems that learn from data.",
    "Supervised, Unsupervised, and Reinforcement Learning.",
    "Supervised Learning",
    "An AI playing chess and improving through experience.",
    "Random Forest",
    "To group similar data points together based on features.",
    "Analyzing and understanding human language.",
    "A flowchart-like structure used for decision-making in both classification and regression tasks.",
    "The sigmoid function.",
    "A regularization technique that penalizes large coefficients to reduce overfitting.",
    "To find a hyperplane that separates data into different classes.",
    "Ensemble learning",
    "To perform actions in an environment to maximize cumulative rewards.",
    "Naive Bayes",
    "The number of iterations in model training",
    "To create machines that can perform any intellectual task that a human can."
]

# Function to remove or replace special characters
def sanitize_text(text):
    text = text.replace("’", "'").replace("“", '"').replace("”", '"')
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
    password_protected_filename = "protected_quiz_results.pdf"
    with open(pdf_filename, "rb") as file:
        writer = PdfWriter()
        writer.append(file)
        writer.encrypt("your_password")  # Set your desired password here
        with open(password_protected_filename, "wb") as protected_file:
            writer.write(protected_file)

    # Provide a download button for the password-protected PDF
    with open(password_protected_filename, "rb") as protected_file:
        st.download_button("Download Password-Protected Quiz Results", protected_file, file_name="protected_quiz_results.pdf")
