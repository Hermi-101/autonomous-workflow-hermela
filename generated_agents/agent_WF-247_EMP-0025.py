
import pyautogui
import time
import webbrowser
import os

# Generated Agent for Workflow: WF-247
# Employee: EMP-0025
# Pattern: Postman.exe:Custom_CLICK->Postman.exe:Custom_CLICK->Postman.exe:Custom_CLICK->Postman.exe:Custom_CLICK->Postman.exe:APP_SWITCH


def run_agent():
    print(f"--- Start Generated Agent for WF-247 ---")
    pyautogui.PAUSE = 1.0

    steps = [
        {
                "id_employee": "EMP-0025",
                "timestamp": "2026-02-24 05:00:25.716158+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Natnael_EMP-0025/screenshot/Feb24/1a18b38e-36ca-4c8f-a755-bb5f8cc39a6f.webp",
                "app_name": "Postman.exe",
                "window_title": "Update deal - My Workspace",
                "event": "Custom_CLICK",
                "url": "",
                "date": "2026-02-24"
        },
        {
                "id_employee": "EMP-0025",
                "timestamp": "2026-02-24 05:00:30.509827+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Natnael_EMP-0025/screenshot/Feb24/1b7db933-c4bd-4ef4-9761-f3dab70cff9a.webp",
                "app_name": "Postman.exe",
                "window_title": "product detail - My Workspace",
                "event": "Custom_CLICK",
                "url": "",
                "date": "2026-02-24"
        },
        {
                "id_employee": "EMP-0025",
                "timestamp": "2026-02-24 05:00:33.480179+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Natnael_EMP-0025/screenshot/Feb24/ed60c2d7-0b0c-4cf4-81e2-ecbc849d15e9.webp",
                "app_name": "Postman.exe",
                "window_title": "product detail - My Workspace",
                "event": "Custom_CLICK",
                "url": "",
                "date": "2026-02-24"
        },
        {
                "id_employee": "EMP-0025",
                "timestamp": "2026-02-24 05:00:36.797924+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Natnael_EMP-0025/screenshot/Feb24/20509cb2-68f7-49ab-8293-528a1b062a6e.webp",
                "app_name": "Postman.exe",
                "window_title": "product detail - My Workspace",
                "event": "Custom_CLICK",
                "url": "",
                "date": "2026-02-24"
        },
        {
                "id_employee": "EMP-0025",
                "timestamp": "2026-02-24 05:00:37.291000+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Natnael_EMP-0025/screenshot/Feb24/a83ce4a6-1b22-4ffa-9301-f00a6767e9f0.webp",
                "app_name": "Postman.exe",
                "window_title": "Update deal - My Workspace",
                "event": "APP_SWITCH",
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



