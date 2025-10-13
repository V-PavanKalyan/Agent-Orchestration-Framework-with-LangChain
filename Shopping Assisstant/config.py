import streamlit as st
from agents.coordinator_agent import CoordinatorAgent

st.set_page_config(page_title="Multi-Agent Shopping Assistant", page_icon="🛒", layout="centered")

# Color and style settings for good contrast
PRIMARY_COLOR = "#2a9d8f"
SECONDARY_COLOR = "#264653"
BACKGROUND_COLOR = "#f4f1de"
TEXT_COLOR = "#1a1a1a"

# Styling
st.markdown(
    f"""
    <style>
    .reportview-container {{
        background-color: {BACKGROUND_COLOR};
        color: {TEXT_COLOR};
    }}
    .stButton>button {{
        background-color: {PRIMARY_COLOR};
        color: white;
        font-weight: bold;
    }}
    .stTextInput>div>input {{
        border-radius: 5px;
        border: 2px solid {SECONDARY_COLOR};
        padding: 8px;
    }}
    </style>
    """,
    unsafe_allow_html=True,
)

st.title("Multi-Agent Shopping Assistant 🛒")

# Input fields for query and budget
query = st.text_input("Enter product or shopping query", max_chars=100)
budget = st.number_input("Enter your budget (optional)", min_value=0.0, format="%.2f")

if st.button("Search Products"):
    if not query.strip():
        st.warning("Please enter a valid product query to start.")
    else:
        # Initialize Coordinator Agent
        coordinator = CoordinatorAgent()

        with st.spinner("Searching products and analyzing prices, reviews..."):
            result = coordinator.search_and_recommend(query, budget)

        # Display final recommendations dynamically
        if result:
            st.subheader("Recommended Products:")
            for idx, product in enumerate(result):
                st.markdown(f"### {product['title']}")
                st.image(product['thumbnail'], width=200)
                st.write(f"Price: ${product['price']}")
                st.write(f"Rating: {product.get('rating', 'N/A')}")
                st.write(product.get('description', 'No description available.'))
                st.markdown("---")
        else:
            st.info("No suitable products found based on your query and budget.")

