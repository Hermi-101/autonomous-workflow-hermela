
import pyautogui
import time
import webbrowser
import os

# Generated Agent for Workflow: WF-673
# Employee: EMP-0053
# Pattern: chrome.exe:Custom_CLICK->chrome.exe:CLICK->chrome.exe:Custom_CLICK->ShellExperienceHost.exe:APP_SWITCH->chrome.exe:CLICK


def run_agent():
    print(f"--- Start Generated Agent for WF-673 ---")
    pyautogui.PAUSE = 1.0

    steps = [
        {
                "id_employee": "EMP-0053",
                "timestamp": "2026-02-23 13:46:42.999863+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Betelhem_EMP-0053/screenshot/Feb23/bf239bda-e66b-413e-982f-b412f39dd736.webp",
                "app_name": "chrome.exe",
                "window_title": "Meet - Daily optimization - Google Chrome",
                "event": "Custom_CLICK",
                "url": "meet.google.com/vtg-mqos-hts?authuser=0",
                "date": "2026-02-23"
        },
        {
                "id_employee": "EMP-0053",
                "timestamp": "2026-02-23 13:49:10.004000+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Betelhem_EMP-0053/screenshot/Feb23/43db148b-0b56-4fdc-bbfd-fbae50bd697c.webp",
                "app_name": "chrome.exe",
                "window_title": "Meet - Daily optimization - Google Chrome",
                "event": "CLICK",
                "url": "meet.google.com/vtg-mqos-hts?authuser=0",
                "date": "2026-02-23"
        },
        {
                "id_employee": "EMP-0053",
                "timestamp": "2026-02-23 13:49:11.383437+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Betelhem_EMP-0053/screenshot/Feb23/6b1f26c2-afb2-418a-9698-f8bb62c9a0ae.webp",
                "app_name": "chrome.exe",
                "window_title": "Meet - Daily optimization - Google Chrome",
                "event": "Custom_CLICK",
                "url": "",
                "date": "2026-02-23"
        },
        {
                "id_employee": "EMP-0053",
                "timestamp": "2026-02-23 13:49:12.830000+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Betelhem_EMP-0053/screenshot/Feb23/1a8ac6cd-8f29-4b01-9709-7a88e2a19fd0.webp",
                "app_name": "ShellExperienceHost.exe",
                "window_title": "Control Center",
                "event": "APP_SWITCH",
                "url": "",
                "date": "2026-02-23"
        },
        {
                "id_employee": "EMP-0053",
                "timestamp": "2026-02-23 13:49:15.007000+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Betelhem_EMP-0053/screenshot/Feb23/2fa03c25-817e-4211-985f-5b99e2124149.webp",
                "app_name": "chrome.exe",
                "window_title": "Meet - Daily optimization - Google Chrome",
                "event": "CLICK",
                "url": "meet.google.com/vtg-mqos-hts?authuser=0",
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



