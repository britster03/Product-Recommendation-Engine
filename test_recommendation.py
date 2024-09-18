# test_recommendation.py

from src.product_api import fetch_products
from src.recommendation import recommend_products, get_product_embeddings

def test_recommendation():
    df = fetch_products()
    if df.empty:
        print("No products fetched. Test aborted.")
        return
    
    descriptions = df['description'].tolist()
    embeddings = get_product_embeddings(descriptions)
    
    user_query = "I'm looking for a comfortable office chair."
    recommendations = recommend_products(user_query, df, embeddings, top_n=3)
    
    print("Recommendations:")
    for idx, row in recommendations.iterrows():
        print(f"- {row['title']} (${row['price']})")

if __name__ == "__main__":
    test_recommendation()
