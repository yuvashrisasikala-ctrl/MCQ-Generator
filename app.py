import streamlit as st
from huggingface_hub import InferenceClient

st.set_page_config(page_title="AI MCQ Generator")

st.title("AI MCQ Generator")
st.write("Generate multiple-choice questions using AI.")

if "HF_TOKEN" not in st.secrets:
    st.error("HF_TOKEN is missing in Streamlit Secrets.")
    st.stop()

HF_TOKEN = st.secrets["HF_TOKEN"]

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

    if topic.strip() == "":
        st.warning("Please enter a topic.")

    else:
        try:
            client = InferenceClient(
                api_key=HF_TOKEN
            )

            prompt = f"""
Generate {number} multiple-choice questions about {topic}.

Each question must contain:
1. Question
2. Four options (A, B, C, D)
3. Correct answer
4. Short explanation

Use simple English.
Format clearly.
"""

            with st.spinner("Generating MCQs..."):

                response = client.chat_completion(
                    model="openai/gpt-oss-120b",
                    messages=[
                        {
                            "role": "user",
                            "content": prompt
                        }
                    ],
                    max_tokens=1500
                )

            result = response.choices[0].message.content

            st.subheader("Generated MCQs")
            st.write(result)

        except Exception as e:
            st.error(f"Generation Error: {e}")
