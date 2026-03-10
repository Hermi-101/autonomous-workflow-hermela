
import pyautogui
import time
import webbrowser
import os

# Generated Agent for Workflow: WF-309
# Employee: EMP-0025
# Pattern: Postman.exe:TYPE->Postman.exe:Custom_CLICK->Postman.exe:Custom_CLICK->Postman.exe:CLICK->Postman.exe:Custom_CLICK


def run_agent():
    print(f"--- Start Generated Agent for WF-309 ---")
    pyautogui.PAUSE = 1.0

    steps = [
        {
                "id_employee": "EMP-0025",
                "timestamp": "2026-02-24 11:20:30.006000+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Natnael_EMP-0025/screenshot/Feb24/f7165604-36ce-474b-bb0b-335363ae28da.webp",
                "app_name": "Postman.exe",
                "window_title": "create warehouse received product - My Workspace",
                "event": "TYPE",
                "url": "",
                "date": "2026-02-24"
        },
        {
                "id_employee": "EMP-0025",
                "timestamp": "2026-02-24 11:20:31.453616+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Natnael_EMP-0025/screenshot/Feb24/769d3787-2b9b-4232-ab9e-a941f6e16d8a.webp",
                "app_name": "Postman.exe",
                "window_title": "create warehouse received product - My Workspace",
                "event": "Custom_CLICK",
                "url": "",
                "date": "2026-02-24"
        },
        {
                "id_employee": "EMP-0025",
                "timestamp": "2026-02-24 11:20:38.155819+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Natnael_EMP-0025/screenshot/Feb24/b8b59a36-c394-4459-9bfb-ad74f74b494b.webp",
                "app_name": "Postman.exe",
                "window_title": "create warehouse received product - My Workspace",
                "event": "Custom_CLICK",
                "url": "",
                "date": "2026-02-24"
        },
        {
                "id_employee": "EMP-0025",
                "timestamp": "2026-02-24 11:20:45.015000+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Natnael_EMP-0025/screenshot/Feb24/ef410c6b-e7b5-4efe-a832-357017bce8f1.webp",
                "app_name": "Postman.exe",
                "window_title": "create product stock batch - My Workspace",
                "event": "CLICK",
                "url": "",
                "date": "2026-02-24"
        },
        {
                "id_employee": "EMP-0025",
                "timestamp": "2026-02-24 11:20:47.135161+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Natnael_EMP-0025/screenshot/Feb24/12e89915-513f-4727-a1cb-ea899bf27801.webp",
                "app_name": "Postman.exe",
                "window_title": "create warehouse received product - My Workspace",
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



