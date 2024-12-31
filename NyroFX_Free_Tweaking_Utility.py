import streamlit as st
import subprocess
import os
import ctypes
import psutil
import time
import sys

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def run_as_admin():
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)

def run_command(command):
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        st.success(f"Command executed successfully: {command}")
        return result.stdout
    except subprocess.CalledProcessError as e:
        st.error(f"Error executing command: {e}")
        return None

if not is_admin():
    st.error("This application requires administrator privileges. Please run it as an administrator.")
    if st.button("Restart with Admin Rights"):
        run_as_admin()
    st.stop()

# Set page config
st.set_page_config(page_title="NyroFX Free Tweaking Utility", page_icon="🛠️", layout="wide")

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

# Sidebar
st.sidebar.title("About")
st.sidebar.info("NyroFX Free Tweaking Utility is designed to enhance your system's performance. This cloud version provides recommendations and simulations of tweaks.")

# Discord button with logo (unchanged)
discord_html = """
<div style="display: flex; align-items: center;">
    <img src="https://assets-global.website-files.com/6257adef93867e50d84d30e2/636e0a69f118df70ad7828d4_icon_clyde_blurple_RGB.svg" alt="Discord logo" style="width: 24px; height: 24px; margin-right: 10px;">
    <a href="https://discord.gg/4aT28zYy" target="_blank" style="background-color: #7289DA; color: white; text-decoration: none; padding: 10px 15px; border-radius: 5px; display: inline-block;">Join Discord Community</a>
</div>
"""
st.sidebar.markdown(discord_html, unsafe_allow_html=True)

# Main content
tab1, tab2, tab3, tab4, tab5 = st.tabs(["System Tweaks", "Gaming Tweaks", "Network Tweaks", "Cleanup", "Advanced Tweaks"])

with tab1:
    st.header("System Tweaks")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("System Restore")
        if st.button("Create System Restore Point"):
            #run_command("powershell.exe -Command Add-Computer -Credential (Get-Credential)") #Example of a command that requires admin rights
            st.info("In a local environment, this would create a system restore point.")
            st.success("Restore point creation simulated successfully.")
    
    with col2:
        st.subheader("Visual Effects")
        if st.button("Optimize Visual Effects"):
            run_command('reg add "HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Explorer\\VisualEffects" /v VisualFXSetting /t REG_DWORD /d 2 /f')
            run_command('rundll32.exe advapi32.dll,ProcessIdleTasks')
            st.success("Visual effects optimized for performance.")
    
    st.subheader("System Services")
    col3, col4, col5 = st.columns(3)
    
    with col3:
        prefetch_state = st.radio("Prefetch", ("Enable", "Disable"), key="prefetch")
        if st.button("Apply Prefetch Setting"):
            st.info(f"In a local environment, this would {prefetch_state.lower()} Prefetch.")
            st.success(f"Prefetch {prefetch_state.lower()} simulation successful.")
    
    with col4:
        windows_update_state = st.radio("Windows Update", ("Enable", "Disable"), key="windows_update")
        if st.button("Apply Windows Update Setting"):
            st.info(f"In a local environment, this would {windows_update_state.lower()} Windows Update.")
            st.success(f"Windows Update {windows_update_state.lower()} simulation successful.")
    
    with col5:
        superfetch_state = st.radio("Superfetch", ("Enable", "Disable"), key="superfetch")
        if st.button("Apply Superfetch Setting"):
            st.info(f"In a local environment, this would {superfetch_state.lower()} Superfetch.")
            st.success(f"Superfetch {superfetch_state.lower()} simulation successful.")
    
    st.subheader("Power Management")
    power_plans = ["Balanced", "High performance", "Power saver", "Ultimate Performance"]
    selected_plan = st.selectbox("Select Power Plan", power_plans, index=1)
    st.write("💡 High performance or Ultimate Performance is recommended for optimal system performance.")
    if st.button("Apply Power Plan"):
        st.info(f"In a local environment, this would apply the {selected_plan} power plan.")
        st.success(f"{selected_plan} power plan simulation applied successfully.")

with tab2:
    st.header("Gaming Tweaks")
    
    st.subheader("Game DVR")
    game_dvr_state = st.radio("Game DVR", ("Enable", "Disable"), key="game_dvr")
    st.warning("Disabling Game DVR may affect Xbox services and game recording capabilities.")
    if st.button("Apply Game DVR Setting"):
        st.info(f"In a local environment, this would {game_dvr_state.lower()} Game DVR.")
        st.success(f"Game DVR {game_dvr_state.lower()} simulation successful.")
    
    st.subheader("Game Priority")
    game = st.selectbox("Select a game to prioritize", ["Fortnite", "Call of Duty", "FiveM", "Valorant"])
    if st.button("Set Game Priority"):
        st.info(f"In a local environment, this would set high priority for {game}.")
        st.success(f"Priority simulation set for {game}")
    
    st.subheader("GPU Optimization")
    gpu_type = st.radio("Select GPU Type", ["NVIDIA", "AMD"], key="gpu_type")
    if st.button("Optimize GPU"):
        st.info(f"In a local environment, this would optimize {gpu_type} GPU settings.")
        st.success(f"{gpu_type} GPU optimization simulation successful.")

with tab3:
    st.header("Network Tweaks")
    
    if st.button("Optimize Network Settings"):
        st.info("In a local environment, this would optimize various network settings.")
        st.success("Network optimization simulation successful.")
    
    if st.button("Clear DNS Cache"):
        st.info("In a local environment, this would clear the DNS cache.")
        st.success("DNS cache clear simulation successful.")

with tab4:
    st.header("System Cleanup")
    
    if st.button("Clean Temporary Files"):
        st.info("In a local environment, this would clean temporary files from various locations.")
        st.success("Temporary files cleanup simulation successful.")

with tab5:
    st.header("Advanced Tweaks")
    
    st.subheader("RAM Optimization")
    if st.button("Optimize RAM"):
        st.info("In a local environment, this would optimize RAM usage settings.")
        st.success("RAM optimization simulation successful.")
    
    st.subheader("System Information")
    show_info = st.button("Show System Info")
    stop_info = st.empty()

    if show_info:
        placeholder = st.empty()
        stop_button = stop_info.button("Stop Showing System Info")
        
        while show_info:
            cpu_usage = psutil.cpu_percent(interval=1)
            memory = psutil.virtual_memory()
            disk = psutil.disk_usage('/')
            
            placeholder.write(f"""
            CPU Usage: {cpu_usage}%
            Memory Usage: {memory.percent}%
            Disk Usage: {disk.percent}%
            """)
            
            time.sleep(1)
            
            if stop_button:
                break

        placeholder.empty()
        stop_info.empty()

st.info("Note: This is a cloud version of the utility. It simulates tweaks and provides recommendations. To apply actual changes, please run the desktop version with administrator privileges.")

