import streamlit as st

# Create a session state
if 'name' not in st.session_state:
    st.session_state.name = ''

# Define the app's pages
def start_page():
    st.title("Hiring Assistant Chatbot")
    st.write("Welcome to the Hiring Assistant Chatbot!")
    name = st.text_input("Name:")
    st.session_state.name = name
    if st.button("Start"):
        st.experimental_rerun()

def conversation_page():
    st.title("Conversation Page")
    st.write("Hello, " + st.session_state.name + "!")

# Define the app's logic
def main():
    if st.session_state.name == '':
        start_page()
    else:
        conversation_page()

# Run the app
if __name__ == "__main__":
    main()
