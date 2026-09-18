# AI MCQ Generator

## Live Application

Access the deployed application:

https://mcq-generator-eslp2qpkrhaz89qxn2sekq.streamlit.app/


## Project Overview

AI MCQ Generator is a Generative AI-based educational application developed using Python, Streamlit, and Hugging Face.

The application enables users to enter an educational topic and generate multiple-choice questions using an AI language model. Each generated question includes four answer options, the correct answer, and a short explanation.

The project demonstrates how Generative AI and web application technologies can be integrated to create an interactive learning support tool.

## Objectives

- Automate the generation of educational multiple-choice questions.
- Support topic-based learning and practice.
- Provide questions with multiple answer options.
- Display correct answers and short explanations.
- Demonstrate the integration of a Large Language Model with Streamlit.
- Implement secure API token management.

## Key Features

- Topic-based MCQ generation
- Customizable number of questions
- Four answer options for each question
- Correct answer generation
- Short explanations for generated questions
- Interactive Streamlit interface
- Hugging Face Inference API integration
- Secure token management using Streamlit Secrets

## Technologies Used

| Technology | Purpose |
|------------|---------|
| Python | Application development |
| Streamlit | Web application interface |
| Hugging Face | AI model integration |
| Hugging Face Inference API | AI-powered text generation |
| OpenAI GPT-OSS-120B | Language model used for question generation |

## Application Workflow

1. The user enters an educational topic.
2. The user selects the required number of questions.
3. The application sends the request to the Hugging Face Inference API.
4. The AI model generates multiple-choice questions.
5. The application displays the questions, options, correct answers, and explanations.

## Project Structure

```text
mcq-generator/
│
├── app.py
├── requirements.txt
├── README.md
└── .gitignore
