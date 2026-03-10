
import pyautogui
import time
import webbrowser
import os

# Generated Agent for Workflow: WF-636
# Employee: EMP-0053
# Pattern: chrome.exe:Custom_CLICK->chrome.exe:Custom_CLICK->chrome.exe:Custom_CLICK->chrome.exe:CLICK->chrome.exe:MOVE


def run_agent():
    print(f"--- Start Generated Agent for WF-636 ---")
    pyautogui.PAUSE = 1.0

    steps = [
        {
                "id_employee": "EMP-0053",
                "timestamp": "2026-02-23 10:09:44.879335+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Betelhem_EMP-0053/screenshot/Feb23/3750b32b-086c-4fa8-bdee-23d56558a2b3.webp",
                "app_name": "chrome.exe",
                "window_title": "Call center KPI Report - Google Sheets - Google Chrome",
                "event": "Custom_CLICK",
                "url": "docs.google.com/spreadsheets/d/1NuQdUH0ju6WDWrxeut6Thge8oLQ-JP4mJlHU32YO92Q/edit?gid=1993363355#gid=1993363355",
                "date": "2026-02-23"
        },
        {
                "id_employee": "EMP-0053",
                "timestamp": "2026-02-23 10:09:56.471222+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Betelhem_EMP-0053/screenshot/Feb23/adb151b9-6ba6-43bd-bf11-fe33fffb7c71.webp",
                "app_name": "chrome.exe",
                "window_title": "Call center KPI Report - Google Sheets - Google Chrome",
                "event": "Custom_CLICK",
                "url": "docs.google.com/spreadsheets/d/1NuQdUH0ju6WDWrxeut6Thge8oLQ-JP4mJlHU32YO92Q/edit?gid=1993363355#gid=1993363355",
                "date": "2026-02-23"
        },
        {
                "id_employee": "EMP-0053",
                "timestamp": "2026-02-23 10:09:58.644759+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Betelhem_EMP-0053/screenshot/Feb23/51d2d739-916e-4c80-b99b-afaefb638510.webp",
                "app_name": "chrome.exe",
                "window_title": "Call center KPI Report - Google Sheets - Google Chrome",
                "event": "Custom_CLICK",
                "url": "docs.google.com/spreadsheets/d/1NuQdUH0ju6WDWrxeut6Thge8oLQ-JP4mJlHU32YO92Q/edit?gid=1993363355#gid=1993363355",
                "date": "2026-02-23"
        },
        {
                "id_employee": "EMP-0053",
                "timestamp": "2026-02-23 10:20:00.009000+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Betelhem_EMP-0053/screenshot/Feb23/8924bb56-e342-40ad-866d-1ff98c858f91.webp",
                "app_name": "chrome.exe",
                "window_title": "Call center KPI Report - Google Sheets - Google Chrome",
                "event": "CLICK",
                "url": "docs.google.com/spreadsheets/d/1NuQdUH0ju6WDWrxeut6Thge8oLQ-JP4mJlHU32YO92Q/edit?gid=1993363355#gid=1993363355",
                "date": "2026-02-23"
        },
        {
                "id_employee": "EMP-0053",
                "timestamp": "2026-02-23 10:29:20.005000+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Betelhem_EMP-0053/screenshot/Feb23/40d93713-54a7-4029-94b0-5102124904fe.webp",
                "app_name": "chrome.exe",
                "window_title": "Inbox (46) - bettytagele90@gmail.com - Gmail - Google Chrome",
                "event": "MOVE",
                "url": "docs.google.com/spreadsheets/d/1BWXEQhoQOeWd921e_luYu8LeBKEFz7HSNVz_3c3gfO4/edit?gid=1108870173#gid=1108870173",
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



