
import pyautogui
import time
import webbrowser
import os

# Generated Agent for Workflow: WF-279
# Employee: EMP-0025
# Pattern: Postman.exe:Custom_CLICK->Postman.exe:CLICK->Postman.exe:Custom_CLICK->Postman.exe:Custom_CLICK->Postman.exe:MOVE


def run_agent():
    print(f"--- Start Generated Agent for WF-279 ---")
    pyautogui.PAUSE = 1.0

    steps = [
        {
                "id_employee": "EMP-0025",
                "timestamp": "2026-02-24 06:51:09.558488+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Natnael_EMP-0025/screenshot/Feb24/5d4014de-b5d0-4048-83d3-cf3c75cbef9e.webp",
                "app_name": "Postman.exe",
                "window_title": "list product variations with sku, product name, product id, variation id, and attributes - My Workspace",
                "event": "Custom_CLICK",
                "url": "",
                "date": "2026-02-24"
        },
        {
                "id_employee": "EMP-0025",
                "timestamp": "2026-02-24 06:53:55.009000+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Natnael_EMP-0025/screenshot/Feb24/7f75d06c-b0be-420d-a045-651b56d1b1a3.webp",
                "app_name": "Postman.exe",
                "window_title": "product list - My Workspace",
                "event": "CLICK",
                "url": "",
                "date": "2026-02-24"
        },
        {
                "id_employee": "EMP-0025",
                "timestamp": "2026-02-24 06:53:57.833943+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Natnael_EMP-0025/screenshot/Feb24/533b3eee-4eef-4965-bf1f-6f493145f4dd.webp",
                "app_name": "Postman.exe",
                "window_title": "list warehouse received products - My Workspace",
                "event": "Custom_CLICK",
                "url": "",
                "date": "2026-02-24"
        },
        {
                "id_employee": "EMP-0025",
                "timestamp": "2026-02-24 06:54:00.265729+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Natnael_EMP-0025/screenshot/Feb24/b823f1e7-2ad1-48ba-bcf8-38d130ef08cc.webp",
                "app_name": "Postman.exe",
                "window_title": "product list - My Workspace",
                "event": "Custom_CLICK",
                "url": "",
                "date": "2026-02-24"
        },
        {
                "id_employee": "EMP-0025",
                "timestamp": "2026-02-24 06:54:20.014000+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Natnael_EMP-0025/screenshot/Feb24/261a5484-10ae-4e5d-9ceb-580d7edcb699.webp",
                "app_name": "Postman.exe",
                "window_title": "product list - My Workspace",
                "event": "MOVE",
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



