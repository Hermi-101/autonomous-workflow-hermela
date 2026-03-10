
import pyautogui
import time
import webbrowser
import os

# Generated Agent for Workflow: WF-417
# Employee: EMP-0028
# Pattern: chrome.exe:APP_SWITCH->chrome.exe:CLICK->chrome.exe:Custom_CLICK->flet.exe:APP_SWITCH->chrome.exe:APP_SWITCH


def run_agent():
    print(f"--- Start Generated Agent for WF-417 ---")
    pyautogui.PAUSE = 1.0

    steps = [
        {
                "id_employee": "EMP-0028",
                "timestamp": "2026-02-24 07:41:03.648000+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Rihana_EMP-0028/screenshot/Feb24/ed007881-035d-45a4-beb1-b5e0b2f6ea2a.webp",
                "app_name": "chrome.exe",
                "window_title": "Question \u00b7 Metabase - Google Chrome",
                "event": "APP_SWITCH",
                "url": "",
                "date": "2026-02-24"
        },
        {
                "id_employee": "EMP-0028",
                "timestamp": "2026-02-24 07:41:05.006000+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Rihana_EMP-0028/screenshot/Feb24/d9fcb91a-bb10-45cb-bb79-bc87de9cf1ef.webp",
                "app_name": "chrome.exe",
                "window_title": "Question \u00b7 Metabase - Google Chrome",
                "event": "CLICK",
                "url": "64.227.129.135:8088/login/?next=http://64.227.129.135:8088/sqllab/",
                "date": "2026-02-24"
        },
        {
                "id_employee": "EMP-0028",
                "timestamp": "2026-02-24 07:41:08.572951+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Rihana_EMP-0028/screenshot/Feb24/d622b97b-0211-4b9b-ab8f-e2d6e6bdd2ec.webp",
                "app_name": "chrome.exe",
                "window_title": "Question \u00b7 Metabase - Google Chrome",
                "event": "Custom_CLICK",
                "url": "",
                "date": "2026-02-24"
        },
        {
                "id_employee": "EMP-0028",
                "timestamp": "2026-02-24 07:41:08.739000+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Rihana_EMP-0028/screenshot/Feb24/fc616f46-09f4-4367-aab7-dd8aab29b15b.webp",
                "app_name": "flet.exe",
                "window_title": "Status Overlay",
                "event": "APP_SWITCH",
                "url": "",
                "date": "2026-02-24"
        },
        {
                "id_employee": "EMP-0028",
                "timestamp": "2026-02-24 07:41:13.823000+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Rihana_EMP-0028/screenshot/Feb24/1fc4260c-f8d4-49c5-b19e-1d279ed2531b.webp",
                "app_name": "chrome.exe",
                "window_title": "Question \u00b7 Metabase - Google Chrome",
                "event": "APP_SWITCH",
                "url": "64.227.129.135:8088/login/?next=http://64.227.129.135:8088/sqllab/",
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



