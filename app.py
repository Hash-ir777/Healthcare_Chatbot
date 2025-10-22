import streamlit as st
import pandas as pd
from langchain_ollama import OllamaLLM

st.set_page_config(page_title="Medical CSV Chatbot", page_icon="🩺", layout="centered")
st.title("💬 Medical Data Chatbot (Llama 3.2 + Ollama)")

# --- Preload default datasets ---
default_files = {
    "Symptom_severity.csv": None,
    "symptom_Description.csv": None,
    "symptom_precaution.csv": None
}

for file in default_files:
    try:
        default_files[file] = pd.read_csv(file)
        st.success(f"Loaded default dataset: {file}")
    except Exception as e:
        st.warning(f"Could not load {file}: {e}")

# --- Handle file uploads too ---
uploaded_files = st.file_uploader("Upload extra CSV files", type=["csv"], accept_multiple_files=True)
if uploaded_files:
    for f in uploaded_files:
        default_files[f.name] = pd.read_csv(f)
        st.success(f"Added uploaded dataset: {f.name}")

# Combine all into one dictionary
st.session_state.dfs = default_files

# Display available datasets
for name, df in st.session_state.dfs.items():
    if df is not None:
        with st.expander(f"📄 {name}"):
            st.dataframe(df.head())

# --- Chat interaction ---
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

user_input = st.chat_input("Ask about symptoms, severity, or precautions...")

if user_input:
    st.chat_message("user").markdown(user_input)
    st.session_state.chat_history.append({"role": "user", "content": user_input})

    context = "\n\n".join(
        [df.head(50).to_string(index=False) for df in st.session_state.dfs.values() if df is not None]
    )

    prompt = f"""
You are a helpful medical assistant.
Use the data below to answer questions accurately.


Data:
{context}

Question: {user_input}
"""

    llm = OllamaLLM(model="llama3.2", temperature=0)
    response = llm.invoke(prompt)
    response_text = str(response) if not isinstance(response, dict) else response.get("content", str(response))

    st.chat_message("assistant").markdown(response_text)
    st.session_state.chat_history.append({"role": "assistant", "content": response_text})
