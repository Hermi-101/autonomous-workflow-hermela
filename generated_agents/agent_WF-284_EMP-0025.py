
import pyautogui
import time
import webbrowser
import os

# Generated Agent for Workflow: WF-284
# Employee: EMP-0025
# Pattern: brave.exe:MOVE->brave.exe:Custom_CLICK->brave.exe:Custom_CLICK->brave.exe:TYPE->brave.exe:TYPE


def run_agent():
    print(f"--- Start Generated Agent for WF-284 ---")
    pyautogui.PAUSE = 1.0

    steps = [
        {
                "id_employee": "EMP-0025",
                "timestamp": "2026-02-24 08:09:00.013000+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Natnael_EMP-0025/screenshot/Feb24/8e2647e7-1b55-40c2-a2de-386917bf20b3.webp",
                "app_name": "brave.exe",
                "window_title": "Superset - Brave",
                "event": "MOVE",
                "url": "64.227.129.135:8088/sqllab/",
                "date": "2026-02-24"
        },
        {
                "id_employee": "EMP-0025",
                "timestamp": "2026-02-24 08:09:17.720960+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Natnael_EMP-0025/screenshot/Feb24/59490787-a350-4fa6-8242-d167c4dee100.webp",
                "app_name": "brave.exe",
                "window_title": "Superset - Brave",
                "event": "Custom_CLICK",
                "url": "64.227.129.135:8088/sqllab/",
                "date": "2026-02-24"
        },
        {
                "id_employee": "EMP-0025",
                "timestamp": "2026-02-24 08:09:22.038022+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Natnael_EMP-0025/screenshot/Feb24/35263fd7-c2eb-4b6d-8504-da0c4dcd49eb.webp",
                "app_name": "brave.exe",
                "window_title": "Superset - Brave",
                "event": "Custom_CLICK",
                "url": "64.227.129.135:8088/sqllab/",
                "date": "2026-02-24"
        },
        {
                "id_employee": "EMP-0025",
                "timestamp": "2026-02-24 08:09:25.008000+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Natnael_EMP-0025/screenshot/Feb24/77e4ca23-a766-4fc5-bf72-3b1c47782c03.webp",
                "app_name": "brave.exe",
                "window_title": "Superset - Brave",
                "event": "TYPE",
                "url": "64.227.129.135:8088/sqllab/",
                "date": "2026-02-24"
        },
        {
                "id_employee": "EMP-0025",
                "timestamp": "2026-02-24 08:09:30.001000+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Natnael_EMP-0025/screenshot/Feb24/0b020180-0d77-4095-a3ee-aa5129c758ff.webp",
                "app_name": "brave.exe",
                "window_title": "Superset - Brave",
                "event": "TYPE",
                "url": "64.227.129.135:8088/sqllab/",
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



