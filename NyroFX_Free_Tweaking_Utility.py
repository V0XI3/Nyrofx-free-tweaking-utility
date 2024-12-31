import streamlit as st
import platform
import psutil
import time

# Set page config first
st.set_page_config(page_title="NyroFX Free Tweaking Utility", page_icon="🛠️", layout="wide")

def is_streamlit_cloud():
    return 'STREAMLIT_SHARING_MODE' in st.secrets

# Rest of the imports and function definitions...

# Custom CSS (unchanged)
st.markdown("""
    <style>
    body {
        color: #262730;
    }
    .logo-title-container {
        display: flex;
        align-items: center;
        gap: 20px;
        background-color: rgba(255, 255, 255, 0.1);
        padding: 10px;
        border-radius: 15px;
        margin-bottom: 20px;
    }
    .logo-image {
        width: 50px;
        height: 50px;
        border-radius: 12px;
    }
    .app-title {
        font-size: 36px;
        font-weight: bold;
        color: #FF5733;
    }
    .stButton > button {
        border-radius: 10px;
    }
    .stTextInput > div > div > input {
        border-radius: 10px;
    }
    .stSelectbox > div > div > select {
        border-radius: 10px;
    }
    .custom-warning {
        background-color: rgba(255, 87, 51, 0.7);
        color: white;
        padding: 10px;
        border-radius: 5px;
        margin-bottom: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

# Logo and Title
st.markdown("""
    <div class="logo-title-container">
        <img src="https://hebbkx1anhila5yf.public.blob.vercel-storage.com/nyrofx_logo-SA3FeqpXgFettobgQ9vxRXLQaQflGs.gif" class="logo-image">
        <span class="app-title">NyroFX Free Tweaking Utility</span>
    </div>
""", unsafe_allow_html=True)

st.write("Optimize your system performance with ease")

if is_streamlit_cloud():
    st.warning("You are currently viewing this application on Streamlit Cloud. To use all features and make system changes, please run this application locally on your Windows machine.")
    
    st.subheader("Instructions for Local Use:")
    st.markdown("""
    1. Ensure you have Python installed on your Windows machine.
    2. Install Streamlit and other required packages:

