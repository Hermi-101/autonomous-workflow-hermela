
import pyautogui
import time
import webbrowser
import os

# Generated Agent for Workflow: WF-013
# Employee: EMP-0025
# Pattern: brave.exe:Custom_CLICK->brave.exe:Custom_CLICK->brave.exe:APP_SWITCH->brave.exe:TYPE->brave.exe:TYPE


def run_agent():
    print(f"--- Start Generated Agent for WF-013 ---")
    pyautogui.PAUSE = 1.0

    steps = [
        {
                "id_employee": "EMP-0025",
                "timestamp": "2026-02-23 06:52:46.481012+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Natnael_EMP-0025/screenshot/Feb23/23a16eb3-709c-4356-933a-eb7383e4da6d.webp",
                "app_name": "brave.exe",
                "window_title": "Superset - Brave",
                "event": "Custom_CLICK",
                "url": "64.227.129.135:8088/login/?next=http://64.227.129.135:8088/sqllab/",
                "date": "2026-02-23"
        },
        {
                "id_employee": "EMP-0025",
                "timestamp": "2026-02-23 06:52:48.391152+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Natnael_EMP-0025/screenshot/Feb23/36d793af-8521-438b-95a4-d7a036e04f4c.webp",
                "app_name": "brave.exe",
                "window_title": "Superset - Brave",
                "event": "Custom_CLICK",
                "url": "",
                "date": "2026-02-23"
        },
        {
                "id_employee": "EMP-0025",
                "timestamp": "2026-02-23 06:52:49.350000+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Natnael_EMP-0025/screenshot/Feb23/049e379c-8f2d-44d0-9c85-024b191107e7.webp",
                "app_name": "brave.exe",
                "window_title": "YouTube - (624) Bad Bunny Bowl Breakdown: The Politics & Powers over Puerto Rico - YouTube",
                "event": "APP_SWITCH",
                "url": "youtube.com/watch?v=0TQDxoSNikI",
                "date": "2026-02-23"
        },
        {
                "id_employee": "EMP-0025",
                "timestamp": "2026-02-23 06:52:50.015000+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Natnael_EMP-0025/screenshot/Feb23/b3c04e5c-d405-4fa3-b3f6-ee86f1d0c168.webp",
                "app_name": "brave.exe",
                "window_title": "YouTube - (624) Bad Bunny Bowl Breakdown: The Politics & Powers over Puerto Rico - YouTube",
                "event": "TYPE",
                "url": "youtube.com/watch?v=0TQDxoSNikI",
                "date": "2026-02-23"
        },
        {
                "id_employee": "EMP-0025",
                "timestamp": "2026-02-23 06:52:55.009000+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Natnael_EMP-0025/screenshot/Feb23/4c21c3fd-c89b-4a8c-b0df-983a2c463a23.webp",
                "app_name": "brave.exe",
                "window_title": "Superset - Brave",
                "event": "TYPE",
                "url": "64.227.129.135:8088/dashboard/list/?pageIndex=0&sortColumn=changed_on_delta_humanized&sortOrder=desc&viewMode=table",
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



