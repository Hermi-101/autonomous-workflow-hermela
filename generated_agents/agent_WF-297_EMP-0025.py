
import pyautogui
import time
import webbrowser
import os

# Generated Agent for Workflow: WF-297
# Employee: EMP-0025
# Pattern: brave.exe:TYPE->brave.exe:CLICK->brave.exe:Custom_CLICK->brave.exe:CLICK->brave.exe:Custom_CLICK


def run_agent():
    print(f"--- Start Generated Agent for WF-297 ---")
    pyautogui.PAUSE = 1.0

    steps = [
        {
                "id_employee": "EMP-0025",
                "timestamp": "2026-02-24 08:45:35.015000+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Natnael_EMP-0025/screenshot/Feb24/19469f06-216a-4be7-9a6e-ec519df7d6f5.webp",
                "app_name": "brave.exe",
                "window_title": "ChipChip Supply - Brave",
                "event": "TYPE",
                "url": "supplystaging.chipchip.social/inventory/stock-count",
                "date": "2026-02-24"
        },
        {
                "id_employee": "EMP-0025",
                "timestamp": "2026-02-24 08:45:40.005000+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Natnael_EMP-0025/screenshot/Feb24/ec51d9ae-a27a-4328-a5ab-577f2a96aaee.webp",
                "app_name": "brave.exe",
                "window_title": "ChipChip Supply - Brave",
                "event": "CLICK",
                "url": "supplystaging.chipchip.social/inventory/stock-count",
                "date": "2026-02-24"
        },
        {
                "id_employee": "EMP-0025",
                "timestamp": "2026-02-24 08:45:42.723629+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Natnael_EMP-0025/screenshot/Feb24/f293135e-badd-4a01-8f79-4b5a3547dff2.webp",
                "app_name": "brave.exe",
                "window_title": "ChipChip Supply - Brave",
                "event": "Custom_CLICK",
                "url": "supplystaging.chipchip.social/inventory/stock-count",
                "date": "2026-02-24"
        },
        {
                "id_employee": "EMP-0025",
                "timestamp": "2026-02-24 08:45:55.008000+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Natnael_EMP-0025/screenshot/Feb24/9249cd89-709b-4f45-b01a-772388e6ebc6.webp",
                "app_name": "brave.exe",
                "window_title": "ChipChip Supply - Brave",
                "event": "CLICK",
                "url": "supplystaging.chipchip.social/inventory/stock-count",
                "date": "2026-02-24"
        },
        {
                "id_employee": "EMP-0025",
                "timestamp": "2026-02-24 08:45:59.437105+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Natnael_EMP-0025/screenshot/Feb24/2bbee020-62cd-462d-b7bd-57625bf145e4.webp",
                "app_name": "brave.exe",
                "window_title": "Warehouse inventory February 2026 - Google Sheets - Brave",
                "event": "Custom_CLICK",
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



