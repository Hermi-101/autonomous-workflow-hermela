
import pyautogui
import time
import webbrowser
import os

# Generated Agent for Workflow: WF-627
# Employee: EMP-0053
# Pattern: chrome.exe:Custom_CLICK->chrome.exe:CLICK->chrome.exe:Custom_CLICK->chrome.exe:Custom_CLICK->chrome.exe:MOVE


def run_agent():
    print(f"--- Start Generated Agent for WF-627 ---")
    pyautogui.PAUSE = 1.0

    steps = [
        {
                "id_employee": "EMP-0053",
                "timestamp": "2026-02-23 09:38:47.869508+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Betelhem_EMP-0053/screenshot/Feb23/0033181f-07a6-4f3b-8e29-ca80eeb22710.webp",
                "app_name": "chrome.exe",
                "window_title": "Reports - Google Chrome",
                "event": "Custom_CLICK",
                "url": "admin.ringcloud.et/reports",
                "date": "2026-02-23"
        },
        {
                "id_employee": "EMP-0053",
                "timestamp": "2026-02-23 09:38:50.011000+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Betelhem_EMP-0053/screenshot/Feb23/1c13a35d-12ff-4999-8a46-189cacc54103.webp",
                "app_name": "chrome.exe",
                "window_title": "Reports - Google Chrome",
                "event": "CLICK",
                "url": "admin.ringcloud.et/reports",
                "date": "2026-02-23"
        },
        {
                "id_employee": "EMP-0053",
                "timestamp": "2026-02-23 09:38:52.551105+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Betelhem_EMP-0053/screenshot/Feb23/96d68206-3249-4dd0-80b1-44d880f35ef1.webp",
                "app_name": "chrome.exe",
                "window_title": "Reports - Google Chrome",
                "event": "Custom_CLICK",
                "url": "admin.ringcloud.et/reports",
                "date": "2026-02-23"
        },
        {
                "id_employee": "EMP-0053",
                "timestamp": "2026-02-23 09:38:54.262522+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Betelhem_EMP-0053/screenshot/Feb23/431394e7-2567-4dd4-8525-7ad4c0d5241c.webp",
                "app_name": "chrome.exe",
                "window_title": "Reports - Google Chrome",
                "event": "Custom_CLICK",
                "url": "admin.ringcloud.et/reports",
                "date": "2026-02-23"
        },
        {
                "id_employee": "EMP-0053",
                "timestamp": "2026-02-23 09:39:10.012000+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Betelhem_EMP-0053/screenshot/Feb23/e71831e9-ffd4-4b59-ace4-1cd7ff39aaf5.webp",
                "app_name": "chrome.exe",
                "window_title": "Reports - Google Chrome",
                "event": "MOVE",
                "url": "admin.ringcloud.et/reports",
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



