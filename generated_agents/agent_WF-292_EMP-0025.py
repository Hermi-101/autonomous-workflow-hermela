
import pyautogui
import time
import webbrowser
import os

# Generated Agent for Workflow: WF-292
# Employee: EMP-0025
# Pattern: brave.exe:MOVE->brave.exe:CLICK->brave.exe:Custom_CLICK->brave.exe:Custom_CLICK->brave.exe:APP_SWITCH


def run_agent():
    print(f"--- Start Generated Agent for WF-292 ---")
    pyautogui.PAUSE = 1.0

    steps = [
        {
                "id_employee": "EMP-0025",
                "timestamp": "2026-02-24 08:35:40.015000+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Natnael_EMP-0025/screenshot/Feb24/abf0fc31-ee43-4f5a-87b6-064c0c8454aa.webp",
                "app_name": "brave.exe",
                "window_title": "Warehouse inventory February 2026 - Google Sheets - Brave",
                "event": "MOVE",
                "url": "docs.google.com/spreadsheets/d/1FLtbJMfNi2f2aZh_9kaOx9lkPMNQXeujQpwJZmeSsWU/edit?gid=895107596#gid=895107596",
                "date": "2026-02-24"
        },
        {
                "id_employee": "EMP-0025",
                "timestamp": "2026-02-24 08:35:45.005000+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Natnael_EMP-0025/screenshot/Feb24/c33f72b9-2371-46d8-a9fc-f9b98b689db7.webp",
                "app_name": "brave.exe",
                "window_title": "Warehouse inventory February 2026 - Google Sheets - Brave",
                "event": "CLICK",
                "url": "docs.google.com/spreadsheets/d/1FLtbJMfNi2f2aZh_9kaOx9lkPMNQXeujQpwJZmeSsWU/edit?gid=0#gid=0",
                "date": "2026-02-24"
        },
        {
                "id_employee": "EMP-0025",
                "timestamp": "2026-02-24 08:35:45.442267+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Natnael_EMP-0025/screenshot/Feb24/23117f58-c037-4dcf-8302-70cf2a9d4baa.webp",
                "app_name": "brave.exe",
                "window_title": "Warehouse inventory February 2026 - Google Sheets - Brave",
                "event": "Custom_CLICK",
                "url": "docs.google.com/spreadsheets/d/1FLtbJMfNi2f2aZh_9kaOx9lkPMNQXeujQpwJZmeSsWU/edit?gid=0#gid=0",
                "date": "2026-02-24"
        },
        {
                "id_employee": "EMP-0025",
                "timestamp": "2026-02-24 08:35:56.003132+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Natnael_EMP-0025/screenshot/Feb24/711b7d1b-cd2e-492d-be8a-e029e5e2b202.webp",
                "app_name": "brave.exe",
                "window_title": "Warehouse inventory February 2026 - Google Sheets - Brave",
                "event": "Custom_CLICK",
                "url": "supplystaging.chipchip.social/inventory/stock-count",
                "date": "2026-02-24"
        },
        {
                "id_employee": "EMP-0025",
                "timestamp": "2026-02-24 08:35:56.613000+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Natnael_EMP-0025/screenshot/Feb24/a442ccb3-6ed6-47da-80a7-f0d50d774506.webp",
                "app_name": "brave.exe",
                "window_title": "ChipChip Supply - Brave",
                "event": "APP_SWITCH",
                "url": "docs.google.com/spreadsheets/d/1FLtbJMfNi2f2aZh_9kaOx9lkPMNQXeujQpwJZmeSsWU/edit?gid=0#gid=0",
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



