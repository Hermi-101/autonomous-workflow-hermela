
import pyautogui
import time
import webbrowser
import os

# Generated Agent for Workflow: WF-231
# Employee: EMP-0025
# Pattern: Postman.exe:Custom_CLICK->Postman.exe:Custom_CLICK->Postman.exe:Custom_CLICK->Postman.exe:Custom_COPY_ACTION->Postman.exe:Custom_CLICK


def run_agent():
    print(f"--- Start Generated Agent for WF-231 ---")
    pyautogui.PAUSE = 1.0

    steps = [
        {
                "id_employee": "EMP-0025",
                "timestamp": "2026-02-23 16:21:27.321620+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Natnael_EMP-0025/screenshot/Feb23/62ad41b9-f19b-4030-a12e-d6fa517fbfaa.webp",
                "app_name": "Postman.exe",
                "window_title": "Update deal - My Workspace",
                "event": "Custom_CLICK",
                "url": "",
                "date": "2026-02-23"
        },
        {
                "id_employee": "EMP-0025",
                "timestamp": "2026-02-23 16:21:30.973279+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Natnael_EMP-0025/screenshot/Feb23/d680bff7-c005-436e-938d-f73868cb5d5c.webp",
                "app_name": "Postman.exe",
                "window_title": "Update deal - My Workspace",
                "event": "Custom_CLICK",
                "url": "",
                "date": "2026-02-23"
        },
        {
                "id_employee": "EMP-0025",
                "timestamp": "2026-02-23 16:21:34.334646+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Natnael_EMP-0025/screenshot/Feb23/4ce51f66-9929-4d71-b802-d086058a1c89.webp",
                "app_name": "Postman.exe",
                "window_title": "product detail - My Workspace",
                "event": "Custom_CLICK",
                "url": "",
                "date": "2026-02-23"
        },
        {
                "id_employee": "EMP-0025",
                "timestamp": "2026-02-23 16:21:37.482454+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Natnael_EMP-0025/screenshot/Feb23/51aa1c05-a83f-4df0-99d2-f42b93ea02ab.webp",
                "app_name": "Postman.exe",
                "window_title": "product detail - My Workspace",
                "event": "Custom_COPY_ACTION",
                "url": "",
                "date": "2026-02-23"
        },
        {
                "id_employee": "EMP-0025",
                "timestamp": "2026-02-23 16:21:38.876961+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Natnael_EMP-0025/screenshot/Feb23/1a34bfa3-be0a-4641-bda5-378c4ab44fc4.webp",
                "app_name": "Postman.exe",
                "window_title": "product detail - My Workspace",
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



