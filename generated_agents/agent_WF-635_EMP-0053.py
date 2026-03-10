
import pyautogui
import time
import webbrowser
import os

# Generated Agent for Workflow: WF-635
# Employee: EMP-0053
# Pattern: chrome.exe:Custom_CLICK->chrome.exe:Custom_CLICK->chrome.exe:Custom_CLICK->chrome.exe:APP_SWITCH->chrome.exe:Custom_CLICK


def run_agent():
    print(f"--- Start Generated Agent for WF-635 ---")
    pyautogui.PAUSE = 1.0

    steps = [
        {
                "id_employee": "EMP-0053",
                "timestamp": "2026-02-23 09:54:47.821248+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Betelhem_EMP-0053/screenshot/Feb23/dce405d5-8848-4b19-81a8-412239a61d0c.webp",
                "app_name": "chrome.exe",
                "window_title": "Reports - Google Chrome",
                "event": "Custom_CLICK",
                "url": "admin.ringcloud.et/reports",
                "date": "2026-02-23"
        },
        {
                "id_employee": "EMP-0053",
                "timestamp": "2026-02-23 09:54:50.258373+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Betelhem_EMP-0053/screenshot/Feb23/a6b1b8bf-b0ee-4733-b490-018b6d3fa3d0.webp",
                "app_name": "chrome.exe",
                "window_title": "Reports - Google Chrome",
                "event": "Custom_CLICK",
                "url": "admin.ringcloud.et/reports",
                "date": "2026-02-23"
        },
        {
                "id_employee": "EMP-0053",
                "timestamp": "2026-02-23 09:55:10.603203+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Betelhem_EMP-0053/screenshot/Feb23/7bc4ef2c-8c72-42b6-baf2-8925ad72b704.webp",
                "app_name": "chrome.exe",
                "window_title": "Reports - Google Chrome",
                "event": "Custom_CLICK",
                "url": "docs.google.com/spreadsheets/d/1NuQdUH0ju6WDWrxeut6Thge8oLQ-JP4mJlHU32YO92Q/edit?gid=1993363355#gid=1993363355",
                "date": "2026-02-23"
        },
        {
                "id_employee": "EMP-0053",
                "timestamp": "2026-02-23 09:55:11.375000+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Betelhem_EMP-0053/screenshot/Feb23/79ea38aa-10dc-4e09-ba54-68cba64ce1e0.webp",
                "app_name": "chrome.exe",
                "window_title": "Call center KPI Report - Google Sheets - Google Chrome",
                "event": "APP_SWITCH",
                "url": "docs.google.com/spreadsheets/d/1NuQdUH0ju6WDWrxeut6Thge8oLQ-JP4mJlHU32YO92Q/edit?gid=1993363355#gid=1993363355",
                "date": "2026-02-23"
        },
        {
                "id_employee": "EMP-0053",
                "timestamp": "2026-02-23 09:57:37.852547+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Betelhem_EMP-0053/screenshot/Feb23/511cd993-697c-446b-bd18-4d0bf5105df2.webp",
                "app_name": "chrome.exe",
                "window_title": "Call center KPI Report - Google Sheets - Google Chrome",
                "event": "Custom_CLICK",
                "url": "",
                "date": "2026-02-23"
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



