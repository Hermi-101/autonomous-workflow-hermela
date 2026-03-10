
import pyautogui
import time
import webbrowser
import os

# Generated Agent for Workflow: WF-300
# Employee: EMP-0025
# Pattern: brave.exe:CLICK->brave.exe:Custom_CLICK->brave.exe:APP_SWITCH->brave.exe:TYPE->brave.exe:Custom_CLICK


def run_agent():
    print(f"--- Start Generated Agent for WF-300 ---")
    pyautogui.PAUSE = 1.0

    steps = [
        {
                "id_employee": "EMP-0025",
                "timestamp": "2026-02-24 09:07:25+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Natnael_EMP-0025/screenshot/Feb24/cacb2386-4b28-47b2-92da-8e46507c2a39.webp",
                "app_name": "brave.exe",
                "window_title": "ChipChip Supply - Brave",
                "event": "CLICK",
                "url": "",
                "date": "2026-02-24"
        },
        {
                "id_employee": "EMP-0025",
                "timestamp": "2026-02-24 09:07:25.405602+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Natnael_EMP-0025/screenshot/Feb24/9f259b0b-54d5-415b-a245-1bccc02a45ac.webp",
                "app_name": "brave.exe",
                "window_title": "Warehouse inventory February 2026 - Google Sheets - Brave",
                "event": "Custom_CLICK",
                "url": "docs.google.com/spreadsheets/d/1FLtbJMfNi2f2aZh_9kaOx9lkPMNQXeujQpwJZmeSsWU/edit?gid=0#gid=0",
                "date": "2026-02-24"
        },
        {
                "id_employee": "EMP-0025",
                "timestamp": "2026-02-24 09:07:43.302000+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Natnael_EMP-0025/screenshot/Feb24/3fc0db32-639b-4618-9343-93138e00b4d1.webp",
                "app_name": "brave.exe",
                "window_title": "Warehouse inventory February 2026 - Google Sheets - Brave",
                "event": "APP_SWITCH",
                "url": "docs.google.com/spreadsheets/d/1FLtbJMfNi2f2aZh_9kaOx9lkPMNQXeujQpwJZmeSsWU/edit?gid=0#gid=0",
                "date": "2026-02-24"
        },
        {
                "id_employee": "EMP-0025",
                "timestamp": "2026-02-24 09:07:45.014000+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Natnael_EMP-0025/screenshot/Feb24/001e7c09-9b2c-4473-b164-a82db711bbee.webp",
                "app_name": "brave.exe",
                "window_title": "Warehouse inventory February 2026 - Google Sheets - Brave",
                "event": "TYPE",
                "url": "docs.google.com/spreadsheets/d/1FLtbJMfNi2f2aZh_9kaOx9lkPMNQXeujQpwJZmeSsWU/edit?gid=0#gid=0",
                "date": "2026-02-24"
        },
        {
                "id_employee": "EMP-0025",
                "timestamp": "2026-02-24 09:08:05.281281+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Natnael_EMP-0025/screenshot/Feb24/725ee434-9cae-4fbd-95cb-eab9b51e57da.webp",
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



