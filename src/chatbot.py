# src/chatbot.py

from langchain import HuggingFaceHub
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory
from cachetools import TTLCache, cached
from dotenv import load_dotenv

load_dotenv()
# Initialize cache with TTL of 1 hour and max size of 1000
cache = TTLCache(maxsize=1000, ttl=3600)

@cached(cache)
def load_chatbot():
    """
    Initializes the LangChain chatbot with memory.
    Caches the chatbot to avoid re-initializing on every function call.
    """
    memory = ConversationBufferMemory()

    # Using HuggingFaceHub for the model
    llm = HuggingFaceHub(repo_id="HuggingFaceH4/zephyr-7b-beta", model_kwargs={"temperature": 0.1, "max_length": 10000})

    conversation = ConversationChain(llm=llm, memory=memory, verbose=False)
    
    return conversation

conversation = load_chatbot()

def get_chatbot_response(user_input):
    """
    Generates a response from the chatbot based on user_input.
    Maintains conversation context to ensure relevance.
    """
    response = conversation.run(input=user_input)
    return response.strip()
