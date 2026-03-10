
import pyautogui
import time
import webbrowser
import os

# Generated Agent for Workflow: WF-450
# Employee: EMP-0028
# Pattern: chrome.exe:Custom_CLICK->chrome.exe:Custom_CLICK->chrome.exe:Custom_CLICK->Telegram.exe:Custom_CLICK->Telegram.exe:Custom_CLICK


def run_agent():
    print(f"--- Start Generated Agent for WF-450 ---")
    pyautogui.PAUSE = 1.0

    steps = [
        {
                "id_employee": "EMP-0028",
                "timestamp": "2026-02-24 08:36:30.141887+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Rihana_EMP-0028/screenshot/Feb24/27f5dc6d-f73d-4236-979c-8c5b72f8777d.webp",
                "app_name": "chrome.exe",
                "window_title": "Superset - Google Chrome",
                "event": "Custom_CLICK",
                "url": "64.227.129.135:8088/sqllab/",
                "date": "2026-02-24"
        },
        {
                "id_employee": "EMP-0028",
                "timestamp": "2026-02-24 08:36:33.920519+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Rihana_EMP-0028/screenshot/Feb24/fceda1ec-2e04-4b3a-a38c-20b032ef788a.webp",
                "app_name": "chrome.exe",
                "window_title": "Superset - Google Chrome",
                "event": "Custom_CLICK",
                "url": "64.227.129.135:8088/sqllab/",
                "date": "2026-02-24"
        },
        {
                "id_employee": "EMP-0028",
                "timestamp": "2026-02-24 08:36:39.876980+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Rihana_EMP-0028/screenshot/Feb24/bf919a50-a2bf-40c6-8386-0c770f72b85b.webp",
                "app_name": "chrome.exe",
                "window_title": "Superset - Google Chrome",
                "event": "Custom_CLICK",
                "url": "",
                "date": "2026-02-24"
        },
        {
                "id_employee": "EMP-0028",
                "timestamp": "2026-02-24 08:36:41.957326+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Rihana_EMP-0028/screenshot/Feb24/f02015e7-72ec-4106-9bf5-663862703394.webp",
                "app_name": "Telegram.exe",
                "window_title": "\u200eSiltawi \u1235\u120d\u1273\u12ca \u2013 (879436)",
                "event": "Custom_CLICK",
                "url": "",
                "date": "2026-02-24"
        },
        {
                "id_employee": "EMP-0028",
                "timestamp": "2026-02-24 08:36:45.471131+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Rihana_EMP-0028/screenshot/Feb24/b7edb138-966e-4488-bfd5-a868476a371e.webp",
                "app_name": "Telegram.exe",
                "window_title": "\u200eSiltawi \u1235\u120d\u1273\u12ca \u2013 (879436)",
                "event": "Custom_CLICK",
                "url": "",
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



