
import pyautogui
import time
import webbrowser
import os

# Generated Agent for Workflow: WF-322
# Employee: EMP-0028
# Pattern: chrome.exe:APP_SWITCH->chrome.exe:Custom_CLICK->chrome.exe:Custom_CLICK->chrome.exe:Custom_CLICK->chrome.exe:Custom_CLICK


def run_agent():
    print(f"--- Start Generated Agent for WF-322 ---")
    pyautogui.PAUSE = 1.0

    steps = [
        {
                "id_employee": "EMP-0028",
                "timestamp": "2026-02-23 11:33:10.047000+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Rihana_EMP-0028/screenshot/Feb23/337ab0ff-1cb3-4199-a7ad-566aa45008b6.webp",
                "app_name": "chrome.exe",
                "window_title": "Superset - Google Chrome",
                "event": "APP_SWITCH",
                "url": "64.227.129.135:8088/sqllab/",
                "date": "2026-02-23"
        },
        {
                "id_employee": "EMP-0028",
                "timestamp": "2026-02-23 11:33:27.634399+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Rihana_EMP-0028/screenshot/Feb23/27d95c78-5c80-4c93-8aef-7b3952aeaff0.webp",
                "app_name": "chrome.exe",
                "window_title": "Superset - Google Chrome",
                "event": "Custom_CLICK",
                "url": "64.227.129.135:8088/sqllab/",
                "date": "2026-02-23"
        },
        {
                "id_employee": "EMP-0028",
                "timestamp": "2026-02-23 11:33:53.725875+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Rihana_EMP-0028/screenshot/Feb23/3b87657d-85ed-4143-8c09-7807a9b82808.webp",
                "app_name": "chrome.exe",
                "window_title": "Superset - Google Chrome",
                "event": "Custom_CLICK",
                "url": "64.227.129.135:8088/sqllab/",
                "date": "2026-02-23"
        },
        {
                "id_employee": "EMP-0028",
                "timestamp": "2026-02-23 11:34:16.814410+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Rihana_EMP-0028/screenshot/Feb23/42f0787f-52a7-481f-811c-65f3cc1f9303.webp",
                "app_name": "chrome.exe",
                "window_title": "Superset - Google Chrome",
                "event": "Custom_CLICK",
                "url": "64.227.129.135:8088/sqllab/",
                "date": "2026-02-23"
        },
        {
                "id_employee": "EMP-0028",
                "timestamp": "2026-02-23 11:34:37.695673+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Rihana_EMP-0028/screenshot/Feb23/9ce0f763-c200-4056-894f-4d21e136c317.webp",
                "app_name": "chrome.exe",
                "window_title": "Superset - Google Chrome",
                "event": "Custom_CLICK",
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



