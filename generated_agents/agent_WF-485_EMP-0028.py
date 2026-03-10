
import pyautogui
import time
import webbrowser
import os

# Generated Agent for Workflow: WF-485
# Employee: EMP-0028
# Pattern: chrome.exe:Custom_CLICK->chrome.exe:Custom_CLICK->Telegram.exe:APP_SWITCH->Telegram.exe:APP_SWITCH->Telegram.exe:Custom_CLICK


def run_agent():
    print(f"--- Start Generated Agent for WF-485 ---")
    pyautogui.PAUSE = 1.0

    steps = [
        {
                "id_employee": "EMP-0028",
                "timestamp": "2026-02-24 10:19:31.863714+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Rihana_EMP-0028/screenshot/Feb24/619c20f3-c60d-47e0-bfa0-a1c30ef50145.webp",
                "app_name": "chrome.exe",
                "window_title": "Financial Dashbord - Google Chrome",
                "event": "Custom_CLICK",
                "url": "64.227.129.135:8088/superset/dashboard/66/",
                "date": "2026-02-24"
        },
        {
                "id_employee": "EMP-0028",
                "timestamp": "2026-02-24 10:19:41.048318+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Rihana_EMP-0028/screenshot/Feb24/c08c0a67-f47e-4a96-aab5-63eb1e69546a.webp",
                "app_name": "chrome.exe",
                "window_title": "Financial Dashbord - Google Chrome",
                "event": "Custom_CLICK",
                "url": "",
                "date": "2026-02-24"
        },
        {
                "id_employee": "EMP-0028",
                "timestamp": "2026-02-24 10:19:41.915000+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Rihana_EMP-0028/screenshot/Feb24/92c3b3ac-9720-40d2-97b1-a55f6a4dbb56.webp",
                "app_name": "Telegram.exe",
                "window_title": "\u200eAmanuel Nigatu \u2013 (879601)",
                "event": "APP_SWITCH",
                "url": "",
                "date": "2026-02-24"
        },
        {
                "id_employee": "EMP-0028",
                "timestamp": "2026-02-24 10:19:49.076000+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Rihana_EMP-0028/screenshot/Feb24/ecc65fc1-27a5-4e35-af1b-75d53a45caf4.webp",
                "app_name": "Telegram.exe",
                "window_title": "TelegramDesktop",
                "event": "APP_SWITCH",
                "url": "",
                "date": "2026-02-24"
        },
        {
                "id_employee": "EMP-0028",
                "timestamp": "2026-02-24 10:19:50.089841+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Rihana_EMP-0028/screenshot/Feb24/3dc52406-2d21-4028-a3d7-e76565f6e3b8.webp",
                "app_name": "Telegram.exe",
                "window_title": "TelegramDesktop",
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



