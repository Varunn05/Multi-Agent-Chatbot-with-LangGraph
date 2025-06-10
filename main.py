import streamlit as st
import requests

st.set_page_config(page_title="Multi Agent Chatbot", layout="centered")
st.title("Chatbot")
st.write("Interact with AI Agents!")

system_prompt=st.text_area("Define you AI Agent: ", height=70, placeholder="Type your system prompt here...")

MODEL_NAMES_GROQ = ["llama-3.3-70b-versatile", "mixtral-8x7b-32768"]
MODEL_NAMES_OPENAI = ["gpt-4o-mini"]

provider=st.radio("Select provider: ", ("Groq", "OpenAI"))

if provider=="Groq":
    selected_model=st.selectbox("Selected Groq Model:", MODEL_NAMES_GROQ)
elif provider=="OpenAI":
    selected_model=st.selectbox("Selected OpenAI Model:", MODEL_NAMES_OPENAI)

allow_web_search=st.checkbox("Allow Web Search")

user_query=st.text_area("Enter you query: ", height=120, placeholder="Ask anything...")

API_URL="http://127.0.0.1:9999/chat"

if st.button("Ask Agent!"):
    if user_query.strip():
        payload={
            "model_name": selected_model,
            "model_provider": provider,
            "system_prompt": system_prompt,
            "messages": [user_query],
            "allow_search": allow_web_search
        }
        response = requests.post(API_URL, json=payload)
        if response.status_code==200:
            response_data= response.json()
            if "error" in response_data:
                st.error(response_data["error"])
            else:    
                st.subheader("Agent response")
                st.markdown(f"**Final resposne:** {response_data}")