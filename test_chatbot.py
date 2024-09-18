# test_chatbot.py

from src.chatbot import get_chatbot_response

def test_chatbot():
    user_input = "Hello! Can you recommend a good laptop for gaming?"
    response = get_chatbot_response(user_input)
    print("Bot:", response)

if __name__ == "__main__":
    test_chatbot()
