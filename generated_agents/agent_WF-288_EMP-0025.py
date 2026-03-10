
import pyautogui
import time
import webbrowser
import os

# Generated Agent for Workflow: WF-288
# Employee: EMP-0025
# Pattern: Postman.exe:Custom_CLICK->Postman.exe:Custom_CLICK->Postman.exe:APP_SWITCH->Postman.exe:APP_SWITCH->Postman.exe:TYPE


def run_agent():
    print(f"--- Start Generated Agent for WF-288 ---")
    pyautogui.PAUSE = 1.0

    steps = [
        {
                "id_employee": "EMP-0025",
                "timestamp": "2026-02-24 08:25:51.006665+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Natnael_EMP-0025/screenshot/Feb24/658c69e3-2bee-473b-ac25-002873bda972.webp",
                "app_name": "Postman.exe",
                "window_title": "New Request - My Workspace",
                "event": "Custom_CLICK",
                "url": "",
                "date": "2026-02-24"
        },
        {
                "id_employee": "EMP-0025",
                "timestamp": "2026-02-24 08:25:54.116103+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Natnael_EMP-0025/screenshot/Feb24/72e0fe95-e928-43c7-9987-3c5ad6dadf24.webp",
                "app_name": "Postman.exe",
                "window_title": "New Request - My Workspace",
                "event": "Custom_CLICK",
                "url": "",
                "date": "2026-02-24"
        },
        {
                "id_employee": "EMP-0025",
                "timestamp": "2026-02-24 08:25:55.770000+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Natnael_EMP-0025/screenshot/Feb24/1a93e2dc-59ad-44e9-9b51-84713621f143.webp",
                "app_name": "Postman.exe",
                "window_title": "Postman",
                "event": "APP_SWITCH",
                "url": "",
                "date": "2026-02-24"
        },
        {
                "id_employee": "EMP-0025",
                "timestamp": "2026-02-24 08:25:57.824000+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Natnael_EMP-0025/screenshot/Feb24/343c7035-8af2-470f-b1cf-bda58fa1fc14.webp",
                "app_name": "Postman.exe",
                "window_title": "New Request - My Workspace",
                "event": "APP_SWITCH",
                "url": "",
                "date": "2026-02-24"
        },
        {
                "id_employee": "EMP-0025",
                "timestamp": "2026-02-24 08:26:10.008000+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Natnael_EMP-0025/screenshot/Feb24/ebe9a466-1c33-4b50-923d-488412fc504c.webp",
                "app_name": "Postman.exe",
                "window_title": "order report - My Workspace",
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



