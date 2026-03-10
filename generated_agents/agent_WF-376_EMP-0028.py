
import pyautogui
import time
import webbrowser
import os

# Generated Agent for Workflow: WF-376
# Employee: EMP-0028
# Pattern: chrome.exe:Custom_CLICK->chrome.exe:CLICK->chrome.exe:Custom_CLICK->chrome.exe:CLICK->chrome.exe:CLICK


def run_agent():
    print(f"--- Start Generated Agent for WF-376 ---")
    pyautogui.PAUSE = 1.0

    steps = [
        {
                "id_employee": "EMP-0028",
                "timestamp": "2026-02-23 12:04:13.368251+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Rihana_EMP-0028/screenshot/Feb23/86f3d796-25a1-444f-89fa-4ff9fd2d55f4.webp",
                "app_name": "chrome.exe",
                "window_title": "Superset - Google Chrome",
                "event": "Custom_CLICK",
                "url": "64.227.129.135:8088/sqllab/",
                "date": "2026-02-23"
        },
        {
                "id_employee": "EMP-0028",
                "timestamp": "2026-02-23 12:04:15.048000+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Rihana_EMP-0028/screenshot/Feb23/df0453c1-87bc-417d-a453-4278d06ec6b8.webp",
                "app_name": "chrome.exe",
                "window_title": "Superset - Google Chrome",
                "event": "CLICK",
                "url": "64.227.129.135:8088/sqllab/",
                "date": "2026-02-23"
        },
        {
                "id_employee": "EMP-0028",
                "timestamp": "2026-02-23 12:04:15.922610+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Rihana_EMP-0028/screenshot/Feb23/e2ed08f6-edb4-4dd4-9c96-2edcee4f10fb.webp",
                "app_name": "chrome.exe",
                "window_title": "Superset - Google Chrome",
                "event": "Custom_CLICK",
                "url": "64.227.129.135:8088/sqllab/",
                "date": "2026-02-23"
        },
        {
                "id_employee": "EMP-0028",
                "timestamp": "2026-02-23 12:04:25.039000+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Rihana_EMP-0028/screenshot/Feb23/e5c61ce4-fef7-446c-93b9-45df628bb152.webp",
                "app_name": "chrome.exe",
                "window_title": "Superset - Google Chrome",
                "event": "CLICK",
                "url": "64.227.129.135:8088/sqllab/",
                "date": "2026-02-23"
        },
        {
                "id_employee": "EMP-0028",
                "timestamp": "2026-02-23 12:04:35.024000+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Rihana_EMP-0028/screenshot/Feb23/ef6c7113-fbaf-4ed6-b716-1d7443c63719.webp",
                "app_name": "chrome.exe",
                "window_title": "Superset - Google Chrome",
                "event": "CLICK",
                "url": "64.227.129.135:8088/sqllab/",
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



