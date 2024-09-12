import streamlit as st
import pandas as pd
import io
from llama_cpp import Llama

# Initialize the Llama model
# Initialize the Llama model
@st.cache_resource
def load_model():
    return Llama.from_pretrained(
        repo_id="TheBloke/Llama-2-7B-Chat-GGUF",
        filename="llama-2-7b-chat.Q2_K.gguf",
        n_ctx=2048,
        n_threads=4
    )
    
llm = load_model()

st.title("Local LLM Data Analysis Assistant")

# File uploader
uploaded_file = st.file_uploader("Choose a CSV or Excel file", type=["csv", "xlsx"])

if uploaded_file is not None:
    # Read the file
    if uploaded_file.name.endswith('.csv'):
        df = pd.read_csv(uploaded_file)
    else:
        df = pd.read_excel(uploaded_file)

    st.write("Data Preview:")
    st.dataframe(df.head())

    # Data info
    st.write("Data Info:")
    buffer = io.StringIO()
    df.info(buf=buffer)
    s = buffer.getvalue()
    st.text(s)

    user_input = st.text_area("Ask a question about the data:", height=100)

    if st.button("Analyze"):
        if user_input:
            # Prepare context for the LLM
            context = f"Here's some information about the dataset:\n"
            context += f"Columns: {', '.join(df.columns)}\n"
            context += f"Shape: {df.shape}\n"
            context += f"Data types:\n{df.dtypes.to_string()}\n"
            context += f"Summary statistics:\n{df.describe().to_string()}\n"

            # Generate prompt for the LLM
            prompt = f"{context}\n\nHuman: {user_input}\n\nAssistant: Based on the information provided about the dataset, I'll do my best to answer your question. "

            # Generate response from the LLM
            response = llm(prompt, max_tokens=500, stop=["Human:", "\n"], echo=False)
            
            st.write("Analysis Result:")
            st.write(response['choices'][0]['text'])
        else:
            st.warning("Please enter a question about the data.")

# Chat interface
st.sidebar.header("Chat with the LLM")
chat_input = st.sidebar.text_input("Ask a general question:")

if st.sidebar.button("Send"):
    if chat_input:
        response = llm(f"Human: {chat_input}\n\nAssistant:", max_tokens=500, stop=["Human:", "\n"], echo=False)
        st.sidebar.write("LLM Response:")
        st.sidebar.write(response['choices'][0]['text'])
    else:
        st.sidebar.warning("Please enter a question.")