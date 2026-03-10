
import pyautogui
import time
import webbrowser
import os

# Generated Agent for Workflow: WF-269
# Employee: EMP-0025
# Pattern: Telegram.exe:APP_SWITCH->Telegram.exe:Custom_CLICK->Telegram.exe:TYPE->Telegram.exe:Custom_CLICK->Telegram.exe:APP_SWITCH


def run_agent():
    print(f"--- Start Generated Agent for WF-269 ---")
    pyautogui.PAUSE = 1.0

    steps = [
        {
                "id_employee": "EMP-0025",
                "timestamp": "2026-02-24 05:23:16.927000+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Natnael_EMP-0025/screenshot/Feb24/f6e73088-c473-448d-9cd1-db4235cf14fc.webp",
                "app_name": "Telegram.exe",
                "window_title": "(9) \u200eVendor x Marketing (ChipChip) @ \u200eNA (6905)",
                "event": "APP_SWITCH",
                "url": "",
                "date": "2026-02-24"
        },
        {
                "id_employee": "EMP-0025",
                "timestamp": "2026-02-24 05:23:18.712030+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Natnael_EMP-0025/screenshot/Feb24/112f391e-0b16-4b54-9d07-b218461c3061.webp",
                "app_name": "Telegram.exe",
                "window_title": "(9) \u200eVendor x Marketing (ChipChip) @ \u200eNA (6905)",
                "event": "Custom_CLICK",
                "url": "",
                "date": "2026-02-24"
        },
        {
                "id_employee": "EMP-0025",
                "timestamp": "2026-02-24 05:23:20.003000+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Natnael_EMP-0025/screenshot/Feb24/9072fb69-40a6-4a4a-8179-06acec98d5b0.webp",
                "app_name": "Telegram.exe",
                "window_title": "(9) \u200eVendor x Marketing (ChipChip) @ \u200eNA (6905)",
                "event": "TYPE",
                "url": "",
                "date": "2026-02-24"
        },
        {
                "id_employee": "EMP-0025",
                "timestamp": "2026-02-24 05:23:20.352227+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Natnael_EMP-0025/screenshot/Feb24/870bad2c-7be3-46d9-a030-45d8d54a7cb3.webp",
                "app_name": "Telegram.exe",
                "window_title": "(9) \u200eVendor x Marketing (ChipChip) @ \u200eNA (6905)",
                "event": "Custom_CLICK",
                "url": "",
                "date": "2026-02-24"
        },
        {
                "id_employee": "EMP-0025",
                "timestamp": "2026-02-24 05:23:21.056000+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Natnael_EMP-0025/screenshot/Feb24/23614894-3dba-4eb1-9753-770e5e9f1b1a.webp",
                "app_name": "Telegram.exe",
                "window_title": "Media viewer",
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



