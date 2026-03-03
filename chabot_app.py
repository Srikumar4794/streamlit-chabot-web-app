from dotenv import load_dotenv
import streamlit as st
from langchain_groq import ChatGroq
from langchain_openai import ChatOpenAI
from langchain_google_genai import ChatGoogleGenerativeAI

#load the env variables from the .env file
load_dotenv()

# streamlit page setup
st.set_page_config(page_title="💬Chatbot", page_icon="🤖", layout="centered")
st.title("💬 Generative AI Chatbot")

model_name = st.selectbox("Select a model", ["llama-3.3-70b-versatile", "gpt-4.1"])

if model_name == "llama-3.3-70b-versatile":
    llm = ChatGroq(model="llama-3.3-70b-versatile" ,temperature=0)
elif model_name == "gpt-4.1":
    llm = ChatOpenAI(model="gpt-4.1" ,temperature=0)

# initiate chat history in session state if it doesn't exist
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

for message in st.session_state.chat_history:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

user_prompt = st.chat_input("Ask me anything:")

if(user_prompt):
   with st.chat_message("user"):
        st.markdown(user_prompt)
   st.session_state.chat_history.append({"role": "user", "content": user_prompt})

   response = llm.invoke(input=[{"role": "system", "content": "You are a helpful assistant."}] + st.session_state.chat_history)

   with st.chat_message("assistant"):
         st.markdown(response.content)
   st.session_state.chat_history.append({"role": "assistant", "content": response.content})
