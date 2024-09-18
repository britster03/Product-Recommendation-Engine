# src/product_api.py

import requests
import pandas as pd
from cachetools import TTLCache, cached
import streamlit as st

# Initialize cache with TTL of 1 hour and max size of 1000
cache = TTLCache(maxsize=1000, ttl=3600)

@cached(cache)
def fetch_products():
    """
    Fetches products from the Fake Store API and returns as a DataFrame.
    Caches the result for 1 hour to reduce API calls.
    """
    try:
        response = requests.get("https://fakestoreapi.com/products")
        response.raise_for_status()
        products = response.json()
        df = pd.DataFrame(products)
        return df
    except requests.exceptions.RequestException as e:
        st.error(f"Error fetching products: {e}")
        return pd.DataFrame()  # Return empty DataFrame on error
