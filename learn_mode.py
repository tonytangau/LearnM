import os
import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

API_URL = "https://api.deepseek.com"
API_KEY = os.getenv('DEEP_SEEK_API_KEY')
MODEL = "deepseek-chat"

# Streamlit app title
st.title("LearnM: AI-Powered Learning")

# System role for the AI assistant
SYSTEM_ROLE = """
You are a knowledgeable and friendly learning assistant for students. Your goal is to help users understand topics deeply by providing clear explanations, examples, and resources. Follow these rules:
1. Always respond in a structured format with the following sections: Key Concepts, Examples, FAQs, and Suggested Resources.
2. Use simple, easy-to-understand language and avoid jargon.
3. Make your explanations engaging and interactive.
4. Ask questions to check the user's understanding and encourage critical thinking.
"""

def generate_study_guide(topic: str) -> str:
    client = OpenAI(api_key=API_KEY, base_url=API_URL)

    prompt = f"""
    Create a detailed study guide for the topic: {topic}. Include:
    - Key concepts and definitions.
    - Examples or analogies to explain the topic.
    - Frequently asked questions (FAQs).
    - Links to external resources (blogs, books, videos, online courses).
    """

    try:
        response = client.chat.completions.create(
            model=MODEL,
            messages=[
                {"role": "system", "content": SYSTEM_ROLE},
                {"role": "user", "content": prompt},
            ],
            stream=False,
        )
        return response.choices[0].message.content
    except Exception as e:
        st.error(f"API Error: {e}")
        return None

def main():
    # Input box for the topic
    topic = st.text_input("Enter a topic to learn:")

    # Generate button
    if st.button("Generate Study Guide"):
        if topic:
            with st.spinner("Generating study guide..."):
                study_guide = generate_study_guide(topic)
                if study_guide:
                    st.write(study_guide)
        else:
            st.warning("Please enter a topic!")

# Run the app
if __name__ == "__main__":
    main()