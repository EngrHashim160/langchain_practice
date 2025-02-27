from langchain_groq import ChatGroq
from dotenv import load_dotenv
import streamlit as st
from langchain_core.prompts import PromptTemplate
import os

# Load API key from .env file
load_dotenv()

# Set up the Groq model
model = ChatGroq(
    groq_api_key=os.getenv("GROQ_API_KEY"),
    model_name="llama3-8b-8192",  # Example model, choose the right one from Groq
)


st.header("Research Tool")

paper_input = st.selectbox(
    "Select Research Paper Name", [
        "Attention is all you need",
        "BERT: Pre-training of deep bidirectional Transformers",
        "GPT-3: Language Models are Few-Shot Learners",
        "Diffusion Models Beat GANs on Image synthesis"
    ]
)

style_input = st.selectbox(
    "Select Explanation Style", [
        "Beginner-Friendly",
        "Technical",
        "Code-Oriented",
        "Mathematical"
    ]
)

length_input = st.selectbox(
    "Select Explanation Length", [
        "Short (1-2 paragraphs)",
        "Medium (3-5 paragraphs)",
        "Large (Detailed Explanation)"
    ]
)

# Template
template = PromptTemplate(
    template="""
        Please summarize the research paper titled "{paper_input}" with the following specifications:
        Explanation style: {style_input}
        Explanation Length: {length_input}
        1. Mathematical Details:
            - Include relevant mathematical equations if present in the paper.
            - Explain the mathematical concepts using simple, intuitive code snippets where applicable.
        2. Analogies:
            - Use relatable analogies to simplify the complex ideas.
        If certain information is not available in the paper, respond with: "Insufficient information available" instead of guessing.
        Ensure the summary is clear, accurate, and aligned with the provided style and length.
    """,
    input_variables=['paper_input', 'style_input', 'length_input']
)

# fill the placeholder
prompt = template.invoke(
    {
        'paper_input': paper_input,
        'style_input': style_input,
        'length_input': length_input
    }
)

if st.button("Summarize"):
    response = model.invoke(prompt)
    st.write(response.content)