# import streamlit as st
# from agents.coordinator_agent import CoordinatorAgent

# st.set_page_config(page_title="Multi-Agent Shopping Assistant", page_icon="🛒", layout="centered")

# # Color and style settings for good contrast
# PRIMARY_COLOR = "#2a9d8f"
# SECONDARY_COLOR = "#264653"
# BACKGROUND_COLOR = "#f4f1de"
# TEXT_COLOR = "#1a1a1a"

# # Styling
# st.markdown(
#     f"""
#     <style>
#     .reportview-container {{
#         background-color: {BACKGROUND_COLOR};
#         color: {TEXT_COLOR};
#     }}
#     .stButton>button {{
#         background-color: {PRIMARY_COLOR};
#         color: white;
#         font-weight: bold;
#     }}
#     .stTextInput>div>input {{
#         border-radius: 5px;
#         border: 2px solid {SECONDARY_COLOR};
#         padding: 8px;
#     }}
#     </style>
#     """,
#     unsafe_allow_html=True,
# )

# st.title("Multi-Agent Shopping Assistant 🛒")

# # Input fields for query and budget
# query = st.text_input("Enter product or shopping query", max_chars=100)
# budget_input = st.text_input("Enter your budget (optional)")
# try:
#     budget = float(budget_input) if budget_input else None
# except ValueError:
#     budget = None
#     st.warning("Please enter a valid number for the budget.")
# if st.button("Search Products"):
#     if not query.strip():
#         st.warning("Please enter a valid product query to start.")
#     else:
#         # Initialize Coordinator Agent
#         coordinator = CoordinatorAgent()

#         with st.spinner("Searching products and analyzing prices, reviews..."):
#             result = coordinator.search_and_recommend(query, budget)

#         # Display final recommendations dynamically
#         if result:
#             st.subheader("Recommended Products:")
#             for idx, product in enumerate(result):
#                 st.markdown(f"### {product['title']}")
#                 st.image(product['thumbnail'], width=200)
#                 st.write(f"Price: ${product['price']}")
#                 st.write(f"Rating: {product.get('rating', 'N/A')}")
#                 st.write(product.get('description', 'No description available.'))
#                 st.markdown("---")
#         else:
#             st.info("No suitable products found based on your query and budget.")




import streamlit as st
from agents.coordinator_agent import CoordinatorAgent

# Simulated LLM-like shopping advisor (replace with real LLM call for full intelligence)
def shopping_chat_response(query):
    # Hardcoded sample rules for demo; you can expand or replace with an actual LLM API call
    q = query.lower()
    if "ram" in q and "gaming phone" in q:
        return "For a gaming phone, at least 8GB RAM is recommended for smooth performance."
    if "gift" in q and "teenager" in q:
        return "Some good gift ideas for a teenager include wireless earbuds, smartwatches, or trending fashion accessories."
    if "budget" in q:
        return "Set a reasonable budget for your needs, balancing brand value with features."
    return "I'm here to help with any shopping advice, product selection, or feature comparisons!"

st.set_page_config(page_title="AI Shopping Assistant", layout="centered")
coordinator = CoordinatorAgent()

# Session states for both tabs
if "product_history" not in st.session_state:
    st.session_state["product_history"] = []

if "chat_history" not in st.session_state:
    st.session_state["chat_history"] = []

tab1, tab2 = st.tabs(["Shopping Chat", "Product Finder"])

with tab1:
    st.header("🗨️ Chat with AI Shopping Assistant")
    for q, a in st.session_state["chat_history"]:
        st.markdown(f"**You:** {q}")
        st.markdown(f"**Assistant:** {a}")
    chat_input = st.text_input("Type your question for shopping advice", key="chat_input", placeholder="e.g. What RAM should a gaming phone have?")
    if st.button("Send Chat", key="send_chat_button"):
        if chat_input.strip():
            answer = shopping_chat_response(chat_input)
            st.session_state["chat_history"].append((chat_input, answer))
            st.rerun()


with tab2:
    st.header("😎 Find Products")
    # Display full conversation history, input at BOTTOM
    for idx, (q, products) in enumerate(st.session_state["product_history"]):
        st.markdown(f"**Query {idx+1}:** {q}")
        if products:
            for product in products:
                st.markdown(f"**{product['title']}** (${product['price']})")
                if product.get("thumbnail"):
                    st.image(product["thumbnail"], width=120)
                st.write(f"Rating: {product.get('rating', 'N/A')}")
                st.write(product.get('description', 'No description.'))
                st.markdown("---")
        else:
            st.info("No matching products found.")
    # Input AT THE BOTTOM
    with st.container():
        query_input = st.text_input("Enter product query or filter (products will update with each query):", key="product_input")
        if st.button("Send Product Query", key="send_product_button"):
            previous_products = st.session_state["product_history"][-1][1] if st.session_state["product_history"] else None
            filtered_products = coordinator.contextual_search(query_input, previous_products)
            st.session_state["product_history"].append((query_input, filtered_products))
            st.rerun()











# import streamlit as st
# from agents.coordinator_agent import CoordinatorAgent

# st.set_page_config(page_title="Multi-Agent Shopping Assistant", layout="centered")

# if "history" not in st.session_state:
#     st.session_state["history"] = []  # Stores tuples of (query, filtered_products)

# coordinator = CoordinatorAgent()

# st.title("Multi-Agent Shopping Assistant 🛒")

# user_query = st.text_input("Enter query or filter (e.g., 'laptops', 'dell laptops', 'under 30000'):")

# if st.button("Send Query") and user_query.strip():
#     previous_products = st.session_state["history"][-1][1] if st.session_state["history"] else None
#     filtered_products = coordinator.contextual_search(user_query, previous_products)
#     # Save query and results to history
#     st.session_state["history"].append((user_query, filtered_products))

# # Display the history/chat log
# for idx, (q, products) in enumerate(st.session_state["history"]):
#     st.markdown(f"**Query {idx+1}:** {q}")
#     if products:
#         for product in products:
#             st.markdown(f"**{product['title']}** (${product['price']})")
#             if product.get("thumbnail"):
#                 st.image(product["thumbnail"], width=120)
#             st.write(f"Rating: {product.get('rating', 'N/A')}")
#             st.write(product.get('description', 'No description.'))
#             st.markdown("---")
#     else:
#         st.info("No matching products found.")


