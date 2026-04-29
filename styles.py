import streamlit as st


def apply_styles():
    st.markdown("""
    <style>
    /* 1. Global Background: Digital Lavender */
    .stApp {
        background-color: #E6E6FA !important;
    }

    /* 2. Top Navigation Bar (Full Width) */
    .custom-nav {
        background-color: #4B0082;
        padding: 15px 40px;
        display: flex;
        justify-content: space-between;
        align-items: center;
        color: white;
        position: fixed;
        top: 0;
        left: 0;
        right: 0;
        z-index: 999;
        box-shadow: 0 4px 10px rgba(0,0,0,0.2);
    }

    /* 3. High Contrast Text: Jet Black */
    .stMarkdown p, .stChatMessage p, label, .stChatInputContainer textarea {
        color: #000000 !important;
        font-weight: 500 !important;
        font-size: 1.1rem !important;
    }

    /* 4. Chat Bubbles (Soft White) */
    [data-testid="stChatMessage"] {
        background-color: rgba(255, 255, 255, 0.9) !important;
        border-radius: 20px !important;
        border: none !important;
        margin-bottom: 15px;
    }

    /* 5. Custom Sidebar/Right-Side Nav Buttons */
    div.stButton > button {
        background-color: #4B0082 !important;
        color: white !important;
        border: 1px solid #9370DB !important;
        border-radius: 12px !important;
        font-weight: bold !important;
        transition: 0.3s;
    }

    div.stButton > button:hover {
        background-color: #6A5ACD !important;
        border-color: white !important;
    }

    /* 6. Professional Chat Input */
    .stChatInputContainer {
        border-radius: 35px !important;
        background-color: white !important;
        border: 2px solid #4B0082 !important;
    }

    /* Offset main content so it doesn't hide under the fixed navbar */
    .main-content {
        padding-top: 80px;
    }
    </style>
    """, unsafe_allow_html=True)