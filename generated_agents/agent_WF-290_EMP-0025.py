
import pyautogui
import time
import webbrowser
import os

# Generated Agent for Workflow: WF-290
# Employee: EMP-0025
# Pattern: Telegram.exe:APP_SWITCH->Telegram.exe:CLICK->Telegram.exe:Custom_CLICK->Telegram.exe:Custom_CLICK->Telegram.exe:APP_SWITCH


def run_agent():
    print(f"--- Start Generated Agent for WF-290 ---")
    pyautogui.PAUSE = 1.0

    steps = [
        {
                "id_employee": "EMP-0025",
                "timestamp": "2026-02-24 08:32:29.846000+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Natnael_EMP-0025/screenshot/Feb24/1d1fc0e0-6bb4-4b7a-aefe-9cf8a35efea5.webp",
                "app_name": "Telegram.exe",
                "window_title": "\u200eMehari @ \u200eNA (6935)",
                "event": "APP_SWITCH",
                "url": "",
                "date": "2026-02-24"
        },
        {
                "id_employee": "EMP-0025",
                "timestamp": "2026-02-24 08:32:30.014000+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Natnael_EMP-0025/screenshot/Feb24/f97e0471-1795-4aea-934a-4243b3ad4a11.webp",
                "app_name": "Telegram.exe",
                "window_title": "\u200eMehari @ \u200eNA (6936)",
                "event": "CLICK",
                "url": "",
                "date": "2026-02-24"
        },
        {
                "id_employee": "EMP-0025",
                "timestamp": "2026-02-24 08:32:33.994930+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Natnael_EMP-0025/screenshot/Feb24/8b52d3b6-1eee-4bfa-a0ea-ea75961b9780.webp",
                "app_name": "Telegram.exe",
                "window_title": "\u200eMehari @ \u200eNA (6935)",
                "event": "Custom_CLICK",
                "url": "",
                "date": "2026-02-24"
        },
        {
                "id_employee": "EMP-0025",
                "timestamp": "2026-02-24 08:32:35.436199+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Natnael_EMP-0025/screenshot/Feb24/85fb4dca-eb6d-476a-abb0-7aad7203698b.webp",
                "app_name": "Telegram.exe",
                "window_title": "\u200eMehari @ \u200eNA (6935)",
                "event": "Custom_CLICK",
                "url": "",
                "date": "2026-02-24"
        },
        {
                "id_employee": "EMP-0025",
                "timestamp": "2026-02-24 08:32:37.056000+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Natnael_EMP-0025/screenshot/Feb24/78929f81-9380-4647-9fd0-fd1373130641.webp",
                "app_name": "Telegram.exe",
                "window_title": "\u200eMehari @ \u200eNA (6936)",
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



