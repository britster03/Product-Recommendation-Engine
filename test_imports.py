# test_imports.py

from src.product_api import fetch_products
from src.recommendation import recommend_products, get_product_embeddings
from src.chatbot import get_chatbot_response


def test_imports():
    print("All modules imported successfully!")

if __name__ == "__main__":
    test_imports()
