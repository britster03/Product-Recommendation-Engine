# src/recommendation.py

from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
from cachetools import TTLCache, cached
from cachetools.keys import hashkey

# Initialize cache with TTL of 1 hour and max size of 1000
cache = TTLCache(maxsize=1000, ttl=3600)

def tuple_key(descriptions):
    """
    Converts a list of descriptions to a tuple to make it hashable.
    """
    return hashkey(tuple(descriptions))

@cached(cache)  # Use default key since there are no arguments
def load_model():
    """
    Loads the SentenceTransformer model.
    Caches the model to avoid reloading on every function call.
    """
    model = SentenceTransformer('all-MiniLM-L6-v2')  # Efficient and effective model
    return model

model = load_model()

@cached(cache, key=tuple_key)  # Use custom key function for caching
def get_product_embeddings(descriptions):
    """
    Generates embeddings for each product description.
    Caches the embeddings to avoid recomputation.
    """
    embeddings = model.encode(descriptions, convert_to_tensor=True)
    return embeddings

def recommend_products(user_query, df, embeddings, top_n=5):
    """
    Recommends top_n products based on user_query.
    """
    user_embedding = model.encode([user_query], convert_to_tensor=True)
    similarities = cosine_similarity(user_embedding.cpu(), embeddings.cpu())[0]
    top_indices = similarities.argsort()[-top_n:][::-1]
    recommended = df.iloc[top_indices]
    return recommended
