
import pyautogui
import time
import webbrowser
import os

# Generated Agent for Workflow: WF-237
# Employee: EMP-0025
# Pattern: brave.exe:Custom_CLICK->brave.exe:Custom_CLICK->Postman.exe:Custom_CLICK->brave.exe:Custom_CLICK->Postman.exe:Custom_CLICK


def run_agent():
    print(f"--- Start Generated Agent for WF-237 ---")
    pyautogui.PAUSE = 1.0

    steps = [
        {
                "id_employee": "EMP-0025",
                "timestamp": "2026-02-23 16:39:55.001895+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Natnael_EMP-0025/screenshot/Feb23/2e7612d3-d80e-49e6-9f85-09807a9b7a69.webp",
                "app_name": "brave.exe",
                "window_title": "YouTube - (624) Bad Bunny Bowl Breakdown: The Politics & Powers over Puerto Rico - YouTube",
                "event": "Custom_CLICK",
                "url": "youtube.com/watch?v=0TQDxoSNikI",
                "date": "2026-02-23"
        },
        {
                "id_employee": "EMP-0025",
                "timestamp": "2026-02-23 16:40:02.855185+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Natnael_EMP-0025/screenshot/Feb23/f338e999-887d-4395-b260-fe5c450e3435.webp",
                "app_name": "brave.exe",
                "window_title": "YouTube - (624) Bad Bunny Bowl Breakdown: The Politics & Powers over Puerto Rico - YouTube",
                "event": "Custom_CLICK",
                "url": "youtube.com/watch?v=0TQDxoSNikI",
                "date": "2026-02-23"
        },
        {
                "id_employee": "EMP-0025",
                "timestamp": "2026-02-23 16:40:11.431833+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Natnael_EMP-0025/screenshot/Feb23/bc409b10-60ea-42e8-8284-bc2c7b66fa7c.webp",
                "app_name": "Postman.exe",
                "window_title": "Update deal - My Workspace",
                "event": "Custom_CLICK",
                "url": "",
                "date": "2026-02-23"
        },
        {
                "id_employee": "EMP-0025",
                "timestamp": "2026-02-23 16:40:20.842574+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Natnael_EMP-0025/screenshot/Feb23/926cb909-2fab-49cf-bf7e-96746ce6ac1a.webp",
                "app_name": "brave.exe",
                "window_title": "Minimum KG - Google Sheets - Brave",
                "event": "Custom_CLICK",
                "url": "",
                "date": "2026-02-23"
        },
        {
                "id_employee": "EMP-0025",
                "timestamp": "2026-02-23 16:40:23.785836+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Natnael_EMP-0025/screenshot/Feb23/f73b7c7d-3e0d-4b19-91d8-76990eb3d078.webp",
                "app_name": "Postman.exe",
                "window_title": "Update deal - My Workspace",
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



