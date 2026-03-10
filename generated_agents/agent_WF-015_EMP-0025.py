
import pyautogui
import time
import webbrowser
import os

# Generated Agent for Workflow: WF-015
# Employee: EMP-0025
# Pattern: explorer.exe:APP_SWITCH->brave.exe:APP_SWITCH->brave.exe:CLICK->brave.exe:Custom_CLICK->brave.exe:CLICK


def run_agent():
    print(f"--- Start Generated Agent for WF-015 ---")
    pyautogui.PAUSE = 1.0

    steps = [
        {
                "id_employee": "EMP-0025",
                "timestamp": "2026-02-23 06:53:53.095000+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Natnael_EMP-0025/screenshot/Feb23/deefcf90-4ecb-40d5-a19a-4efd9bf6b8d1.webp",
                "app_name": "explorer.exe",
                "window_title": "New Tab - Brave",
                "event": "APP_SWITCH",
                "url": "",
                "date": "2026-02-23"
        },
        {
                "id_employee": "EMP-0025",
                "timestamp": "2026-02-23 06:54:02.329000+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Natnael_EMP-0025/screenshot/Feb23/a68ef4e7-bd8e-40b2-800f-9d221887e78f.webp",
                "app_name": "brave.exe",
                "window_title": "New Tab - Brave",
                "event": "APP_SWITCH",
                "url": "docs.google.com/spreadsheets/d/1lNOXGpxug27xOOkdrPO8ZD69-i-8gpE26ixhZEZJHT8/edit?gid=375857456#gid=375857456",
                "date": "2026-02-23"
        },
        {
                "id_employee": "EMP-0025",
                "timestamp": "2026-02-23 06:54:05.015000+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Natnael_EMP-0025/screenshot/Feb23/296d707b-3e0b-4725-b45a-2e75ce48716b.webp",
                "app_name": "brave.exe",
                "window_title": "expected bag usage - Google Sheets - Brave",
                "event": "CLICK",
                "url": "docs.google.com/spreadsheets/d/1lNOXGpxug27xOOkdrPO8ZD69-i-8gpE26ixhZEZJHT8/edit?gid=375857456#gid=375857456",
                "date": "2026-02-23"
        },
        {
                "id_employee": "EMP-0025",
                "timestamp": "2026-02-23 06:54:05.132784+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Natnael_EMP-0025/screenshot/Feb23/94b99930-815e-4a2b-b8a8-5dc856348814.webp",
                "app_name": "brave.exe",
                "window_title": "New Tab - Brave",
                "event": "Custom_CLICK",
                "url": "docs.google.com/spreadsheets/d/1lNOXGpxug27xOOkdrPO8ZD69-i-8gpE26ixhZEZJHT8/edit?gid=375857456#gid=375857456",
                "date": "2026-02-23"
        },
        {
                "id_employee": "EMP-0025",
                "timestamp": "2026-02-23 06:54:10.012000+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Natnael_EMP-0025/screenshot/Feb23/92250d89-9169-4c89-b7e7-331f366f042c.webp",
                "app_name": "brave.exe",
                "window_title": "Fix of warehouse - Google Sheets - Brave",
                "event": "CLICK",
                "url": "docs.google.com/spreadsheets/d/1UByYg7_GMjNIqjoXEcNezc2bNfnSVuOU8japFLXceUU/edit?gid=895107596#gid=895107596",
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



