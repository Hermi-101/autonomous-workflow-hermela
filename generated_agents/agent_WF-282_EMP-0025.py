
import pyautogui
import time
import webbrowser
import os

# Generated Agent for Workflow: WF-282
# Employee: EMP-0025
# Pattern: Telegram.exe:TYPE->brave.exe:CLICK->Telegram.exe:Custom_CLICK->Telegram.exe:APP_SWITCH->Telegram.exe:Custom_CLICK


def run_agent():
    print(f"--- Start Generated Agent for WF-282 ---")
    pyautogui.PAUSE = 1.0

    steps = [
        {
                "id_employee": "EMP-0025",
                "timestamp": "2026-02-24 07:53:15.012000+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Natnael_EMP-0025/screenshot/Feb24/320e6e5c-8082-4f84-8e00-68c1721df80f.webp",
                "app_name": "Telegram.exe",
                "window_title": "\u200eBruk @ \u200eNA (6921)",
                "event": "TYPE",
                "url": "",
                "date": "2026-02-24"
        },
        {
                "id_employee": "EMP-0025",
                "timestamp": "2026-02-24 07:53:35+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Natnael_EMP-0025/screenshot/Feb24/db7e673b-4899-41e7-8d9d-557e01cd1b41.webp",
                "app_name": "brave.exe",
                "window_title": "Superset - Brave",
                "event": "CLICK",
                "url": "64.227.129.135:8088/sqllab/",
                "date": "2026-02-24"
        },
        {
                "id_employee": "EMP-0025",
                "timestamp": "2026-02-24 07:53:39.031882+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Natnael_EMP-0025/screenshot/Feb24/ee316c59-aea2-46fc-920e-aeaa9ed8ba70.webp",
                "app_name": "Telegram.exe",
                "window_title": "\u200eBruk @ \u200eNA (6921)",
                "event": "Custom_CLICK",
                "url": "",
                "date": "2026-02-24"
        },
        {
                "id_employee": "EMP-0025",
                "timestamp": "2026-02-24 07:53:49.926000+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Natnael_EMP-0025/screenshot/Feb24/5d7c13fa-eb1a-4f8a-b821-cc417b782918.webp",
                "app_name": "Telegram.exe",
                "window_title": "\u200eBruk @ \u200eNA (6921)",
                "event": "APP_SWITCH",
                "url": "",
                "date": "2026-02-24"
        },
        {
                "id_employee": "EMP-0025",
                "timestamp": "2026-02-24 07:53:50.352240+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Natnael_EMP-0025/screenshot/Feb24/70941685-feaf-4ce7-af1d-dad20ba1bb76.webp",
                "app_name": "Telegram.exe",
                "window_title": "\u200eBruk @ \u200eNA (6921)",
                "event": "Custom_CLICK",
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



