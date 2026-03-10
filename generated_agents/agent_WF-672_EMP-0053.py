
import pyautogui
import time
import webbrowser
import os

# Generated Agent for Workflow: WF-672
# Employee: EMP-0053
# Pattern: chrome.exe:CLICK->chrome.exe:Custom_CLICK->chrome.exe:MOVE->chrome.exe:Custom_CLICK->chrome.exe:Custom_CLICK


def run_agent():
    print(f"--- Start Generated Agent for WF-672 ---")
    pyautogui.PAUSE = 1.0

    steps = [
        {
                "id_employee": "EMP-0053",
                "timestamp": "2026-02-23 13:09:35.001000+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Betelhem_EMP-0053/screenshot/Feb23/7532b52b-5198-4192-b6d6-2ae390f64b48.webp",
                "app_name": "chrome.exe",
                "window_title": "Meet - Daily optimization - Google Chrome",
                "event": "CLICK",
                "url": "meet.google.com/vtg-mqos-hts?authuser=0",
                "date": "2026-02-23"
        },
        {
                "id_employee": "EMP-0053",
                "timestamp": "2026-02-23 13:09:38.344005+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Betelhem_EMP-0053/screenshot/Feb23/98e9bfdb-78d8-402e-91ab-afbbe2425c77.webp",
                "app_name": "chrome.exe",
                "window_title": "Meet - Daily optimization - Google Chrome",
                "event": "Custom_CLICK",
                "url": "meet.google.com/vtg-mqos-hts?authuser=0",
                "date": "2026-02-23"
        },
        {
                "id_employee": "EMP-0053",
                "timestamp": "2026-02-23 13:16:15.010000+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Betelhem_EMP-0053/screenshot/Feb23/9d2a2100-88e7-4367-aed8-a7696ee61f26.webp",
                "app_name": "chrome.exe",
                "window_title": "Meet - Daily optimization - Google Chrome",
                "event": "MOVE",
                "url": "meet.google.com/vtg-mqos-hts?authuser=0",
                "date": "2026-02-23"
        },
        {
                "id_employee": "EMP-0053",
                "timestamp": "2026-02-23 13:17:41.486624+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Betelhem_EMP-0053/screenshot/Feb23/3f645562-83d6-4ca6-9121-082be4fe2b8f.webp",
                "app_name": "chrome.exe",
                "window_title": "Meet - Daily optimization - Google Chrome",
                "event": "Custom_CLICK",
                "url": "meet.google.com/vtg-mqos-hts?authuser=0",
                "date": "2026-02-23"
        },
        {
                "id_employee": "EMP-0053",
                "timestamp": "2026-02-23 13:20:14.648655+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Betelhem_EMP-0053/screenshot/Feb23/f9d7c770-2829-4167-bd2c-f219f494435b.webp",
                "app_name": "chrome.exe",
                "window_title": "Meet - Daily optimization - Google Chrome",
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



