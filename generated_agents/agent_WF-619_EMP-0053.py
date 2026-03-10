
import pyautogui
import time
import webbrowser
import os

# Generated Agent for Workflow: WF-619
# Employee: EMP-0053
# Pattern: chrome.exe:CLICK->chrome.exe:Custom_CLICK->chrome.exe:CLICK->explorer.exe:APP_SWITCH->ShellExperienceHost.exe:Custom_CLICK


def run_agent():
    print(f"--- Start Generated Agent for WF-619 ---")
    pyautogui.PAUSE = 1.0

    steps = [
        {
                "id_employee": "EMP-0053",
                "timestamp": "2026-02-23 09:09:40.014000+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Betelhem_EMP-0053/screenshot/Feb23/7a239278-1fb0-4b44-b6d3-cb1cb57b2530.webp",
                "app_name": "chrome.exe",
                "window_title": "Cash back tracking system - Google Sheets - Google Chrome",
                "event": "CLICK",
                "url": "docs.google.com/spreadsheets/d/1zgiazbXFk94yiNbwCo6sGeTI6_o1bACY69-d10r1JBk/edit?gid=0#gid=0",
                "date": "2026-02-23"
        },
        {
                "id_employee": "EMP-0053",
                "timestamp": "2026-02-23 09:09:45.847557+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Betelhem_EMP-0053/screenshot/Feb23/4383169b-7803-4437-8948-3eb3a430c02a.webp",
                "app_name": "chrome.exe",
                "window_title": "Cash back tracking system - Google Sheets - Google Chrome",
                "event": "Custom_CLICK",
                "url": "docs.google.com/spreadsheets/d/1zgiazbXFk94yiNbwCo6sGeTI6_o1bACY69-d10r1JBk/edit?gid=0#gid=0",
                "date": "2026-02-23"
        },
        {
                "id_employee": "EMP-0053",
                "timestamp": "2026-02-23 09:09:50.014000+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Betelhem_EMP-0053/screenshot/Feb23/fb779c68-b020-4085-beef-9775dca8fb34.webp",
                "app_name": "chrome.exe",
                "window_title": "Cash back tracking system - Google Sheets - Google Chrome",
                "event": "CLICK",
                "url": "docs.google.com/spreadsheets/d/1zgiazbXFk94yiNbwCo6sGeTI6_o1bACY69-d10r1JBk/edit?gid=0#gid=0",
                "date": "2026-02-23"
        },
        {
                "id_employee": "EMP-0053",
                "timestamp": "2026-02-23 09:09:55.765000+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Betelhem_EMP-0053/screenshot/Feb23/91ca37f5-829e-415b-8cbe-6ccba11d011c.webp",
                "app_name": "explorer.exe",
                "window_title": "Control Center",
                "event": "APP_SWITCH",
                "url": "",
                "date": "2026-02-23"
        },
        {
                "id_employee": "EMP-0053",
                "timestamp": "2026-02-23 09:09:58.732138+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Betelhem_EMP-0053/screenshot/Feb23/3fb2d770-0a27-4985-bd80-62d1b1122bf3.webp",
                "app_name": "ShellExperienceHost.exe",
                "window_title": "Control Center",
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



