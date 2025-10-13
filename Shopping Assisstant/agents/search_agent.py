# import requests

# class SearchAgent:
#     FAKE_STORE_API = "https://dummyjson.com/products/search"

#     def search_products(self, query):
#         try:
#             response = requests.get(f"{self.FAKE_STORE_API}?q={query}")
#             response.raise_for_status()
#             result = response.json()
#             return result.get("products", [])
#         except requests.RequestException:
#             return []


import requests
import re

class SearchAgent:
    FAKE_STORE_API = "https://dummyjson.com/products/search"
    ALL_PRODUCTS_API = "https://dummyjson.com/products"

    # Basic keywords for demo, can be expanded
    PRODUCT_KEYWORDS = [
        "phone", "laptop", "headphone", "earbud", "tablet", "speaker", "watch", "backpack", "camera"
    ]
    
    def extract_keyword(self, query):
        # Look for a known keyword in the query, else fallback
        query_lower = query.lower()
        for word in self.PRODUCT_KEYWORDS:
            if word in query_lower:
                return word
        # Try fallback simple noun extraction
        match = re.search(r"\b(?:for a|a|an|the)\s+([a-zA-Z]+)", query_lower)
        if match:
            return match.group(1)
        return ""

    def search_products(self, query):
        keyword = self.extract_keyword(query)
        if keyword:
            response = requests.get(f"{self.FAKE_STORE_API}?q={keyword}")
            if response.ok and response.json().get("products"):
                return response.json()["products"]
        # Fallback: fetch all products if search failed or result empty
        response = requests.get(self.ALL_PRODUCTS_API)
        if response.ok:
            return response.json().get("products", [])
        return []
