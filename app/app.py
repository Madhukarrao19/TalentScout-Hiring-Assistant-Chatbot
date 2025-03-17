import streamlit as st
import importlib.metadata

st.title("TalentScout Hiring Assistant Chatbox")
st.write("Welcome to the TalentScout Hiring Assistant Chatbox!")

def conversation_flow():
    st.write("Please enter your name and tech stack to get started.")

    name = st.text_input("Name:")
    tech_stack = st.text_input("Tech Stack:")

    questions = generate_questions(tech_stack)

    st.write("Here are some questions based on your tech stack:")
    responses = []
    for question in questions:
        st.write(question)
        response = st.text_input("Response:")
        responses.append(response)

    st.write("Here are your responses:")
    for response in responses:
        st.write(response)

def generate_questions(tech_stack):
    # Use a simple question generation algorithm
    questions = ["What is your experience with " + tech_stack + "?",
                 "How do you stay up-to-date with the latest developments in " + tech_stack + "?",
                 "Can you give an example of a project you worked on that involved " + tech_stack + "?"]
    return questions

conversation_flow()