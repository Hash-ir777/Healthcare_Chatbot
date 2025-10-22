import streamlit as st
import pandas as pd
from langchain_ollama import OllamaLLM

# Streamlit setup
st.set_page_config(page_title="CSV Chatbot", page_icon="🤖", layout="centered")
st.title("💬 CSV-Based Chatbot (Llama 3.2 + Ollama)")

# File uploader
uploaded_file = st.file_uploader("Upload your CSV file:", type=["csv"])
use_sample = st.checkbox("Use example dataset (symptom_Description.csv)")

df = None
if uploaded_file:
    df = pd.read_csv(uploaded_file)
elif use_sample:
    try:
        df = pd.read_csv("symptom_Description.csv")
        st.success("Loaded example dataset.")
    except Exception as e:
        st.error(f"Could not load example dataset: {e}")

if df is not None:
    st.write("### Preview:")
    st.dataframe(df.head())
else:
    st.info("⬆️ Please upload a CSV file or select 'Use example dataset' to begin.")
    # do not stop the app; allowing the chat input to be visible for convenience

# Initialize LLM
llm = None
try:
    llm = OllamaLLM(model="llama3.2", temperature=0)
except Exception as e:
    st.warning(f"Ollama LLM not available: {e}\nResponses will be simulated locally.")

# Initialize chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Display past messages (if any)
for message in st.session_state.chat_history:
    try:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
    except Exception:
        # fallback rendering
        st.write(f"{message['role'].title()}: {message['content']}")

# Provide chat input with a fallback for older Streamlit versions
user_input = None
try:
    # Preferred API when available
    user_input = st.chat_input("Ask me about your data...")
except Exception:
    # Fallback to text_input for older Streamlit
    user_input = st.text_input("Ask me about your data...")

if user_input:
    # render user's message
    try:
        st.chat_message("user").markdown(user_input)
    except Exception:
        st.write(f"User: {user_input}")
    st.session_state.chat_history.append({"role": "user", "content": user_input})

    # Combine context from the dataframe
    context = df.head(50).to_string(index=False)  # show first 50 rows as context
    prompt = f"""You are a data assistant. Use the table data below to answer user queries.
Data:
{context}

User question: {user_input}
Answer based only on the data above when possible.
"""

    with st.spinner("Thinking..."):
        response = None
        if llm is not None:
            try:
                # Some wrappers return a dict or object; normalize to string
                raw = llm.invoke(prompt)
                if isinstance(raw, (dict,)) and "content" in raw:
                    response = raw["content"]
                else:
                    response = str(raw)
            except Exception as e:
                response = f"LLM call failed: {e}"
        else:
            # Simple local heuristic: echo and summarize
            response = "I don't have an LLM available. Based on the provided data, please check the CSV; I can answer simple questions about column names or row counts."

    st.session_state.chat_history.append({"role": "assistant", "content": response})
    try:
        with st.chat_message("assistant"):
            st.markdown(response)
    except Exception:
        st.write(f"Assistant: {response}")
