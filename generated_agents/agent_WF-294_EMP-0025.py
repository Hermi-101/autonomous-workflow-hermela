
import pyautogui
import time
import webbrowser
import os

# Generated Agent for Workflow: WF-294
# Employee: EMP-0025
# Pattern: Telegram.exe:APP_SWITCH->Telegram.exe:Custom_CLICK->Telegram.exe:APP_SWITCH->brave.exe:TYPE->Telegram.exe:APP_SWITCH


def run_agent():
    print(f"--- Start Generated Agent for WF-294 ---")
    pyautogui.PAUSE = 1.0

    steps = [
        {
                "id_employee": "EMP-0025",
                "timestamp": "2026-02-24 08:39:38.303000+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Natnael_EMP-0025/screenshot/Feb24/fbca0464-22d1-4c41-aef3-5a7aee0d6509.webp",
                "app_name": "Telegram.exe",
                "window_title": "\u200eBrayce Fepa @ \u200eNA (6938)",
                "event": "APP_SWITCH",
                "url": "",
                "date": "2026-02-24"
        },
        {
                "id_employee": "EMP-0025",
                "timestamp": "2026-02-24 08:39:43.667787+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Natnael_EMP-0025/screenshot/Feb24/f0584444-8242-4608-87cf-429a9284ee52.webp",
                "app_name": "Telegram.exe",
                "window_title": "\u200eBrayce Fepa @ \u200eNA (6938)",
                "event": "Custom_CLICK",
                "url": "",
                "date": "2026-02-24"
        },
        {
                "id_employee": "EMP-0025",
                "timestamp": "2026-02-24 08:39:44.450000+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Natnael_EMP-0025/screenshot/Feb24/3e61c5d2-3d34-471c-8a0a-1dafa9fd32a6.webp",
                "app_name": "Telegram.exe",
                "window_title": "\u200eAmir @ \u200eNA (6938)",
                "event": "APP_SWITCH",
                "url": "",
                "date": "2026-02-24"
        },
        {
                "id_employee": "EMP-0025",
                "timestamp": "2026-02-24 08:39:45.011000+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Natnael_EMP-0025/screenshot/Feb24/22c3190d-8e36-4ac6-8387-f2f0e56e6080.webp",
                "app_name": "brave.exe",
                "window_title": "Warehouse inventory February 2026 - Google Sheets - Brave",
                "event": "TYPE",
                "url": "docs.google.com/spreadsheets/d/1FLtbJMfNi2f2aZh_9kaOx9lkPMNQXeujQpwJZmeSsWU/edit?gid=0#gid=0",
                "date": "2026-02-24"
        },
        {
                "id_employee": "EMP-0025",
                "timestamp": "2026-02-24 08:39:49.613000+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Natnael_EMP-0025/screenshot/Feb24/b64433f7-c968-4961-9477-70aaa6596318.webp",
                "app_name": "Telegram.exe",
                "window_title": "\u200eBrayce Fepa @ \u200eNA (6938)",
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



