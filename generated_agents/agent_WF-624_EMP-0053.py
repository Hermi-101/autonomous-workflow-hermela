
import pyautogui
import time
import webbrowser
import os

# Generated Agent for Workflow: WF-624
# Employee: EMP-0053
# Pattern: chrome.exe:Custom_CLICK->chrome.exe:CLICK->chrome.exe:Custom_CLICK->chrome.exe:CLICK->chrome.exe:CLICK


def run_agent():
    print(f"--- Start Generated Agent for WF-624 ---")
    pyautogui.PAUSE = 1.0

    steps = [
        {
                "id_employee": "EMP-0053",
                "timestamp": "2026-02-23 09:26:56.535826+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Betelhem_EMP-0053/screenshot/Feb23/2aff3907-eeab-4992-ab80-e867f83701cd.webp",
                "app_name": "chrome.exe",
                "window_title": "Call center KPI Report - Google Sheets - Google Chrome",
                "event": "Custom_CLICK",
                "url": "docs.google.com/spreadsheets/d/1NuQdUH0ju6WDWrxeut6Thge8oLQ-JP4mJlHU32YO92Q/edit?gid=523742192#gid=523742192",
                "date": "2026-02-23"
        },
        {
                "id_employee": "EMP-0053",
                "timestamp": "2026-02-23 09:27:45.003000+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Betelhem_EMP-0053/screenshot/Feb23/bf0eb3db-977e-46e2-8ede-6558424a3862.webp",
                "app_name": "chrome.exe",
                "window_title": "Call center KPI Report - Google Sheets - Google Chrome",
                "event": "CLICK",
                "url": "docs.google.com/spreadsheets/d/1NuQdUH0ju6WDWrxeut6Thge8oLQ-JP4mJlHU32YO92Q/edit?gid=1993363355#gid=1993363355",
                "date": "2026-02-23"
        },
        {
                "id_employee": "EMP-0053",
                "timestamp": "2026-02-23 09:27:45.541235+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Betelhem_EMP-0053/screenshot/Feb23/48dd4329-4e36-4357-a57f-a2f12775d5c7.webp",
                "app_name": "chrome.exe",
                "window_title": "Call center KPI Report - Google Sheets - Google Chrome",
                "event": "Custom_CLICK",
                "url": "docs.google.com/spreadsheets/d/1NuQdUH0ju6WDWrxeut6Thge8oLQ-JP4mJlHU32YO92Q/edit?gid=1993363355#gid=1993363355",
                "date": "2026-02-23"
        },
        {
                "id_employee": "EMP-0053",
                "timestamp": "2026-02-23 09:28:00.002000+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Betelhem_EMP-0053/screenshot/Feb23/3097ff04-10cd-4a25-bed2-f5cb35777104.webp",
                "app_name": "chrome.exe",
                "window_title": "Call center KPI Report - Google Sheets - Google Chrome",
                "event": "CLICK",
                "url": "docs.google.com/spreadsheets/d/1NuQdUH0ju6WDWrxeut6Thge8oLQ-JP4mJlHU32YO92Q/edit?gid=1993363355#gid=1993363355",
                "date": "2026-02-23"
        },
        {
                "id_employee": "EMP-0053",
                "timestamp": "2026-02-23 09:28:40.005000+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Betelhem_EMP-0053/screenshot/Feb23/32eefbf7-532a-4a87-b7b2-4287686438cf.webp",
                "app_name": "chrome.exe",
                "window_title": "Call center KPI Report - Google Sheets - Google Chrome",
                "event": "CLICK",
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



