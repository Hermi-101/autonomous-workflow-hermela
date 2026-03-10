
import pyautogui
import time
import webbrowser
import os

# Generated Agent for Workflow: WF-313
# Employee: EMP-0025
# Pattern: brave.exe:Custom_CLICK->brave.exe:Custom_CLICK->brave.exe:TYPE->brave.exe:TYPE->Telegram.exe:CLICK


def run_agent():
    print(f"--- Start Generated Agent for WF-313 ---")
    pyautogui.PAUSE = 1.0

    steps = [
        {
                "id_employee": "EMP-0025",
                "timestamp": "2026-02-24 12:36:35.363176+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Natnael_EMP-0025/screenshot/Feb24/44d56485-7152-4f3d-8c77-195678d6e319.webp",
                "app_name": "brave.exe",
                "window_title": "Fix of warehouse - Google Sheets - Brave",
                "event": "Custom_CLICK",
                "url": "docs.google.com/spreadsheets/d/1UByYg7_GMjNIqjoXEcNezc2bNfnSVuOU8japFLXceUU/edit?gid=895107596#gid=895107596",
                "date": "2026-02-24"
        },
        {
                "id_employee": "EMP-0025",
                "timestamp": "2026-02-24 12:36:51.224757+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Natnael_EMP-0025/screenshot/Feb24/41c079c8-3dfb-44ad-9e38-542d45959ccb.webp",
                "app_name": "brave.exe",
                "window_title": "Fix of warehouse - Google Sheets - Brave",
                "event": "Custom_CLICK",
                "url": "docs.google.com/spreadsheets/d/1UByYg7_GMjNIqjoXEcNezc2bNfnSVuOU8japFLXceUU/edit?gid=895107596#gid=895107596",
                "date": "2026-02-24"
        },
        {
                "id_employee": "EMP-0025",
                "timestamp": "2026-02-24 12:37:15.010000+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Natnael_EMP-0025/screenshot/Feb24/640be744-27da-4a40-9e79-5cb0a60a2588.webp",
                "app_name": "brave.exe",
                "window_title": "Fix of warehouse - Google Sheets - Brave",
                "event": "TYPE",
                "url": "docs.google.com/spreadsheets/d/1UByYg7_GMjNIqjoXEcNezc2bNfnSVuOU8japFLXceUU/edit?gid=895107596#gid=895107596",
                "date": "2026-02-24"
        },
        {
                "id_employee": "EMP-0025",
                "timestamp": "2026-02-24 12:37:20.010000+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Natnael_EMP-0025/screenshot/Feb24/024ca6c4-9c58-4533-9f46-e0de25074bf6.webp",
                "app_name": "brave.exe",
                "window_title": "Fix of warehouse - Google Sheets - Brave",
                "event": "TYPE",
                "url": "docs.google.com/spreadsheets/d/1UByYg7_GMjNIqjoXEcNezc2bNfnSVuOU8japFLXceUU/edit?gid=895107596#gid=895107596",
                "date": "2026-02-24"
        },
        {
                "id_employee": "EMP-0025",
                "timestamp": "2026-02-24 12:37:25.001000+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Natnael_EMP-0025/screenshot/Feb24/018e0539-fd28-4955-9b0a-08d242835ef0.webp",
                "app_name": "Telegram.exe",
                "window_title": "\u200eOperations Leads @ \u200eNA (6948)",
                "event": "CLICK",
                "url": "",
                "date": "2026-02-24"
        }
]
    
    for i, step in enumerate(steps):
        print(f"Step {i+1}: {step['event']} in {step['app_name']}")
        
        # 1. Navigation Logic
        if step['url'] and str(step['url']) != 'None':
            print(f"  > Opening URL: {step['url']}")
            webbrowser.open(step['url'])
            time.sleep(4) # Wait for page load
            
        # 2. Click Logic
        if 'CLICK' in step['event'].upper():
            # In a production environment, we would use:
            # pos = pyautogui.locateOnScreen(step['image_path'])
            # pyautogui.click(pos)
            print(f"  > [Simulated] Clicking based on image: {step['image_path']}")
            
        # 3. Typing Logic
        if 'TYPE' in step['event'].upper():
            print(f"  > Typing automated sequence...")
            pyautogui.write("Generated Input", interval=0.1)
            
        time.sleep(1)

    print("--- Workflow Execution Complete ---")

if __name__ == "__main__":
    run_agent() 



