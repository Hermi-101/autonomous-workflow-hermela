
import pyautogui
import time
import webbrowser
import os

# Generated Agent for Workflow: WF-686
# Employee: EMP-0053
# Pattern: chrome.exe:Custom_CLICK->chrome.exe:APP_SWITCH->chrome.exe:Custom_CLICK->chrome.exe:APP_SWITCH->chrome.exe:Custom_CLICK


def run_agent():
    print(f"--- Start Generated Agent for WF-686 ---")
    pyautogui.PAUSE = 1.0

    steps = [
        {
                "id_employee": "EMP-0053",
                "timestamp": "2026-02-23 14:54:52.622129+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Betelhem_EMP-0053/screenshot/Feb23/5223ef9a-6c2b-48a9-8078-ae890bfea6fa.webp",
                "app_name": "chrome.exe",
                "window_title": "Call rating - Google Chrome",
                "event": "Custom_CLICK",
                "url": "drive.google.com/u/0/open?id=1Cmk55CPBPd8EtEE9J6cqiDMG9gTAjuNp&usp=forms_web",
                "date": "2026-02-23"
        },
        {
                "id_employee": "EMP-0053",
                "timestamp": "2026-02-23 14:54:52.933000+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Betelhem_EMP-0053/screenshot/Feb23/3ba96f74-3138-4006-bdf4-97dc93f4b550.webp",
                "app_name": "chrome.exe",
                "window_title": "Untitled - Google Chrome",
                "event": "APP_SWITCH",
                "url": "drive.google.com/file/d/1Cmk55CPBPd8EtEE9J6cqiDMG9gTAjuNp/view",
                "date": "2026-02-23"
        },
        {
                "id_employee": "EMP-0053",
                "timestamp": "2026-02-23 14:55:00.062369+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Betelhem_EMP-0053/screenshot/Feb23/2e2c0327-c4ab-4547-acc0-be92c5e821f4.webp",
                "app_name": "chrome.exe",
                "window_title": "1771602057.232392.m4a - Google Drive - Google Chrome",
                "event": "Custom_CLICK",
                "url": "docs.google.com/forms/d/e/1FAIpQLSfT7yNPzJDyJvzMrd4hfKuVdH8VDYydur6r0vdGD3ES__ZExA/viewform",
                "date": "2026-02-23"
        },
        {
                "id_employee": "EMP-0053",
                "timestamp": "2026-02-23 14:55:00.153000+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Betelhem_EMP-0053/screenshot/Feb23/412ec524-ab97-4e15-ac3e-4e831dbff74e.webp",
                "app_name": "chrome.exe",
                "window_title": "Call rating - Google Chrome",
                "event": "APP_SWITCH",
                "url": "docs.google.com/forms/d/e/1FAIpQLSfT7yNPzJDyJvzMrd4hfKuVdH8VDYydur6r0vdGD3ES__ZExA/viewform",
                "date": "2026-02-23"
        },
        {
                "id_employee": "EMP-0053",
                "timestamp": "2026-02-23 14:55:03.842107+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Betelhem_EMP-0053/screenshot/Feb23/b2c7631b-1f38-4d36-bea0-32b588330fad.webp",
                "app_name": "chrome.exe",
                "window_title": "Call rating - Google Chrome",
                "event": "Custom_CLICK",
                "url": "docs.google.com/forms/d/e/1FAIpQLSfT7yNPzJDyJvzMrd4hfKuVdH8VDYydur6r0vdGD3ES__ZExA/viewform",
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



