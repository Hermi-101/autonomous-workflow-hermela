
import pyautogui
import time
import webbrowser
import os

# Generated Agent for Workflow: WF-010
# Employee: EMP-0025
# Pattern: brave.exe:APP_SWITCH->brave.exe:TYPE->brave.exe:CLICK->brave.exe:Custom_CLICK->brave.exe:Custom_CLICK


def run_agent():
    print(f"--- Start Generated Agent for WF-010 ---")
    pyautogui.PAUSE = 1.0

    steps = [
        {
                "id_employee": "EMP-0025",
                "timestamp": "2026-02-23 06:52:36.026000+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Natnael_EMP-0025/screenshot/Feb23/46350e6c-391c-44c4-96fb-e52077a6f0c5.webp",
                "app_name": "brave.exe",
                "window_title": "New Tab - Brave",
                "event": "APP_SWITCH",
                "url": "64.227.129.135:8088/login/?next=http://64.227.129.135:8088/sqllab/",
                "date": "2026-02-23"
        },
        {
                "id_employee": "EMP-0025",
                "timestamp": "2026-02-23 06:52:40.002000+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Natnael_EMP-0025/screenshot/Feb23/f24acdbb-f64f-42e2-a242-7ec012bd3f9a.webp",
                "app_name": "brave.exe",
                "window_title": "YouTube - (624) Bad Bunny Bowl Breakdown: The Politics & Powers over Puerto Rico - YouTube",
                "event": "TYPE",
                "url": "youtube.com/watch?v=0TQDxoSNikI",
                "date": "2026-02-23"
        },
        {
                "id_employee": "EMP-0025",
                "timestamp": "2026-02-23 06:52:45.010000+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Natnael_EMP-0025/screenshot/Feb23/1695402e-ec0c-41d3-8995-d072341814d0.webp",
                "app_name": "brave.exe",
                "window_title": "YouTube - (624) Bad Bunny Bowl Breakdown: The Politics & Powers over Puerto Rico - YouTube",
                "event": "CLICK",
                "url": "youtube.com/watch?v=0TQDxoSNikI",
                "date": "2026-02-23"
        },
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



