
import pyautogui
import time
import webbrowser
import os

# Generated Agent for Workflow: WF-499
# Employee: EMP-0028
# Pattern: chrome.exe:Custom_CLICK->Telegram.exe:APP_SWITCH->Telegram.exe:TYPE->Telegram.exe:TYPE->Telegram.exe:Custom_CLICK


def run_agent():
    print(f"--- Start Generated Agent for WF-499 ---")
    pyautogui.PAUSE = 1.0

    steps = [
        {
                "id_employee": "EMP-0028",
                "timestamp": "2026-02-24 10:52:17.025932+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Rihana_EMP-0028/screenshot/Feb24/67f21e84-a4eb-4c00-9ccb-09b1bd5d0497.webp",
                "app_name": "chrome.exe",
                "window_title": "Financial Dashbord - Google Chrome",
                "event": "Custom_CLICK",
                "url": "",
                "date": "2026-02-24"
        },
        {
                "id_employee": "EMP-0028",
                "timestamp": "2026-02-24 10:52:17.400000+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Rihana_EMP-0028/screenshot/Feb24/002c9fee-df4c-4c61-a382-fedd4542ae8c.webp",
                "app_name": "Telegram.exe",
                "window_title": "(2) \u200eAmanuel Nigatu \u2013 (879633)",
                "event": "APP_SWITCH",
                "url": "",
                "date": "2026-02-24"
        },
        {
                "id_employee": "EMP-0028",
                "timestamp": "2026-02-24 10:52:25.005000+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Rihana_EMP-0028/screenshot/Feb24/b12a6b11-33b5-4240-a635-99038e9bb629.webp",
                "app_name": "Telegram.exe",
                "window_title": "\u200eAmanuel Nigatu \u2013 (879631)",
                "event": "TYPE",
                "url": "",
                "date": "2026-02-24"
        },
        {
                "id_employee": "EMP-0028",
                "timestamp": "2026-02-24 10:52:30.009000+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Rihana_EMP-0028/screenshot/Feb24/9356df57-342c-48c8-aeb2-61b2aca5b454.webp",
                "app_name": "Telegram.exe",
                "window_title": "\u200eAmanuel Nigatu \u2013 (879631)",
                "event": "TYPE",
                "url": "",
                "date": "2026-02-24"
        },
        {
                "id_employee": "EMP-0028",
                "timestamp": "2026-02-24 10:52:45.872149+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Rihana_EMP-0028/screenshot/Feb24/b471c2e9-ea23-4400-a55a-8d7ecdfc716e.webp",
                "app_name": "Telegram.exe",
                "window_title": "\u200eAmanuel Nigatu \u2013 (879631)",
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



