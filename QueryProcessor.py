from langchain.chat_models import ChatOpenAI
from langchain.prompts import (
    ChatPromptTemplate,
    MessagesPlaceholder,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
)
from langchain.chains import LLMChain
from langchain.memory import ConversationBufferMemory

class QueryProcessor:

    def __init__(self, openai_api_key):
        model_name = "gpt-3.5-turbo"
        llm = ChatOpenAI(model_name=model_name, temperature=0.7, openai_api_key = openai_api_key, verbose=False)
        prompt = ChatPromptTemplate(
            messages=[
                SystemMessagePromptTemplate.from_template(
                    "You are a nice chatbot having a conversation with a human."
                ),                
                MessagesPlaceholder(variable_name="chat_history"),
                HumanMessagePromptTemplate.from_template("Keep your answers short if possible only one to two sentences. Here is the user question: {question}")
            ]
        )
        memory = ConversationBufferMemory(memory_key="chat_history",return_messages=True)
        self.conversation = LLMChain(
            llm=llm,
            prompt=prompt,
            verbose=True,
            memory=memory
        )

    def process(self, query):
        response = self.conversation({"question": query})        
        return response['text']
