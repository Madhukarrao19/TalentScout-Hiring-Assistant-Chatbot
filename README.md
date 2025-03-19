# TalentScout Hiring Assistant Chatbot

This is a hiring assistant chatbot built using Streamlit and Hugging Face Transformers. The chatbot assists in job screening by gathering essential candidate information and generating relevant technical questions based on their tech stack.

## Installation Instructions

1. Clone the repository:
   ```bash
   git clone https://github.com/Madhukarrao19/TalentScout-Hiring-Assistant-Chatbot.git
   ```
2. Navigate to the project directory:
   ```bash
   cd hiring-assistant-chatbot
   ```
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the chatbot:
   ```bash
   streamlit run app.py
   ```

## Usage Guide

1. Open the chatbot in your web browser at `http://localhost:8501`
2. Enter your details, including name, email, phone number, experience, desired position, location, and tech stack.
3. Answer the technical questions generated based on your tech stack.
4. View your responses and chatbot feedback.

## Technical Details

* The chatbot uses the `transformers` library from Hugging Face for Named Entity Recognition (NER).
* Streamlit is used for the frontend interface.
* The chatbot dynamically generates technical questions based on the candidate's provided tech stack.

## Features

* Extracts named entities from the provided tech stack using a pre-trained NER model.
* Generates relevant technical questions dynamically.
* Interactive conversation flow with candidate details and responses.

## Challenges & Solutions

* **Extracting accurate tech stack details:** Solved using Hugging Face's `dslim/bert-base-NER` model.
* **Generating relevant questions:** Implemented a structured question generation approach based on provided technologies.

## Requirements

* Python 3.8 or later
* Streamlit
* Hugging Face Transformers (for NLP processing)
* Huggingface_hub (for model integration)
* Torch

## Contributing

Contributions are welcome! If you have any suggestions or improvements, please submit a pull request.

## License

This project is licensed under the MIT License.
