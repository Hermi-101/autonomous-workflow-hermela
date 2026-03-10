
import pyautogui
import time
import webbrowser
import os

# Generated Agent for Workflow: WF-126
# Employee: EMP-0025
# Pattern: brave.exe:Custom_CLICK->Telegram.exe:APP_SWITCH->Telegram.exe:TYPE->Telegram.exe:Custom_CLICK->Telegram.exe:APP_SWITCH


def run_agent():
    print(f"--- Start Generated Agent for WF-126 ---")
    pyautogui.PAUSE = 1.0

    steps = [
        {
                "id_employee": "EMP-0025",
                "timestamp": "2026-02-23 07:26:34.107120+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Natnael_EMP-0025/screenshot/Feb23/113ae044-40c9-4504-95be-97dd495cc019.webp",
                "app_name": "brave.exe",
                "window_title": "ChipChip System Security Evaluation - Google Docs - Brave",
                "event": "Custom_CLICK",
                "url": "",
                "date": "2026-02-23"
        },
        {
                "id_employee": "EMP-0025",
                "timestamp": "2026-02-23 07:26:35.350000+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Natnael_EMP-0025/screenshot/Feb23/ec96a8c0-109e-46db-8d18-349690399eac.webp",
                "app_name": "Telegram.exe",
                "window_title": "\u200eKirubel Chip @ \u200eNA (6796)",
                "event": "APP_SWITCH",
                "url": "",
                "date": "2026-02-23"
        },
        {
                "id_employee": "EMP-0025",
                "timestamp": "2026-02-23 07:26:45.015000+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Natnael_EMP-0025/screenshot/Feb23/6ae14d9f-5640-488b-ba47-c9077520dae0.webp",
                "app_name": "Telegram.exe",
                "window_title": "TelegramDesktop",
                "event": "TYPE",
                "url": "",
                "date": "2026-02-23"
        },
        {
                "id_employee": "EMP-0025",
                "timestamp": "2026-02-23 07:26:45.155749+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Natnael_EMP-0025/screenshot/Feb23/c63d30a6-24be-47f2-b8ba-5f5535d0269e.webp",
                "app_name": "Telegram.exe",
                "window_title": "\u200eKirubel Chip @ \u200eNA (6796)",
                "event": "Custom_CLICK",
                "url": "",
                "date": "2026-02-23"
        },
        {
                "id_employee": "EMP-0025",
                "timestamp": "2026-02-23 07:26:47.710000+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Natnael_EMP-0025/screenshot/Feb23/209a86b0-0d5b-43b7-8f5c-85919b9c7449.webp",
                "app_name": "Telegram.exe",
                "window_title": "Media viewer",
                "event": "APP_SWITCH",
                "url": "",
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



