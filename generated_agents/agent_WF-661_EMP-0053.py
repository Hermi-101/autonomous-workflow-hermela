
import pyautogui
import time
import webbrowser
import os

# Generated Agent for Workflow: WF-661
# Employee: EMP-0053
# Pattern: chrome.exe:CLICK->chrome.exe:Custom_CLICK->chrome.exe:Custom_CLICK->chrome.exe:APP_SWITCH->chrome.exe:CLICK


def run_agent():
    print(f"--- Start Generated Agent for WF-661 ---")
    pyautogui.PAUSE = 1.0

    steps = [
        {
                "id_employee": "EMP-0053",
                "timestamp": "2026-02-23 12:40:55.015000+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Betelhem_EMP-0053/screenshot/Feb23/0329bd80-bb21-423b-8b11-8c85b33eae5a.webp",
                "app_name": "chrome.exe",
                "window_title": "Reports - Google Chrome",
                "event": "CLICK",
                "url": "admin.ringcloud.et/reports",
                "date": "2026-02-23"
        },
        {
                "id_employee": "EMP-0053",
                "timestamp": "2026-02-23 12:40:58.291263+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Betelhem_EMP-0053/screenshot/Feb23/e4481b79-d151-473e-8f7b-d7f597e8d1f0.webp",
                "app_name": "chrome.exe",
                "window_title": "Reports - Google Chrome",
                "event": "Custom_CLICK",
                "url": "admin.ringcloud.et/reports",
                "date": "2026-02-23"
        },
        {
                "id_employee": "EMP-0053",
                "timestamp": "2026-02-23 12:41:14.933096+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Betelhem_EMP-0053/screenshot/Feb23/ca5f703d-6b1e-4e02-9df5-cd855495c36d.webp",
                "app_name": "chrome.exe",
                "window_title": "Reports - Google Chrome",
                "event": "Custom_CLICK",
                "url": "docs.google.com/forms/u/0/d/e/1FAIpQLSfT7yNPzJDyJvzMrd4hfKuVdH8VDYydur6r0vdGD3ES__ZExA/formResponse",
                "date": "2026-02-23"
        },
        {
                "id_employee": "EMP-0053",
                "timestamp": "2026-02-23 12:41:15.096000+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Betelhem_EMP-0053/screenshot/Feb23/7684ae71-9bb2-4f81-9766-dd75fad653e0.webp",
                "app_name": "chrome.exe",
                "window_title": "Call rating - Google Chrome",
                "event": "APP_SWITCH",
                "url": "docs.google.com/forms/d/e/1FAIpQLSfT7yNPzJDyJvzMrd4hfKuVdH8VDYydur6r0vdGD3ES__ZExA/viewform",
                "date": "2026-02-23"
        },
        {
                "id_employee": "EMP-0053",
                "timestamp": "2026-02-23 12:41:20.001000+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Betelhem_EMP-0053/screenshot/Feb23/bbf0de04-2471-434f-9705-d4509da2cab0.webp",
                "app_name": "chrome.exe",
                "window_title": "Call rating - Google Chrome",
                "event": "CLICK",
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



