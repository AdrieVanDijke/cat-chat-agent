import os
import pinecone
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.agents.agent_toolkits import create_retriever_tool
from langchain.vectorstores import Pinecone
import streamlit as st
import itertools

class PineconeRetriever:
    def __init__(self):
        os.environ["OPENAI_API_KEY"] = st.secrets["OPENAI_API_KEY"]
        pinecone.init(api_key=st.secrets["PINECONE_API_KEY"], environment=st.secrets["PINECONE_ENVIRONMENT"])

        embeddings = OpenAIEmbeddings(client='')
        docsearch = Pinecone.from_existing_index(
            index_name=st.secrets["PINECONE_INDEX_NAME"], embedding=embeddings)
        retriever = docsearch.as_retriever()
        self.retriever_tool = create_retriever_tool(
            retriever,
            name="qa_conversational_business",
            description="Searches and returns documents regarding conversational business. Input: send the user input."
        )
        #print(dir(self.retriever_tool))

    def retrieve_documents(self, query):
        # geeft 4 documenten terug
        #return self.retriever_tool.run(query)

        # toon alleen de eerste 2 documenten oplossing:
        results = self.retriever_tool.run(query)

        return list(itertools.islice(results, 2))