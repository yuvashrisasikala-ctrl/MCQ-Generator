import os
import streamlit as st
from dotenv import load_dotenv
from huggingface_hub import InferenceClient

load_dotenv()

st.set_page_config(
    page_title="AI MCQ Generator",
    page_icon="🤖"
)

st.title("🤖 AI MCQ Generator")
st.write("Generate multiple-choice questions using AI.")

HF_TOKEN = os.getenv("HF_TOKEN")

if not HF_TOKEN:
    st.error("HF_TOKEN not found in .env file")
    st.stop()

topic = st.text_input(
    "Enter Topic",
    placeholder="Example: Artificial Intelligence"
)

number = st.number_input(
    "Number of Questions",
    min_value=1,
    max_value=20,
    value=5
)

if st.button("Generate MCQs"):

    if not topic:
        st.warning("Please enter a topic.")

    else:
        try:
            client = InferenceClient(
                api_key=HF_TOKEN
            )

            prompt = f"""
Generate {number} multiple-choice questions
about {topic}.

Each question must have:
1. Question
2. Four options (A, B, C, D)
3. Correct answer
4. Short explanation

Use simple English.
Format the output clearly.
"""

            with st.spinner("Generating MCQs..."):

                response = client.chat_completion(
                    model="openai/gpt-oss-120b:fastest",
                    messages=[
                        {
                            "role": "user",
                            "content": prompt
                        }
                    ],
                    max_tokens=1500
                )

            answer = response.choices[0].message.content

            st.subheader("Generated MCQs")
            st.write(answer)

        except Exception as e:
            st.error(f"Generation Error: {e}")
