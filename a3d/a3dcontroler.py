from a3d.a3dtools import PineconeRetriever

class DocumentRetrievalAgent:
    def __init__(self):
        self.retriever = PineconeRetriever()

    def process_query(self, query):
        documents = self.retriever.retrieve_documents(query)
        # Verwerk de opgehaalde documenten en geef een antwoord of actie terug
        return documents

# Gebruik van de agent
agent = DocumentRetrievalAgent()


#agent.process_query("Wat is CAT?")       