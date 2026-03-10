
import pyautogui
import time
import webbrowser
import os

# Generated Agent for Workflow: WF-616
# Employee: EMP-0053
# Pattern: chrome.exe:CLICK->msedge.exe:Custom_CLICK->chrome.exe:APP_SWITCH->chrome.exe:CLICK->chrome.exe:Custom_CLICK


def run_agent():
    print(f"--- Start Generated Agent for WF-616 ---")
    pyautogui.PAUSE = 1.0

    steps = [
        {
                "id_employee": "EMP-0053",
                "timestamp": "2026-02-23 09:02:20.014000+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Betelhem_EMP-0053/screenshot/Feb23/8cf4f638-b8a0-4833-be64-b9e22c2dd175.webp",
                "app_name": "chrome.exe",
                "window_title": "Cash back tracking system - Google Sheets - Google Chrome",
                "event": "CLICK",
                "url": "docs.google.com/spreadsheets/d/1zgiazbXFk94yiNbwCo6sGeTI6_o1bACY69-d10r1JBk/edit?gid=0#gid=0",
                "date": "2026-02-23"
        },
        {
                "id_employee": "EMP-0053",
                "timestamp": "2026-02-23 09:02:23.343197+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Betelhem_EMP-0053/screenshot/Feb23/0468a2f3-a7d1-45e1-8e8e-5250d99f1d62.webp",
                "app_name": "msedge.exe",
                "window_title": "Reports and 4 more pages - Personal - Microsoft\u200b Edge",
                "event": "Custom_CLICK",
                "url": "docs.google.com/spreadsheets/d/1zgiazbXFk94yiNbwCo6sGeTI6_o1bACY69-d10r1JBk/edit?gid=0#gid=0",
                "date": "2026-02-23"
        },
        {
                "id_employee": "EMP-0053",
                "timestamp": "2026-02-23 09:02:23.562000+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Betelhem_EMP-0053/screenshot/Feb23/a28f3274-edf8-40d9-ba7a-f6d6e74c41a4.webp",
                "app_name": "chrome.exe",
                "window_title": "Cash back tracking system - Google Sheets - Google Chrome",
                "event": "APP_SWITCH",
                "url": "docs.google.com/spreadsheets/d/1zgiazbXFk94yiNbwCo6sGeTI6_o1bACY69-d10r1JBk/edit?gid=0#gid=0",
                "date": "2026-02-23"
        },
        {
                "id_employee": "EMP-0053",
                "timestamp": "2026-02-23 09:02:35.007000+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Betelhem_EMP-0053/screenshot/Feb23/37f898c7-e1b1-43f3-a216-f7831e23173e.webp",
                "app_name": "chrome.exe",
                "window_title": "Cash back tracking system - Google Sheets - Google Chrome",
                "event": "CLICK",
                "url": "docs.google.com/spreadsheets/d/1zgiazbXFk94yiNbwCo6sGeTI6_o1bACY69-d10r1JBk/edit?gid=0#gid=0",
                "date": "2026-02-23"
        },
        {
                "id_employee": "EMP-0053",
                "timestamp": "2026-02-23 09:02:39.067633+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Betelhem_EMP-0053/screenshot/Feb23/8ed7f30c-7522-4bfd-a2f0-c9a7a2b60487.webp",
                "app_name": "chrome.exe",
                "window_title": "Cash back tracking system - Google Sheets - Google Chrome",
                "event": "Custom_CLICK",
                "url": "docs.google.com/spreadsheets/d/1zgiazbXFk94yiNbwCo6sGeTI6_o1bACY69-d10r1JBk/edit?gid=0#gid=0",
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



