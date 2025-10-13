class PriceAgent:
    def filter_by_budget(self, products, budget):
        if not budget or budget <= 0:
            return products
        filtered = [
            p for p in products if p.get('price') is not None and p['price'] <= budget
        ]
        return filtered

