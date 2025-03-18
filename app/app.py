import streamlit as st
import nltk
from nltk.tokenize import word_tokenize

# Define the chatbot's conversation flow
def conversation_flow():
    st.title("Hiring Assistant Chatbot")
    st.write("Welcome to the Hiring Assistant Chatbot!")

    # Start button
    if st.button("Start"):
        # Gather initial candidate information
        name = st.text_input("Name:")
        email = st.text_input("Email:")
        phone = st.text_input("Phone:")
        experience = st.text_input("Years of Experience:")
        position = st.text_input("Desired Position:")
        location = st.text_input("Current Location:")
        tech_stack = st.text_input("Tech Stack:")

        # Generate technical questions based on the candidate's tech stack
        questions = generate_questions(tech_stack)

        # Display the questions to the candidate
        st.write("Here are some questions based on your tech stack:")
        responses = []
        for i, question in enumerate(questions):
            st.write(question)
            response = st.text_input("Response:", key=f"response_{i}")
            responses.append(response)

        # Display the candidate's responses
        st.write("Here are your responses:")
        for response in responses:
            st.write(response)

        # Fallback Mechanism
        if st.button("I don't understand"):
            st.write("Sorry, I didn't quite get that. Can you please rephrase your question or provide more context?")

        # End Conversation
        if st.button("End Conversation"):
            st.write("Thank you for chatting with me! We will review your responses and get back to you soon. Have a great day!")

# Define the function to generate technical questions
def generate_questions(tech_stack):
    # Use a simple question generation algorithm
    questions = ["What is your experience with " + tech_stack + "?",
                 "How do you stay up-to-date with the latest developments in " + tech_stack + "?",
                 "Can you give an example of a project you worked on that involved " + tech_stack + "?"]
    return questions

# Run the conversation flow
conversation_flow()
