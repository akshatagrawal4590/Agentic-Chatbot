import streamlit as st
import os
from src.langgraph_agentic_ai.ui.ui_config_file import Config

class LoadStreamlitUI:
    def __init__(self):
        self.config = Config()
        self.user_controls = {}

    def load_streamlit_ui(self):
        st.set_page_config(page_title = "🤖 " + self.config.get_page_title(), layout = "wide")
        st.header("🤖 " + self.config.get_page_title())

        with st.sidebar:

            # Get options from config
            llm_options = self.config.get_llm_options()
            usecase_options = self.config.get_usecase_options()

            # LLM Selection
            self.user_controls["selected_llm"] = st.selectbox(label = "Select LLM", options = llm_options)

            if self.user_controls["selected_llm"] == 'Groq':
                # Model Selection
                model_options = self.config.get_groq_model_options()
                self.user_controls["selected_groq_model"] = st.selectbox(label = "Select Model", options = model_options)
                self.user_controls["GROQ_API_KEY"] = st.session_state["GROQ_API_KEY"] = st.text_input(label = "API Key", type = "password")

                # Validate API Key
                if not self.user_controls["GROQ_API_KEY"]:
                    st.warning("⚠️ Please enter your GROQ API Key to proceed. Don't have? Refer : https://console.groq.com/keys")
                
            # Usecase Selection
            self.user_controls["selected_usecase"] = st.selectbox(label = "Select Usecase", options = usecase_options)

        return self.user_controls