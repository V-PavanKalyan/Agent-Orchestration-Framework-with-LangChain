# Multi-Agent Shopping Assistant 🛍️

A Streamlit-based AI shopping assistant that uses a team of specialized agents to help you find ideal products, get tailored advice, and interactively filter results through a natural, conversational interface.


---

## 📋 Table of Contents

- [Key Features](#-key-features)
- [How It Works: The Agentic Approach](#-how-it-works-the-agentic-approach)
- [Tech Stack](#-tech-stack)
- [Getting Started](#-getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation & Setup](#installation--setup)
  - [Running the Application](#running-the-application)
- [How to Use](#-how-to-use)
  - [Shopping Chat Mode](#shopping-chat-mode-)
  - [Product Finder Mode](#product-finder-mode-)
- [Customization & Future Scope](#-customization--future-scope)

---

## ✨ Key Features

* **🤖 Conversational Shopping Assistant**: Get expert shopping guidance in a dedicated chat tab. Ask anything from "What's the best RAM for a gaming phone?" to "Suggest a gift for a teenager." Powered by a simple rule-based system or extensible with LLMs like **Gemini** or **OpenAI GPT**.
* **🔎 Interactive Product Finder**: Start with a broad query like "laptops" and narrow it down step-by-step with natural language commands like "Only Dell please," "under 40000," or "with 16GB RAM."
* **🧠 Smart Context & Memory**: The Product Finder is memory-aware. Each new constraint refines the *previous* search, creating a seamless and intuitive filtering experience, just like a real shopping dialogue.
* **✨ Modern & Responsive UI**: A clean, tabbed interface built with Streamlit, featuring a bottom-aligned input for a natural chat feel and a contrast-rich design for easy viewing.
* **🔌 Pluggable Architecture**: The system is powered by the **Fake Store API** for demonstration but is designed to easily connect to any real product database or e-commerce API.

---

## 🧠 How It Works: The Agentic Approach

This isn't just a simple chatbot. The application uses a multi-agent system where different Python agents collaborate to fulfill your request.

1.  **Coordinator Agent**: The "team lead." It receives your raw query and decides which specialist agent(s) to call.
2.  **Search Agent**: Handles initial product searches based on keywords (e.g., "smartphones," "men's clothing").
3.  **Price Agent**: Extracts and applies price or budget constraints from your query (e.g., "under 20000," "between 500 and 1000").
4.  **Review Agent**: Assesses and filters products based on ratings or review-related queries.
5.  **Memory**: A simple but effective memory system ensures that context is carried over between messages in the Product Finder.

This modular design makes the system easy to extend and maintain.

---

## 🛠️ Tech Stack

* **Frontend**: Streamlit
* **Backend/Logic**: Python 3.8+
* **API Communication**: `requests` library
* **AI Chat (Optional)**: Google Gemini or OpenAI GPT APIs
* **Product Data**: Fake Store API (by default)

---

## 🚀 Getting Started

Follow these steps to get the Multi-Agent Shopping Assistant running on your local machine.

### Prerequisites

* Python 3.8 or newer
* `pip` (Python package installer)

### Installation & Setup

1.  **Clone the Repository**
    ```bash
    git clone https://github.com/your-username/multi-agent-shopping-assistant.git
    cd multi-agent-shopping-assistant
    ```

2.  **Verify Project Structure**
    Ensure all files are in the correct place as provided:
    ```
    .
    ├── main.py
    ├── agents/
    │   ├── __init__.py
    │   ├── coordinator_agent.py
    │   ├── search_agent.py
    │   ├── price_agent.py
    │   └── review_agent.py
    ├── memory.py
    ├── models.py
    ├── utils.py
    └── config.py
    ```

3.  **Install Required Packages**
    ```bash
    pip install streamlit requests
    ```

4.  **(Optional) Install LLM SDKs**
    If you want to enable advanced AI chat, install your preferred library:
    ```bash
    # For OpenAI
    pip install openai

    # For Google Gemini
    pip install google-generativeai
    ```

5.  **(Optional) Configure API Keys**
    For LLM integration, add your API key to your environment variables or directly in the `config.py` file. It's recommended to use an environment variable for security.

### Running the Application

Once the setup is complete, launch the app with a single command:
```bash
streamlit run main.py
