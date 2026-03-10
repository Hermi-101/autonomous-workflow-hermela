
import pyautogui
import time
import webbrowser
import os

# Generated Agent for Workflow: WF-350
# Employee: EMP-0028
# Pattern: explorer.exe:Custom_CLICK->Telegram.exe:APP_SWITCH->Telegram.exe:Custom_CLICK->Telegram.exe:Custom_CLICK->Telegram.exe:APP_SWITCH


def run_agent():
    print(f"--- Start Generated Agent for WF-350 ---")
    pyautogui.PAUSE = 1.0

    steps = [
        {
                "id_employee": "EMP-0028",
                "timestamp": "2026-02-23 11:45:45.100817+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Rihana_EMP-0028/screenshot/Feb23/62d2bfc8-e184-4db2-865b-31fe82940192.webp",
                "app_name": "explorer.exe",
                "window_title": "\u200eHani 3 \u2013 (882603)",
                "event": "Custom_CLICK",
                "url": "",
                "date": "2026-02-23"
        },
        {
                "id_employee": "EMP-0028",
                "timestamp": "2026-02-23 11:45:50.303000+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Rihana_EMP-0028/screenshot/Feb23/040d9de5-dd0e-4181-8c89-8685309dce44.webp",
                "app_name": "Telegram.exe",
                "window_title": "\u200eHani 3 \u2013 (882603)",
                "event": "APP_SWITCH",
                "url": "",
                "date": "2026-02-23"
        },
        {
                "id_employee": "EMP-0028",
                "timestamp": "2026-02-23 11:45:50.466145+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Rihana_EMP-0028/screenshot/Feb23/0c4e5ab1-7a8c-4d1d-ac00-5fcdd9503bd7.webp",
                "app_name": "Telegram.exe",
                "window_title": "\u200eHani 3 \u2013 (882603)",
                "event": "Custom_CLICK",
                "url": "",
                "date": "2026-02-23"
        },
        {
                "id_employee": "EMP-0028",
                "timestamp": "2026-02-23 11:45:53.985573+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Rihana_EMP-0028/screenshot/Feb23/bdcbed6d-dab7-4d63-8f97-3729394c92ea.webp",
                "app_name": "Telegram.exe",
                "window_title": "\u200eHani 3 \u2013 (882603)",
                "event": "Custom_CLICK",
                "url": "",
                "date": "2026-02-23"
        },
        {
                "id_employee": "EMP-0028",
                "timestamp": "2026-02-23 11:46:14.309000+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Rihana_EMP-0028/screenshot/Feb23/ca96696e-6d29-4820-9135-4b4a6c8b271d.webp",
                "app_name": "Telegram.exe",
                "window_title": "\u200eBrayce Fepa \u2013 (882604)",
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



