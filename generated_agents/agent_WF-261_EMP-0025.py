
import pyautogui
import time
import webbrowser
import os

# Generated Agent for Workflow: WF-261
# Employee: EMP-0025
# Pattern: Postman.exe:Custom_CLICK->Postman.exe:APP_SWITCH->Postman.exe:Custom_CLICK->Postman.exe:APP_SWITCH->Postman.exe:TYPE


def run_agent():
    print(f"--- Start Generated Agent for WF-261 ---")
    pyautogui.PAUSE = 1.0

    steps = [
        {
                "id_employee": "EMP-0025",
                "timestamp": "2026-02-24 05:17:38.353259+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Natnael_EMP-0025/screenshot/Feb24/926f7ed1-209b-4feb-9e4e-1bc64c444255.webp",
                "app_name": "Postman.exe",
                "window_title": "product detail - My Workspace",
                "event": "Custom_CLICK",
                "url": "",
                "date": "2026-02-24"
        },
        {
                "id_employee": "EMP-0025",
                "timestamp": "2026-02-24 05:17:38.823000+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Natnael_EMP-0025/screenshot/Feb24/cccde7a9-db36-4189-9e79-dc0f703e59f4.webp",
                "app_name": "Postman.exe",
                "window_title": "Update deal - My Workspace",
                "event": "APP_SWITCH",
                "url": "",
                "date": "2026-02-24"
        },
        {
                "id_employee": "EMP-0025",
                "timestamp": "2026-02-24 05:17:39.384609+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Natnael_EMP-0025/screenshot/Feb24/089d2010-1e91-42f8-8f2b-3630aa636ebb.webp",
                "app_name": "Postman.exe",
                "window_title": "Update deal - My Workspace",
                "event": "Custom_CLICK",
                "url": "",
                "date": "2026-02-24"
        },
        {
                "id_employee": "EMP-0025",
                "timestamp": "2026-02-24 05:17:48.066000+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Natnael_EMP-0025/screenshot/Feb24/4d22655e-9f0a-4572-ac62-e6f748979bee.webp",
                "app_name": "Postman.exe",
                "window_title": "product detail - My Workspace",
                "event": "APP_SWITCH",
                "url": "",
                "date": "2026-02-24"
        },
        {
                "id_employee": "EMP-0025",
                "timestamp": "2026-02-24 05:17:50.002000+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Natnael_EMP-0025/screenshot/Feb24/055d323b-6484-4cf1-867a-b2c90058f962.webp",
                "app_name": "Postman.exe",
                "window_title": "Update deal - My Workspace",
                "event": "TYPE",
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



