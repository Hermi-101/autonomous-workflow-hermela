
import pyautogui
import time
import webbrowser
import os

# Generated Agent for Workflow: WF-304
# Employee: EMP-0025
# Pattern: brave.exe:Custom_CLICK->brave.exe:TYPE->brave.exe:MOVE->brave.exe:CLICK->brave.exe:Custom_CLICK


def run_agent():
    print(f"--- Start Generated Agent for WF-304 ---")
    pyautogui.PAUSE = 1.0

    steps = [
        {
                "id_employee": "EMP-0025",
                "timestamp": "2026-02-24 09:18:14.546558+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Natnael_EMP-0025/screenshot/Feb24/d4adec29-d718-428f-8bc8-5692709ca516.webp",
                "app_name": "brave.exe",
                "window_title": "Warehouse inventory February 2026 - Google Sheets - Brave",
                "event": "Custom_CLICK",
                "url": "docs.google.com/spreadsheets/d/1FLtbJMfNi2f2aZh_9kaOx9lkPMNQXeujQpwJZmeSsWU/edit?gid=0#gid=0",
                "date": "2026-02-24"
        },
        {
                "id_employee": "EMP-0025",
                "timestamp": "2026-02-24 09:18:15.002000+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Natnael_EMP-0025/screenshot/Feb24/73cde09b-d722-4399-a439-d2cfb5c1967b.webp",
                "app_name": "brave.exe",
                "window_title": "ChipChip Supply - Brave",
                "event": "TYPE",
                "url": "",
                "date": "2026-02-24"
        },
        {
                "id_employee": "EMP-0025",
                "timestamp": "2026-02-24 09:18:40.001000+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Natnael_EMP-0025/screenshot/Feb24/29c84c98-06e3-44a8-b538-e3007af92e66.webp",
                "app_name": "brave.exe",
                "window_title": "ChipChip Supply - Brave",
                "event": "MOVE",
                "url": "",
                "date": "2026-02-24"
        },
        {
                "id_employee": "EMP-0025",
                "timestamp": "2026-02-24 09:19:25.012000+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Natnael_EMP-0025/screenshot/Feb24/612fba7e-5302-4024-877a-f5e2f7f2d21f.webp",
                "app_name": "brave.exe",
                "window_title": "Warehouse inventory February 2026 - Google Sheets - Brave",
                "event": "CLICK",
                "url": "docs.google.com/spreadsheets/d/1FLtbJMfNi2f2aZh_9kaOx9lkPMNQXeujQpwJZmeSsWU/edit?gid=0#gid=0",
                "date": "2026-02-24"
        },
        {
                "id_employee": "EMP-0025",
                "timestamp": "2026-02-24 09:19:29.629680+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Natnael_EMP-0025/screenshot/Feb24/996d0911-2a6c-48db-abbb-b7e99eaa8b00.webp",
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



