import streamlit as st
from transformers import pipeline

# Load Hugging Face pipeline for Named Entity Recognition (NER)
ner_pipeline = pipeline("ner", model="dslim/bert-base-NER")

# Function to extract named entities (useful for tech stacks, names, etc.)
def extract_entities(text):
    entities = ner_pipeline(text)
    extracted_info = {entity['entity']: entity['word'] for entity in entities}
    return extracted_info

# Define the chatbot's conversation flow
def conversation_flow():
    st.title("TalentScout Hiring Assistant Chatbot 🤖")
    st.write("Welcome! I will assist you with job screening and tech assessment.")

    # Gather initial candidate information
    name = st.text_input("Full Name:")
    email = st.text_input("Email Address:")
    phone = st.text_input("Phone Number:")
    experience = st.text_input("Years of Experience:")
    position = st.text_input("Desired Position:")
    location = st.text_input("Current Location:")
    tech_stack = st.text_input("Tech Stack (e.g., Python, Java, React):")

    # Extract structured info from input (Optional Enhancement)
    structured_data = extract_entities(tech_stack)
    
    # Generate technical questions based on the candidate's tech stack
    questions = generate_questions(tech_stack)

    # Display the questions to the candidate
    st.write("Here are some technical questions based on your tech stack:")
    responses = []
    for i, question in enumerate(questions):
        st.write(f"**{i+1}. {question}**")
        response = st.text_input("Your Response:", key=f"response_{i}")
        responses.append(response)

    # Display candidate responses
    st.write("**Your responses:**")
    for i, response in enumerate(responses):
        st.write(f"**Q{i+1}:** {questions[i]}")
        st.write(f"**A:** {response}")

    # Fallback & End conversation options
    if st.button("I don't understand"):
        st.write("Sorry, I didn’t quite get that. Can you rephrase?")

    if st.button("End Conversation"):
        st.write("Thank you for chatting! We will review your responses and contact you soon.")

# Function to generate technical questions based on tech stack
def generate_questions(tech_stack):
    if not tech_stack:
        return ["Please enter your tech stack to generate relevant questions."]
    
    tech_list = tech_stack.split(",")  # Convert tech stack input into a list
    questions = []
    
    for tech in tech_list:
        tech = tech.strip()  # Remove unnecessary spaces
        questions.append(f"What is your experience with {tech}?")
        questions.append(f"How do you stay up-to-date with the latest in {tech}?")
        questions.append(f"Can you give an example of a project you worked on using {tech}?")
    
    return questions[:5]  # Limit to 5 questions for brevity

# Run the chatbot
conversation_flow()
