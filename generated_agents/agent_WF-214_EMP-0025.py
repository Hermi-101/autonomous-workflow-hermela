
import pyautogui
import time
import webbrowser
import os

# Generated Agent for Workflow: WF-214
# Employee: EMP-0025
# Pattern: brave.exe:Custom_CLICK->Postman.exe:Custom_CLICK->Postman.exe:Custom_CLICK->Postman.exe:Custom_CLICK->Postman.exe:Custom_CLICK


def run_agent():
    print(f"--- Start Generated Agent for WF-214 ---")
    pyautogui.PAUSE = 1.0

    steps = [
        {
                "id_employee": "EMP-0025",
                "timestamp": "2026-02-23 11:26:35.686054+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Natnael_EMP-0025/screenshot/Feb23/fbb0e6f2-9aa9-4d8f-990d-0e820dccad66.webp",
                "app_name": "brave.exe",
                "window_title": "Swagger UI - Brave",
                "event": "Custom_CLICK",
                "url": "stagingapi.chipchip.social/swagger/index.html#/",
                "date": "2026-02-23"
        },
        {
                "id_employee": "EMP-0025",
                "timestamp": "2026-02-23 11:26:41.870092+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Natnael_EMP-0025/screenshot/Feb23/4537283a-f815-43df-9148-9ca6068f65bf.webp",
                "app_name": "Postman.exe",
                "window_title": "list benchmark products - My Workspace",
                "event": "Custom_CLICK",
                "url": "",
                "date": "2026-02-23"
        },
        {
                "id_employee": "EMP-0025",
                "timestamp": "2026-02-23 11:26:45.176415+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Natnael_EMP-0025/screenshot/Feb23/2af55155-6337-4f2c-b989-071bbad29617.webp",
                "app_name": "Postman.exe",
                "window_title": "list benchmark products - My Workspace",
                "event": "Custom_CLICK",
                "url": "",
                "date": "2026-02-23"
        },
        {
                "id_employee": "EMP-0025",
                "timestamp": "2026-02-23 11:27:52.550387+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Natnael_EMP-0025/screenshot/Feb23/f0569dd1-7f73-4874-b244-998e34cda1b4.webp",
                "app_name": "Postman.exe",
                "window_title": "list benchmark products - My Workspace",
                "event": "Custom_CLICK",
                "url": "",
                "date": "2026-02-23"
        },
        {
                "id_employee": "EMP-0025",
                "timestamp": "2026-02-23 11:27:56.027970+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Natnael_EMP-0025/screenshot/Feb23/44fd741b-7846-4f84-9b4f-feff56461b52.webp",
                "app_name": "Postman.exe",
                "window_title": "create warehouse received product - My Workspace",
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



