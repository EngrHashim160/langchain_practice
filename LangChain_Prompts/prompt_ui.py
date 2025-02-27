from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import load_prompt
import streamlit as st
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

template = load_prompt('./LangChain_Prompts/template.json')

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