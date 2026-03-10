
import pyautogui
import time
import webbrowser
import os

# Generated Agent for Workflow: WF-241
# Employee: EMP-0025
# Pattern: Postman.exe:Custom_CLICK->Postman.exe:TYPE->Postman.exe:TYPE->Postman.exe:Custom_CLICK->Postman.exe:Custom_CLICK


def run_agent():
    print(f"--- Start Generated Agent for WF-241 ---")
    pyautogui.PAUSE = 1.0

    steps = [
        {
                "id_employee": "EMP-0025",
                "timestamp": "2026-02-24 04:53:39.072598+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Natnael_EMP-0025/screenshot/Feb24/5c427b83-b14a-42fb-90f3-2ca230e22fd2.webp",
                "app_name": "Postman.exe",
                "window_title": "product detail - My Workspace",
                "event": "Custom_CLICK",
                "url": "",
                "date": "2026-02-24"
        },
        {
                "id_employee": "EMP-0025",
                "timestamp": "2026-02-24 04:53:40.013000+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Natnael_EMP-0025/screenshot/Feb24/b1d41e81-e733-4baa-99ce-8e3adfa00056.webp",
                "app_name": "Postman.exe",
                "window_title": "product detail - My Workspace",
                "event": "TYPE",
                "url": "",
                "date": "2026-02-24"
        },
        {
                "id_employee": "EMP-0025",
                "timestamp": "2026-02-24 04:53:45.004000+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Natnael_EMP-0025/screenshot/Feb24/c7e7b476-3825-4cf6-a3a9-8cb8cd49e598.webp",
                "app_name": "Postman.exe",
                "window_title": "Update deal - My Workspace",
                "event": "TYPE",
                "url": "",
                "date": "2026-02-24"
        },
        {
                "id_employee": "EMP-0025",
                "timestamp": "2026-02-24 04:53:45.158650+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Natnael_EMP-0025/screenshot/Feb24/728c6063-84d6-48f1-b933-5b8a78f05a8a.webp",
                "app_name": "Postman.exe",
                "window_title": "product detail - My Workspace",
                "event": "Custom_CLICK",
                "url": "",
                "date": "2026-02-24"
        },
        {
                "id_employee": "EMP-0025",
                "timestamp": "2026-02-24 04:53:50.854696+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Natnael_EMP-0025/screenshot/Feb24/17dfa02d-3102-4718-8393-0adade105ba7.webp",
                "app_name": "Postman.exe",
                "window_title": "product detail - My Workspace",
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



