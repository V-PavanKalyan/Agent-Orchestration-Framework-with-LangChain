# from agents.search_agent import SearchAgent
# from agents.price_agent import PriceAgent
# from agents.review_agent import ReviewAgent

# class CoordinatorAgent:
#     def __init__(self):
#         self.search_agent = SearchAgent()
#         self.price_agent = PriceAgent()
#         self.review_agent = ReviewAgent()

#     def search_and_recommend(self, query, budget=None):
#         # 1. Search products based on query
#         products = self.search_agent.search_products(query)

#         if not products:
#             return []

#         # 2. Price filtering if budget is given
#         if budget:
#             products = self.price_agent.filter_by_budget(products, budget)

#         # 3. Retrieve reviews and ratings for products
#         products = self.review_agent.add_reviews(products)

#         # 4. Final product recommendation logic (e.g. rank by rating and price)
#         recommended = sorted(products, key=lambda x: (-x.get('rating', 0), x['price']))

#         return recommended[:5]  # Return top 5 recommendations


# import re

# class CoordinatorAgent:
#     def __init__(self):
#         from agents.search_agent import SearchAgent
#         from agents.price_agent import PriceAgent
#         from agents.review_agent import ReviewAgent
#         self.search_agent = SearchAgent()
#         self.price_agent = PriceAgent()
#         self.review_agent = ReviewAgent()

#     def contextual_search(self, query, previous_products=None):
#         # Extract budget, brand, product type from query
#         brand = self.extract_brand(query)
#         product_type = self.extract_type(query)
#         budget = self.extract_budget(query)

#         products = previous_products if previous_products else self.search_agent.search_products(product_type or query)
#         if brand:
#             products = [p for p in products if brand.lower() in p["title"].lower() or brand.lower() in p.get("brand", "").lower()]
#         if budget:
#             products = self.price_agent.filter_by_budget(products, budget)
#         products = self.review_agent.add_reviews(products)
#         return products[:10]

#     def extract_brand(self, query):
#         # Add/extend this list as needed
#         brands = ['dell', 'samsung', 'apple', 'sony', 'hp', 'asus', 'lenovo']
#         for b in brands:
#             if b in query.lower():
#                 return b
#         return None

#     def extract_type(self, query):
#         types = ['laptop', 'phone', 'headphone', 'watch', 'tablet']
#         for t in types:
#             if t in query.lower():
#                 return t
#         return None

#     def extract_budget(self, query):
#         match = re.search(r'under (\d+)', query.lower())
#         if match:
#             return float(match.group(1))
#         return None











import re

class CoordinatorAgent:
    def __init__(self):
        from agents.search_agent import SearchAgent
        from agents.price_agent import PriceAgent
        from agents.review_agent import ReviewAgent
        self.search_agent = SearchAgent()
        self.price_agent = PriceAgent()
        self.review_agent = ReviewAgent()
        self.KNOWN_BRANDS = ['dell', 'hp', 'samsung', 'apple', 'sony', 'asus', 'lenovo', 'boat', 'jbl']
        self.KNOWN_TYPES = ['laptop', 'phone', 'headphone', 'earbud', 'tablet', 'backpack', 'watch', 'monitor']

    def contextual_search(self, query, previous_products=None):
        # Extract constraints
        brand = self.extract_brand(query)
        prod_type = self.extract_type(query)
        budget = self.extract_budget(query)

        products = previous_products if previous_products else self.search_agent.search_products(prod_type or query)
        if brand:
            products = [p for p in products if brand.lower() in p['title'].lower() or brand.lower() in p.get("brand", "").lower()]
        if budget:
            products = self.price_agent.filter_by_budget(products, budget)
        products = self.review_agent.add_reviews(products)
        products = sorted(products, key=lambda x: (-x.get('rating', 0), x['price']))
        return products[:10]

    def extract_brand(self, query):
        for b in self.KNOWN_BRANDS:
            if b in query.lower():
                return b
        return None

    def extract_type(self, query):
        for t in self.KNOWN_TYPES:
            if t in query.lower():
                return t
        return None

    def extract_budget(self, query):
        for pat in [r'under\s+(\d+)', r'below\s+(\d+)', r'max\s*(\d+)']:
            m = re.search(pat, query.lower())
            if m: return float(m.group(1))
        return None
