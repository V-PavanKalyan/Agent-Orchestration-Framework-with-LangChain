import streamlit as st

# Set page config
st.set_page_config(
    page_title="Agent-Orchestration Framework with LangChain",
    page_icon="🤖",
    layout="wide"
)

# Custom CSS for styling (No dark mode)
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;900&display=swap');

    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
    }

    .stApp {
        background: linear-gradient(to right, #f0f4f8, #d9e2ec);
        color: #0F172A;
        padding: 2rem;
    }

    .stButton>button {
        border-radius: 0.5rem;
        border: 1px solid #E2E8F0;
        padding: 0.5rem 1rem;
        background-color: #F8FAFC;
        color: #0F172A;
        transition: all 0.3s;
    }

    .stButton>button:hover {
        border-color: #3B82F6;
        box-shadow: 0 5px 15px -3px rgba(59, 130, 246, 0.5);
        transform: translateY(-2px);
    }

    .card {
        border-radius: 0.5rem;
        border: 1px solid #E2E8F0;
        padding: 1rem;
        background-color: #ffffff;
        height: 350px;
        transition: all 0.3s;
        display: flex;
        flex-direction: column;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.05);
    }

    .card:hover {
        border-color: #3B82F6;
        box-shadow: 0 8px 24px rgba(59, 130, 246, 0.2);
        transform: translateY(-4px);
    }

    .card img {
        border-radius: 0.3rem;
        width: 100%;
        height: 220px;
        object-fit: cover;
        margin-bottom: 0.5rem;
    }

    .card h2 {
        font-size: 1.2rem;
        font-weight: 600;
        margin: 0.5rem 0;
        color: #1E293B;
    }

    .card p {
        font-size: 0.9rem;
        color: #475569;
        margin: 0.25rem 0;
    }
</style>
""", unsafe_allow_html=True)

# Title and description
st.markdown(
    """
    <div style="text-align: center; margin-bottom: 2rem;">
        <h1 style="font-size: 2.5rem; font-weight: 800; margin-bottom: 0.5rem; color: #1E293B;">
            Agent-Orchestration Framework with LangChain
        </h1>
        <p style="font-size: 1.1rem; color: #64748B; max-width: 600px; margin: 0 auto;">
            Click on one of the options below to explore the capabilities of our AI agents.
        </p>
    </div>
    """,
    unsafe_allow_html=True
)

# Card grid
col1, col2 = st.columns(2, gap="medium")
with col1:
    st.markdown(
        """
        <a href="https://medagentapp-cn5gdssn2dsvp9kbdhqehz.streamlit.app/" style="text-decoration: none;">
            <div class="card">
                <img src="https://lh3.googleusercontent.com/aida-public/AB6AXuBBimX72RLhD3zLD-W01HbAWEv0vid_ucMYvGviN8RVJUIAzZLKXvug8DaF9588wwrlRZSv0-Ze4zFiWHVL7gh_Wg2di63HPAXkCBoD82Y6iFOqxEfyRQFWwBglU3ZXqQ35eGwMGUXc72-ROgpoK0xlAwtO87NLYvRTtnef2XsawexT1zhGFXHBdwz6c9MqgtBzMzE0Cejtfv2_tRJDNqVE-d7FDZf396-_40URJrMQfJGNeLSsR-Yks8fheNoE6-JD2mbx4TN9QpKQ" alt="Abstract visualization of data points and connections">
                <h2>Medical AI Assistant</h2>
                <p>An AI-driven medical assistant that provides diagnostic support.</p>
            </div>
        </a>
        """,
        unsafe_allow_html=True
    )

with col2:
    st.markdown(
        """
        <a href="https://myselfshikhar-agent-orchestration-framework-with-la-main-qv9g04.streamlit.app/" style="text-decoration: none;">
            <div class="card">
                <img src="https://lh3.googleusercontent.com/aida-public/AB6AXuAsqFExH92QpEJLK_jhC9vWvhsxlKefowJdDHz6AIJHvGcl5DTMzkUJUN2y5d-S_sR8yPCgHpujSMaFdUsHmKhPTSIjMk7igwZzhBYAdOY04ozuB_N0cZUhc9gLxDHhpPvpXMzcVqAB6Q3x8NY-knWzM2CGWLmV1u2zsV56aoQ63Xg4WdPW2uRZN6rBARX7dpv9DwFVcUr403_HASVRKbF710heHabziBMT6o6jfyRC1H1Sv5LSh5vyAIWmJ9MFyVeqo67aWFyfogbu" alt="Futuristic robot arm interacting with a digital interface">
                <h2>Shopping Assistant</h2>
                <p>An AI-powered shopping assistant that helps users discover and buy products effortlessly.</p>
            </div>
        </a>
        """,
        unsafe_allow_html=True
    )
