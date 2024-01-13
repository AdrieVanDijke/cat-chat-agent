from a3d.a3dmodel import A3DModel
from a3d.a3dcontroler import A3DControler
from a3d.a3d_teksten import A3DTeksten
import streamlit as st

class A3DGUI:
    def __init__(self):
        self.a3dmod = A3DModel()
        self.a3dcon = A3DControler(self.a3dmod)
        self.a3dtekst = A3DTeksten()
        if 'var' not in st.session_state:
            st.session_state['var'] = 0
        if 'naam' not in st.session_state:
            st.session_state['naam'] = ''
        # Initialize chat history
        if "messages" not in st.session_state:
            st.session_state['messages'] = []

    def start(self): 
        # haal data uit de url =================
        url = st.query_params
        if url != {}:
            if 'var' in url:
                var = url['var']
                st.session_state['var'] = var                   
            if 'naam' in url:
                naam = url['naam']
                st.session_state['naam'] = naam                       
        self.build_gui()

    # Bouw GUI op ========================================================
    def build_gui(self):
        st.subheader("🤖 Chat met CATja *- onze AI-bot*")
        with st.expander("ℹ️ Disclaimer"):
            st.write(self.a3dtekst.get_intro_tekst())
             
        # Display chat messages from history on app rerun
        for message in st.session_state.messages:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])
       
        # React to user input        
        if prompt := st.chat_input("Voer hier je vraag in..."):            
            # Display user message in chat message container
            st.chat_message("user").markdown(prompt)
            preloader = st.empty()
            # Add user message to chat history
            st.session_state.messages.append({"role": "user", "content": prompt})
            preloader.text("🕵️ Een moment geduld a.u.b...")

            response = self.a3dcon.ask_the_database(prompt)
            preloader.empty()

            # Display assistant response in chat message container
            with st.chat_message("assistant"):
                st.markdown(response)
            # Add assistant response to chat history
            st.session_state.messages.append({"role": "assistant", "content": response})

    # Workers =============================================================
    # Callbacks ====================================
       






    
    


