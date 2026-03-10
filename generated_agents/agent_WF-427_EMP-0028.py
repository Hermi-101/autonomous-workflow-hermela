
import pyautogui
import time
import webbrowser
import os

# Generated Agent for Workflow: WF-427
# Employee: EMP-0028
# Pattern: chrome.exe:TYPE->chrome.exe:Custom_CLICK->chrome.exe:Custom_CLICK->chrome.exe:Custom_CLICK->chrome.exe:CLICK


def run_agent():
    print(f"--- Start Generated Agent for WF-427 ---")
    pyautogui.PAUSE = 1.0

    steps = [
        {
                "id_employee": "EMP-0028",
                "timestamp": "2026-02-24 07:45:45.011000+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Rihana_EMP-0028/screenshot/Feb24/168dec94-ed47-4470-b1cf-ac36e3f8715a.webp",
                "app_name": "chrome.exe",
                "window_title": "Superset - Google Chrome",
                "event": "TYPE",
                "url": "64.227.129.135:8088/sqllab/",
                "date": "2026-02-24"
        },
        {
                "id_employee": "EMP-0028",
                "timestamp": "2026-02-24 07:45:45.893462+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Rihana_EMP-0028/screenshot/Feb24/3f5faaeb-3f3f-462b-8b21-0f3a61fcdf54.webp",
                "app_name": "chrome.exe",
                "window_title": "Superset - Google Chrome",
                "event": "Custom_CLICK",
                "url": "64.227.129.135:8088/sqllab/",
                "date": "2026-02-24"
        },
        {
                "id_employee": "EMP-0028",
                "timestamp": "2026-02-24 07:45:50.324242+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Rihana_EMP-0028/screenshot/Feb24/ac906273-d5d7-4bc1-ae68-4efebeff0445.webp",
                "app_name": "chrome.exe",
                "window_title": "Superset - Google Chrome",
                "event": "Custom_CLICK",
                "url": "64.227.129.135:8088/sqllab/",
                "date": "2026-02-24"
        },
        {
                "id_employee": "EMP-0028",
                "timestamp": "2026-02-24 07:45:56.684538+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Rihana_EMP-0028/screenshot/Feb24/a8aca6e7-68d0-488c-b3a9-e1d30a207b47.webp",
                "app_name": "chrome.exe",
                "window_title": "Superset - Google Chrome",
                "event": "Custom_CLICK",
                "url": "64.227.129.135:8088/sqllab/",
                "date": "2026-02-24"
        },
        {
                "id_employee": "EMP-0028",
                "timestamp": "2026-02-24 07:46:00.010000+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Rihana_EMP-0028/screenshot/Feb24/f9ab460e-43e5-420c-80de-4d71b4348b4d.webp",
                "app_name": "chrome.exe",
                "window_title": "Superset - Google Chrome",
                "event": "CLICK",
                "url": "64.227.129.135:8088/sqllab/",
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



