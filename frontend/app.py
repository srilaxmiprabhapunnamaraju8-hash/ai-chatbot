import streamlit as st
import requests

# 1. Page Configuration
st.set_page_config(page_title="AI Chatbot Solution", page_icon="🚀", layout="wide")

# 2. Sidebar Navigation (Matches video structure)
st.sidebar.title("Navigation")
selection = st.sidebar.radio("Go to:", [
    "🏠 Home", 
    "💬 Live Chatbot", 
    "💻 System Architecture", 
    "🛠️ Technology Stack", 
    "📑 Documentation",
    "👩‍💻 Developer Info"
])

# --- PAGE 1: HOME ---
if selection == "🏠 Home":
    st.title("Full-Stack AI Chatbot Solution")
    st.markdown("""
    Welcome to the AI Chatbot project. This application integrates a **FastAPI** backend with a **Streamlit** frontend to deliver a seamless AI experience.
    
    **Project Highlights:**
    - Real-time communication between Frontend and Backend.
    - Integration with Google Gemini AI.
    - Responsive and interactive User Interface.
    """)

# --- PAGE 2: LIVE CHATBOT ---
elif selection == "💬 Live Chatbot":
    st.title("Live AI Assistant")
    
    if "messages" not in st.session_state:
        st.session_state.messages = []

    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    if prompt := st.chat_input("How can I assist you today?"):
        st.chat_message("user").markdown(prompt)
        st.session_state.messages.append({"role": "user", "content": prompt})

        with st.chat_message("assistant"):
            with st.spinner("Wait, I'm thinking..."):
                try:
                    # Connection to the FastAPI endpoint
                    response = requests.post("http://127.0.0.1:8000/chat", json={"message": prompt})
                    bot_reply = response.json().get("response", "Internal Server Error")
                    st.markdown(bot_reply)
                    st.session_state.messages.append({"role": "assistant", "content": bot_reply})
                except:
                    st.error("Connection failed! Please ensure the Backend (main.py) is running.")

# --- PAGE 3: SYSTEM ARCHITECTURE ---
elif selection == "💻 System Architecture":
    st.title("Architecture Overview")
    st.write("The system follows a modular architecture to ensure scalability and ease of maintenance.")
    st.image("https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png", width=150)
    st.markdown("""
    - **Client Layer**: Built with Streamlit for a rich user experience.
    - **API Layer**: FastAPI handles incoming requests and manages logic.
    - **AI Engine**: Google Gemini processes natural language and generates responses.
    """)

# --- PAGE 4: TECHNOLOGY STACK ---
elif selection == "🛠️ Technology Stack":
    st.title("Tools & Technologies")
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Frontend")
        st.write("- Streamlit")
        st.write("- Python")
    with col2:
        st.subheader("Backend")
        st.write("- FastAPI")
        st.write("- Uvicorn")
    st.subheader("AI & Hosting")
    st.write("- Google Gemini 1.5 Flash API")
    st.write("- GitHub Version Control")

# --- PAGE 5: DOCUMENTATION ---
elif selection == "📑 Documentation":
    st.title("Project Documentation")
    st.info("Submission for B.Tech 1st Year, Semester 2 Project.")
    st.write("**Key Features Implementated:**")
    st.write("- Asynchronous API handling.")
    st.write("- Session state management for chat history.")
    st.write("- Secure API key management via .env.")

# --- PAGE 6: DEVELOPER INFO ---
elif selection == "👩‍💻 Developer Info":
    st.title("Developer Credits")
    st.write("Developed with focus on full-stack AI integration.")
    st.write("**Submission Deadline:** February 5, 2026")