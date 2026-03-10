
import pyautogui
import time
import webbrowser
import os

# Generated Agent for Workflow: WF-628
# Employee: EMP-0053
# Pattern: chrome.exe:Custom_CLICK->chrome.exe:Custom_CLICK->chrome.exe:CLICK->chrome.exe:Custom_CLICK->chrome.exe:TYPE


def run_agent():
    print(f"--- Start Generated Agent for WF-628 ---")
    pyautogui.PAUSE = 1.0

    steps = [
        {
                "id_employee": "EMP-0053",
                "timestamp": "2026-02-23 09:40:13.182774+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Betelhem_EMP-0053/screenshot/Feb23/d0bc87e9-7784-4991-916a-e24f6448e311.webp",
                "app_name": "chrome.exe",
                "window_title": "Call center KPI Report - Google Sheets - Google Chrome",
                "event": "Custom_CLICK",
                "url": "docs.google.com/spreadsheets/d/1NuQdUH0ju6WDWrxeut6Thge8oLQ-JP4mJlHU32YO92Q/edit?gid=523742192#gid=523742192",
                "date": "2026-02-23"
        },
        {
                "id_employee": "EMP-0053",
                "timestamp": "2026-02-23 09:41:05.454328+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Betelhem_EMP-0053/screenshot/Feb23/ef9a8cc7-3efa-49c6-90f2-25672e83106c.webp",
                "app_name": "chrome.exe",
                "window_title": "Call center KPI Report - Google Sheets - Google Chrome",
                "event": "Custom_CLICK",
                "url": "docs.google.com/spreadsheets/d/1NuQdUH0ju6WDWrxeut6Thge8oLQ-JP4mJlHU32YO92Q/edit?gid=1993363355#gid=1993363355",
                "date": "2026-02-23"
        },
        {
                "id_employee": "EMP-0053",
                "timestamp": "2026-02-23 09:43:10.014000+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Betelhem_EMP-0053/screenshot/Feb23/98b0a7ec-5610-4659-9d8b-094d6efadd8e.webp",
                "app_name": "chrome.exe",
                "window_title": "Call center KPI Report - Google Sheets - Google Chrome",
                "event": "CLICK",
                "url": "docs.google.com/spreadsheets/d/1NuQdUH0ju6WDWrxeut6Thge8oLQ-JP4mJlHU32YO92Q/edit?gid=1993363355#gid=1993363355",
                "date": "2026-02-23"
        },
        {
                "id_employee": "EMP-0053",
                "timestamp": "2026-02-23 09:43:14.014484+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Betelhem_EMP-0053/screenshot/Feb23/4538d289-249a-4d7d-8c7d-0cc3bfe30098.webp",
                "app_name": "chrome.exe",
                "window_title": "Call center KPI Report - Google Sheets - Google Chrome",
                "event": "Custom_CLICK",
                "url": "docs.google.com/spreadsheets/d/1NuQdUH0ju6WDWrxeut6Thge8oLQ-JP4mJlHU32YO92Q/edit?gid=1993363355#gid=1993363355",
                "date": "2026-02-23"
        },
        {
                "id_employee": "EMP-0053",
                "timestamp": "2026-02-23 09:43:25.012000+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Betelhem_EMP-0053/screenshot/Feb23/c46f2663-ef30-4816-9b36-9710488c2576.webp",
                "app_name": "chrome.exe",
                "window_title": "Call center KPI Report - Google Sheets - Google Chrome",
                "event": "TYPE",
                "url": "docs.google.com/spreadsheets/d/1NuQdUH0ju6WDWrxeut6Thge8oLQ-JP4mJlHU32YO92Q/edit?gid=1993363355#gid=1993363355",
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



