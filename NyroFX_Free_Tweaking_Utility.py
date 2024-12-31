import streamlit as st
import subprocess
import os
import ctypes
import psutil
import time
import base64

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

if not is_admin():
    st.error("This application requires administrator privileges. Please run it as an administrator.")
    st.stop()

def run_command(command):
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        st.error(f"Error executing command: {e}")
        return None

# Set page config
st.set_page_config(page_title="NyroFX Free Tweaking Utility", page_icon="🛠️", layout="wide")

# Custom CSS to style the logo and title
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
    color: #FF5733; /* A bright orange color that should be visible on both light and dark backgrounds */
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
        <img src="data:image/gif;base64,{}" class="logo-image">
        <span class="app-title">NyroFX Free Tweaking Utility</span>
    </div>
""".format(base64.b64encode(open("nyrofx_logo.gif", "rb").read()).decode()), unsafe_allow_html=True)

st.write("Optimize your system performance with ease")

# Sidebar
st.sidebar.title("About")
st.sidebar.info("NyroFX Free Tweaking Utility is designed to enhance your system's performance. Use with caution and always create a restore point before making changes.")

# Discord button with logo
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
            run_command('powershell.exe -Command "Checkpoint-Computer -Description \'NyroFX Optimizer Restore Point\' -RestorePointType \'MODIFY_SETTINGS\'"')
            st.success("Restore point created successfully.")
    
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
            value = 0 if prefetch_state == "Disable" else 1
            run_command(f'reg add "HKLM\\SYSTEM\\CurrentControlSet\\Control\\Session Manager\\Memory Management\\PrefetchParameters" /v EnablePrefetcher /t REG_DWORD /d {value} /f')
            st.success(f"Prefetch {prefetch_state.lower()}d successfully.")
    
    with col4:
        windows_update_state = st.radio("Windows Update", ("Enable", "Disable"), key="windows_update")
        if st.button("Apply Windows Update Setting"):
            if windows_update_state == "Disable":
                run_command('sc stop wuauserv')
                run_command('sc config wuauserv start= disabled')
                st.success("Windows Update service stopped and disabled.")
            else:
                run_command('sc config wuauserv start= auto')
                run_command('sc start wuauserv')
                st.success("Windows Update service enabled and started.")
    
    with col5:
        superfetch_state = st.radio("Superfetch", ("Enable", "Disable"), key="superfetch")
        if st.button("Apply Superfetch Setting"):
            if superfetch_state == "Disable":
                run_command('sc stop SysMain')
                run_command('sc config SysMain start= disabled')
                st.success("Superfetch (SysMain) disabled.")
            else:
                run_command('sc config SysMain start= auto')
                run_command('sc start SysMain')
                st.success("Superfetch (SysMain) enabled and started.")
    
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
        if selected_plan == "Ultimate Performance":
            run_command('powercfg -duplicatescheme e9a42b02-d5df-448d-aa00-03f14749eb61')
        run_command(f'powercfg /setactive {power_plans[selected_plan]}')
        st.success(f"{selected_plan} power plan applied successfully.")

with tab2:
    st.header("Gaming Tweaks")
    
    st.subheader("Game DVR")
    game_dvr_state = st.radio("Game DVR", ("Enable", "Disable"), key="game_dvr")
    st.warning("Disabling Game DVR may affect Xbox services and game recording capabilities.")
    if st.button("Apply Game DVR Setting"):
        value = 0 if game_dvr_state == "Disable" else 1
        run_command(f'reg add "HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\GameDVR" /v AllowGameDVR /t REG_DWORD /d {value} /f')
        run_command(f'reg add "HKCU\\System\\GameConfigStore" /v GameDVR_Enabled /t REG_DWORD /d {value} /f')
        st.success(f"Game DVR {game_dvr_state.lower()}d successfully.")
    
    st.subheader("Game Priority")
    game = st.selectbox("Select a game to prioritize", ["Fortnite", "Call of Duty", "FiveM", "Valorant"])
    if st.button("Set Game Priority"):
        run_command(f'wmic process where name="{game}.exe" CALL setpriority "high priority"')
        st.success(f"Priority set for {game}")
    
    st.subheader("GPU Optimization")
    gpu_type = st.radio("Select GPU Type", ["NVIDIA", "AMD"], key="gpu_type")
    if st.button("Optimize GPU"):
        if gpu_type == "NVIDIA":
            run_command('reg add "HKLM\\SYSTEM\\CurrentControlSet\\Control\\Class\\{4d36e968-e325-11ce-bfc1-08002be10318}\\0000" /v "PerfLevelSrc" /t REG_DWORD /d "2222" /f')
            run_command('reg add "HKLM\\SYSTEM\\CurrentControlSet\\Control\\Class\\{4d36e968-e325-11ce-bfc1-08002be10318}\\0000" /v "PowerMizerEnable" /t REG_DWORD /d "1" /f')
            run_command('reg add "HKLM\\SYSTEM\\CurrentControlSet\\Control\\Class\\{4d36e968-e325-11ce-bfc1-08002be10318}\\0000" /v "PowerMizerLevel" /t REG_DWORD /d "1" /f')
            run_command('reg add "HKLM\\SYSTEM\\CurrentControlSet\\Control\\Class\\{4d36e968-e325-11ce-bfc1-08002be10318}\\0000" /v "PowerMizerLevelAC" /t REG_DWORD /d "1" /f')
        elif gpu_type == "AMD":
            run_command('reg add "HKLM\\SYSTEM\\CurrentControlSet\\Control\\Class\\{4d36e968-e325-11ce-bfc1-08002be10318}\\0000" /v "KMD_EnableComputePreemption" /t REG_DWORD /d "0" /f')
            run_command('reg add "HKLM\\SYSTEM\\CurrentControlSet\\Control\\Class\\{4d36e968-e325-11ce-bfc1-08002be10318}\\0000" /v "DisableDrmdmaPowerGating" /t REG_DWORD /d "1" /f')
        st.success(f"{gpu_type} GPU optimized successfully.")

with tab3:
    st.header("Network Tweaks")
    
    if st.button("Optimize Network Settings"):
        run_command('netsh int tcp set global autotuninglevel=disabled')
        run_command('netsh int tcp set global chimney=disabled')
        run_command('netsh int tcp set global rss=disabled')
        run_command('netsh int tcp set global timestamps=disabled')
        run_command('ipconfig /flushdns')
        st.success("Network optimized successfully.")
    
    if st.button("Clear DNS Cache"):
        result = run_command('ipconfig /flushdns')
        if result:
            st.success("DNS cache cleared successfully.")
        else:
            st.error("Failed to clear DNS cache. Please try running the utility as administrator.")

with tab4:
    st.header("System Cleanup")
    
    if st.button("Clean Temporary Files"):
        temp_folders = [os.environ['TEMP'], r'C:\Windows\Temp']
        files_removed = 0
        for folder in temp_folders:
            for root, dirs, files in os.walk(folder):
                for file in files:
                    try:
                        file_path = os.path.join(root, file)
                        if os.path.isfile(file_path):
                            os.unlink(file_path)
                            files_removed += 1
                    except Exception as e:
                        st.warning(f"Could not remove {file_path}: {e}")
        st.success(f"Temporary files cleaned successfully. {files_removed} files removed.")

with tab5:
    st.header("Advanced Tweaks")
    
    st.subheader("RAM Optimization")
    if st.button("Optimize RAM"):
        run_command('reg add "HKLM\\SYSTEM\\CurrentControlSet\\Control" /v "SvcHostSplitThresholdInKB" /t REG_DWORD /d "68764420" /f')
        st.success("RAM optimized successfully.")
    
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

