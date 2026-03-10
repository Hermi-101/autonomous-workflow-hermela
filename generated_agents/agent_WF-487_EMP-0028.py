
import pyautogui
import time
import webbrowser
import os

# Generated Agent for Workflow: WF-487
# Employee: EMP-0028
# Pattern: chrome.exe:Custom_CLICK->chrome.exe:Custom_CLICK->chrome.exe:TYPE->chrome.exe:Custom_CLICK->chrome.exe:TYPE


def run_agent():
    print(f"--- Start Generated Agent for WF-487 ---")
    pyautogui.PAUSE = 1.0

    steps = [
        {
                "id_employee": "EMP-0028",
                "timestamp": "2026-02-24 10:24:24.151952+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Rihana_EMP-0028/screenshot/Feb24/c0940515-44e0-4ff0-9971-c78e517946fd.webp",
                "app_name": "chrome.exe",
                "window_title": "Superset - Google Chrome",
                "event": "Custom_CLICK",
                "url": "64.227.129.135:8088/sqllab",
                "date": "2026-02-24"
        },
        {
                "id_employee": "EMP-0028",
                "timestamp": "2026-02-24 10:24:30.294607+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Rihana_EMP-0028/screenshot/Feb24/c18f11d9-a2aa-435c-aa15-cd5e6a50f1dc.webp",
                "app_name": "chrome.exe",
                "window_title": "Superset - Google Chrome",
                "event": "Custom_CLICK",
                "url": "64.227.129.135:8088/sqllab",
                "date": "2026-02-24"
        },
        {
                "id_employee": "EMP-0028",
                "timestamp": "2026-02-24 10:24:35.014000+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Rihana_EMP-0028/screenshot/Feb24/06ccb068-839f-4173-850a-4ec17efd536a.webp",
                "app_name": "chrome.exe",
                "window_title": "Superset - Google Chrome",
                "event": "TYPE",
                "url": "64.227.129.135:8088/sqllab",
                "date": "2026-02-24"
        },
        {
                "id_employee": "EMP-0028",
                "timestamp": "2026-02-24 10:24:36.763929+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Rihana_EMP-0028/screenshot/Feb24/be293e89-f017-487c-9a6c-1aaa6fe71d0b.webp",
                "app_name": "chrome.exe",
                "window_title": "Superset - Google Chrome",
                "event": "Custom_CLICK",
                "url": "64.227.129.135:8088/sqllab",
                "date": "2026-02-24"
        },
        {
                "id_employee": "EMP-0028",
                "timestamp": "2026-02-24 10:24:45.005000+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Rihana_EMP-0028/screenshot/Feb24/1daa1a4c-f191-4982-a111-548fdb57193f.webp",
                "app_name": "chrome.exe",
                "window_title": "Superset - Google Chrome",
                "event": "TYPE",
                "url": "64.227.129.135:8088/sqllab",
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



