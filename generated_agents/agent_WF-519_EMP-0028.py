
import pyautogui
import time
import webbrowser
import os

# Generated Agent for Workflow: WF-519
# Employee: EMP-0028
# Pattern: chrome.exe:CLICK->Telegram.exe:APP_SWITCH->chrome.exe:APP_SWITCH->chrome.exe:Custom_CLICK->chrome.exe:APP_SWITCH


def run_agent():
    print(f"--- Start Generated Agent for WF-519 ---")
    pyautogui.PAUSE = 1.0

    steps = [
        {
                "id_employee": "EMP-0028",
                "timestamp": "2026-02-24 12:49:10.003000+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Rihana_EMP-0028/screenshot/Feb24/91f95e5e-39e0-490e-aa1f-2ed6f7801452.webp",
                "app_name": "chrome.exe",
                "window_title": "Late Arrival - Poe - Google Chrome",
                "event": "CLICK",
                "url": "chatgpt.com/c/68f5f983-83f4-8325-9529-8423724644db",
                "date": "2026-02-24"
        },
        {
                "id_employee": "EMP-0028",
                "timestamp": "2026-02-24 12:49:14.268000+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Rihana_EMP-0028/screenshot/Feb24/084a2a0d-bc08-4916-bc21-b5f31177e514.webp",
                "app_name": "Telegram.exe",
                "window_title": "\u200eMehari \u2013 (879784)",
                "event": "APP_SWITCH",
                "url": "",
                "date": "2026-02-24"
        },
        {
                "id_employee": "EMP-0028",
                "timestamp": "2026-02-24 12:49:15.301000+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Rihana_EMP-0028/screenshot/Feb24/755befa1-d6ea-4d70-8ec9-e1abb841c7f8.webp",
                "app_name": "chrome.exe",
                "window_title": "Superset - Google Chrome",
                "event": "APP_SWITCH",
                "url": "poe.com/chat/25r666lphmcstfvcum6",
                "date": "2026-02-24"
        },
        {
                "id_employee": "EMP-0028",
                "timestamp": "2026-02-24 12:49:16.622379+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Rihana_EMP-0028/screenshot/Feb24/be807286-b6d8-4b4e-899a-972aaf609832.webp",
                "app_name": "chrome.exe",
                "window_title": "Superset - Google Chrome",
                "event": "Custom_CLICK",
                "url": "poe.com/chat/25r666lphmcstfvcum6",
                "date": "2026-02-24"
        },
        {
                "id_employee": "EMP-0028",
                "timestamp": "2026-02-24 12:49:17.337000+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Rihana_EMP-0028/screenshot/Feb24/646d9058-9408-474a-ba9f-dabb1228a6d4.webp",
                "app_name": "chrome.exe",
                "window_title": "Late Arrival - Poe - Google Chrome",
                "event": "APP_SWITCH",
                "url": "chatgpt.com/c/68f5f983-83f4-8325-9529-8423724644db",
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



