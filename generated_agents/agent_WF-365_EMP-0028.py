
import pyautogui
import time
import webbrowser
import os

# Generated Agent for Workflow: WF-365
# Employee: EMP-0028
# Pattern: chrome.exe:CLICK->chrome.exe:Custom_CLICK->chrome.exe:Custom_CLICK->chrome.exe:CLICK->chrome.exe:Custom_CLICK


def run_agent():
    print(f"--- Start Generated Agent for WF-365 ---")
    pyautogui.PAUSE = 1.0

    steps = [
        {
                "id_employee": "EMP-0028",
                "timestamp": "2026-02-23 11:58:45.043000+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Rihana_EMP-0028/screenshot/Feb23/9becaad6-1dfa-47f6-b284-d5ae021b7ad6.webp",
                "app_name": "chrome.exe",
                "window_title": "Superset - Google Chrome",
                "event": "CLICK",
                "url": "64.227.129.135:8088/sqllab/",
                "date": "2026-02-23"
        },
        {
                "id_employee": "EMP-0028",
                "timestamp": "2026-02-23 11:58:47.773837+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Rihana_EMP-0028/screenshot/Feb23/39131f7d-3e08-470c-9033-3ce307f4c593.webp",
                "app_name": "chrome.exe",
                "window_title": "Superset - Google Chrome",
                "event": "Custom_CLICK",
                "url": "64.227.129.135:8088/superset/welcome/",
                "date": "2026-02-23"
        },
        {
                "id_employee": "EMP-0028",
                "timestamp": "2026-02-23 11:58:49.750898+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Rihana_EMP-0028/screenshot/Feb23/c7b96195-c4fc-489e-8a06-f0292b4519c3.webp",
                "app_name": "chrome.exe",
                "window_title": "Superset - Google Chrome",
                "event": "Custom_CLICK",
                "url": "64.227.129.135:8088/superset/welcome/",
                "date": "2026-02-23"
        },
        {
                "id_employee": "EMP-0028",
                "timestamp": "2026-02-23 11:58:50.034000+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Rihana_EMP-0028/screenshot/Feb23/41a5c354-05d0-441b-87d1-30fb7e2078e0.webp",
                "app_name": "chrome.exe",
                "window_title": "Superset - Google Chrome",
                "event": "CLICK",
                "url": "64.227.129.135:8088/sqllab/",
                "date": "2026-02-23"
        },
        {
                "id_employee": "EMP-0028",
                "timestamp": "2026-02-23 11:58:51.351275+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Rihana_EMP-0028/screenshot/Feb23/bc97b9fd-a136-4810-ac33-530b36e1c9ff.webp",
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



