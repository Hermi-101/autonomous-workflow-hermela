
import pyautogui
import time
import webbrowser
import os

# Generated Agent for Workflow: WF-475
# Employee: EMP-0028
# Pattern: Telegram.exe:TYPE->Telegram.exe:APP_SWITCH->Telegram.exe:Custom_CLICK->Telegram.exe:Custom_CLICK->Telegram.exe:APP_SWITCH


def run_agent():
    print(f"--- Start Generated Agent for WF-475 ---")
    pyautogui.PAUSE = 1.0

    steps = [
        {
                "id_employee": "EMP-0028",
                "timestamp": "2026-02-24 09:55:10.015000+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Rihana_EMP-0028/screenshot/Feb24/75231e38-e714-48e5-8b49-2092d80192f8.webp",
                "app_name": "Telegram.exe",
                "window_title": "TelegramDesktop",
                "event": "TYPE",
                "url": "",
                "date": "2026-02-24"
        },
        {
                "id_employee": "EMP-0028",
                "timestamp": "2026-02-24 09:55:10.482000+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Rihana_EMP-0028/screenshot/Feb24/a4044ef3-c585-4a84-85fb-5ae5e1647c70.webp",
                "app_name": "Telegram.exe",
                "window_title": "\u200eNati Gebeya \u2013 (879554)",
                "event": "APP_SWITCH",
                "url": "",
                "date": "2026-02-24"
        },
        {
                "id_employee": "EMP-0028",
                "timestamp": "2026-02-24 09:55:16.801386+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Rihana_EMP-0028/screenshot/Feb24/e6bf0eb0-91fc-4286-bd5f-4bbfe221a9a4.webp",
                "app_name": "Telegram.exe",
                "window_title": "\u200eNati Gebeya \u2013 (879554)",
                "event": "Custom_CLICK",
                "url": "",
                "date": "2026-02-24"
        },
        {
                "id_employee": "EMP-0028",
                "timestamp": "2026-02-24 09:55:19.881935+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Rihana_EMP-0028/screenshot/Feb24/f2d1104a-0417-474b-9260-9a72c2a79e90.webp",
                "app_name": "Telegram.exe",
                "window_title": "\u200eNati Gebeya \u2013 (879554)",
                "event": "Custom_CLICK",
                "url": "",
                "date": "2026-02-24"
        },
        {
                "id_employee": "EMP-0028",
                "timestamp": "2026-02-24 09:55:22.784000+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Rihana_EMP-0028/screenshot/Feb24/65c24f24-5242-45c5-afe9-0b50498e8464.webp",
                "app_name": "Telegram.exe",
                "window_title": "\u200eNati Gebeya \u2013 (879554)",
                "event": "APP_SWITCH",
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



