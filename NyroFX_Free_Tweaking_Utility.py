import streamlit as st
import subprocess
import os
import sys
import platform
import psutil
import time

# Set page config first
st.set_page_config(page_title="NyroFX Free Tweaking Utility", page_icon="🛠️", layout="wide")

def is_windows():
    return platform.system() == 'Windows'

def is_admin():
    if is_windows():
        try:
            import ctypes
            return ctypes.windll.shell32.IsUserAnAdmin()
        except:
            return False
    return False

def run_as_admin():
    if is_windows():
        try:
            import ctypes
            ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
        except Exception as e:
            st.error(f"Error while trying to run as admin: {e}")
    else:
        st.error("Elevating privileges is not supported on this platform.")

def run_command(command):
    if is_windows():
        try:
            result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
            st.success(f"Command executed successfully: {command}")
            return result.stdout
        except subprocess.CalledProcessError as e:
            st.error(f"Error executing command: {e}")
            return None
    else:
        st.warning(f"Command simulation: {command}")
        return "Command simulated successfully"

# Custom CSS
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

# Check for Windows and admin rights
if not is_windows():
    st.warning("This application is designed for Windows. Some features may not work on this platform.")
elif not is_admin():
    st.warning("This application works best with administrator privileges.")
    if st.button("Attempt to Restart with Admin Rights"):
        run_as_admin()
    st.info("Continuing with limited functionality. Some features may not work as expected.")
else:
    st.success("Running on Windows with administrator privileges.")

# Sidebar
st.sidebar.title("About")
st.sidebar.info("NyroFX Free Tweaking Utility is designed to enhance your Windows system's performance. Use with caution and always create a restore point before making changes.")

# Discord button
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
            if is_windows():
                run_command('powershell.exe -Command "Checkpoint-Computer -Description \'NyroFX Optimizer Restore Point\' -RestorePointType \'MODIFY_SETTINGS\'"')
                st.success("Restore point created successfully.")
            else:
                st.info("System Restore Point creation simulated (non-Windows environment).")
    
    with col2:
        st.subheader("Visual Effects")
        if st.button("Optimize Visual Effects"):
            if is_windows():
                run_command('reg add "HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Explorer\\VisualEffects" /v VisualFXSetting /t REG_DWORD /d 2 /f')
                run_command('rundll32.exe advapi32.dll,ProcessIdleTasks')
                st.success("Visual effects optimized for performance.")
            else:
                st.info("Visual effects optimization simulated (non-Windows environment).")
    
    st.subheader("System Services")
    col3, col4, col5 = st.columns(3)
    
    with col3:
        prefetch_state = st.radio("Prefetch", ("Enable", "Disable"), key="prefetch")
        if st.button("Apply Prefetch Setting"):
            if is_windows():
                value = 0 if prefetch_state == "Disable" else 1
                run_command(f'reg add "HKLM\\SYSTEM\\CurrentControlSet\\Control\\Session Manager\\Memory Management\\PrefetchParameters" /v EnablePrefetcher /t REG_DWORD /d {value} /f')
                st.success(f"Prefetch {prefetch_state.lower()}d successfully.")
            else:
                st.info(f"Prefetch {prefetch_state.lower()} simulated (non-Windows environment).")
    
    with col4:
        windows_update_state = st.radio("Windows Update", ("Enable", "Disable"), key="windows_update")
        if st.button("Apply Windows Update Setting"):
            if is_windows():
                if windows_update_state == "Disable":
                    run_command('sc stop wuauserv')
                    run_command('sc config wuauserv start= disabled')
                    st.success("Windows Update service stopped and disabled.")
                else:
                    run_command('sc config wuauserv start= auto')
                    run_command('sc start wuauserv')
                    st.success("Windows Update service enabled and started.")
            else:
                st.info(f"Windows Update {windows_update_state.lower()} simulated (non-Windows environment).")
    
    with col5:
        superfetch_state = st.radio("Superfetch", ("Enable", "Disable"), key="superfetch")
        if st.button("Apply Superfetch Setting"):
            if is_windows():
                if superfetch_state == "Disable":
                    run_command('sc stop SysMain')
                    run_command('sc config SysMain start= disabled')
                    st.success("Superfetch (SysMain) disabled.")
                else:
                    run_command('sc config SysMain start= auto')
                    run_command('sc start SysMain')
                    st.success("Superfetch (SysMain) enabled and started.")
            else:
                st.info(f"Superfetch {superfetch_state.lower()} simulated (non-Windows environment).")
    
    st.subheader("Power Management")
    power_plans = {
        "Balanced": "381b4222-f694-41f0-9685-ff5bb260df2e",
        "High performance": "8c5e7fda-e8bf-4a96-9a85-a6e23a8c635c",
        "Power saver": "a1841308-3541-4fab-bc81-f71556f20b4a",
        "Ultimate Performance": "e9a42b02-d5df-448d-aa00-03f14749eb61"
    }
    selected_plan = st.selectbox("Select Power Plan", list(power_plans.keys()), index=1)
    st.write("💡 High performance or Ultimate Performance is recommended for optimal system performance.")
    if st.button("Apply Power Plan"):
        if is_windows():
            if selected_plan == "Ultimate Performance":
                run_command('powercfg -duplicatescheme e9a42b02-d5df-448d-aa00-03f14749eb61')
            run_command(f'powercfg /setactive {power_plans[selected_plan]}')
            st.success(f"{selected_plan} power plan applied successfully.")
        else:
            st.info(f"{selected_plan} power plan application simulated (non-Windows environment).")

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
        if is_windows():
            run_command('reg add "HKLM\\SYSTEM\\CurrentControlSet\\Control" /v "SvcHostSplitThresholdInKB" /t REG_DWORD /d "68764420" /f')
            st.success("RAM optimized successfully.")
        else:
            st.info("RAM optimization simulated (non-Windows environment).")
    
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

if not is_windows():
    st.info("Note: This is a simulation of the NyroFX Free Tweaking Utility. For full functionality, please run on a Windows system with administrator privileges.")

