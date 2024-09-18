# app.py

import streamlit as st
from src.product_api import fetch_products
from src.recommendation import recommend_products, get_product_embeddings
from src.chatbot import get_chatbot_response
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(page_title="🛍️ AI-Powered Chatbot with Product Recommendations", layout="wide")
st.title("🛍️ AI-Powered Chatbot with Product Recommendations")

# Initialize session state for conversation history
if 'conversation' not in st.session_state:
    st.session_state['conversation'] = []

# Sidebar for product search
st.sidebar.header("🔍 Product Search")
search_query = st.sidebar.text_input("Enter product keywords:", "")
search_button = st.sidebar.button("Search")


if search_button and search_query:
    with st.spinner("Fetching and processing recommendations..."):
        df_products = fetch_products()
        if not df_products.empty:
            embeddings = get_product_embeddings(df_products['description'].tolist())
            recommendations = recommend_products(search_query, df_products, embeddings, top_n=5)
            rec_text = "### Recommendations based on your query:\n"
            rec_text += '\n'.join([f"- {row['title']} - ${row['price']}\n[View Product](https://fakestoreapi.com/products/{row['id']})" for idx, row in recommendations.iterrows()])
            st.session_state['conversation'].append(("Bot", rec_text))

# Chat Display
chat_container = st.container()
with chat_container:
    for sender, message in st.session_state['conversation']:
        if sender == "User":
            st.text_area("You said:", value=message, height=75)
        else:  # Bot response
            st.text_area("Bot:", value=message, height=150)

# User Input
user_input = st.text_input("Type your message here:")
submit_button = st.button("Send")

if submit_button and user_input:
    # Append user message to the conversation history
    st.session_state['conversation'].append(("User", user_input))
    
    # Generate bot response
    bot_response = get_chatbot_response(user_input)
    st.session_state['conversation'].append(("Bot", bot_response))

    # Force a rerun of the page to update the chat display
    st.rerun()
