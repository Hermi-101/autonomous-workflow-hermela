
import pyautogui
import time
import webbrowser
import os

# Generated Agent for Workflow: WF-591
# Employee: EMP-0053
# Pattern: chrome.exe:Custom_CLICK->chrome.exe:Custom_CLICK->chrome.exe:Custom_CLICK->chrome.exe:TYPE->chrome.exe:Custom_CLICK


def run_agent():
    print(f"--- Start Generated Agent for WF-591 ---")
    pyautogui.PAUSE = 1.0

    steps = [
        {
                "id_employee": "EMP-0053",
                "timestamp": "2026-02-23 08:31:08.519784+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Betelhem_EMP-0053/screenshot/Feb23/f18f2cc2-2722-4dc1-8794-8d6b91fe858d.webp",
                "app_name": "chrome.exe",
                "window_title": "Refund - Google Sheets - Google Chrome",
                "event": "Custom_CLICK",
                "url": "docs.google.com/spreadsheets/d/1JH9H7e5Ng3vm6oBtKy9ykkrafwh-GykeNXhB77qRkLQ/edit?gid=654230300#gid=654230300",
                "date": "2026-02-23"
        },
        {
                "id_employee": "EMP-0053",
                "timestamp": "2026-02-23 08:31:12.453519+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Betelhem_EMP-0053/screenshot/Feb23/8ce5e95c-46d4-4d97-a0c9-6d8702ec71a8.webp",
                "app_name": "chrome.exe",
                "window_title": "Refund - Google Sheets - Google Chrome",
                "event": "Custom_CLICK",
                "url": "docs.google.com/spreadsheets/d/1JH9H7e5Ng3vm6oBtKy9ykkrafwh-GykeNXhB77qRkLQ/edit?gid=654230300#gid=654230300",
                "date": "2026-02-23"
        },
        {
                "id_employee": "EMP-0053",
                "timestamp": "2026-02-23 08:31:14.038143+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Betelhem_EMP-0053/screenshot/Feb23/fe5a9f93-674a-4bf6-8530-ae41afaa8abe.webp",
                "app_name": "chrome.exe",
                "window_title": "Refund - Google Sheets - Google Chrome",
                "event": "Custom_CLICK",
                "url": "docs.google.com/spreadsheets/d/1JH9H7e5Ng3vm6oBtKy9ykkrafwh-GykeNXhB77qRkLQ/edit?gid=654230300#gid=654230300",
                "date": "2026-02-23"
        },
        {
                "id_employee": "EMP-0053",
                "timestamp": "2026-02-23 08:33:25+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Betelhem_EMP-0053/screenshot/Feb23/d423e294-4083-4ab2-a98d-a8e8421f9c5e.webp",
                "app_name": "chrome.exe",
                "window_title": "Refund - Google Sheets - Google Chrome",
                "event": "TYPE",
                "url": "docs.google.com/spreadsheets/d/1JH9H7e5Ng3vm6oBtKy9ykkrafwh-GykeNXhB77qRkLQ/edit?gid=654230300#gid=654230300",
                "date": "2026-02-23"
        },
        {
                "id_employee": "EMP-0053",
                "timestamp": "2026-02-23 08:33:28.113782+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Betelhem_EMP-0053/screenshot/Feb23/2987e9a2-9f90-44ae-adf0-774477186505.webp",
                "app_name": "chrome.exe",
                "window_title": "Refund - Google Sheets - Google Chrome",
                "event": "Custom_CLICK",
                "url": "docs.google.com/spreadsheets/d/1JH9H7e5Ng3vm6oBtKy9ykkrafwh-GykeNXhB77qRkLQ/edit?gid=654230300#gid=654230300",
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



