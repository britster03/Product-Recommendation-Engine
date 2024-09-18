# test_product_api.py

from src.product_api import fetch_products

def test_fetch_products():
    df = fetch_products()
    assert not df.empty, "Product DataFrame should not be empty."
    print("Number of products fetched:", len(df))

if __name__ == "__main__":
    test_fetch_products()
