import os
import streamlit as st

os.environ["OPENAI_API_KEY"] = st.secrets["OPENAI_API_KEY"]

class A3DModel:
    def __init__(self):
        self.api_openai_key = st.secrets["OPENAI_API_KEY"]
        self.pinecone_api_key = st.secrets["PINECONE_API_KEY"]
        self.pinecone_environment = st.secrets["PINECONE_ENVIRONMENT"]
        self.pinecone_index_name = st.secrets["PINECONE_INDEX_NAME"]
        self.aimodel = "gpt-3.5-turbo-1106"
        self.temperature = 0.1 
        self.max_tokens = 4000 


        
        