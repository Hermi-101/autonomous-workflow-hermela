
import pyautogui
import time
import webbrowser
import os

# Generated Agent for Workflow: WF-621
# Employee: EMP-0053
# Pattern: chrome.exe:CLICK->chrome.exe:APP_SWITCH->chrome.exe:Custom_CLICK->chrome.exe:CLICK->chrome.exe:Custom_CLICK


def run_agent():
    print(f"--- Start Generated Agent for WF-621 ---")
    pyautogui.PAUSE = 1.0

    steps = [
        {
                "id_employee": "EMP-0053",
                "timestamp": "2026-02-23 09:18:00.008000+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Betelhem_EMP-0053/screenshot/Feb23/b5cad3a3-c19d-4453-9eb7-96b94159b605.webp",
                "app_name": "chrome.exe",
                "window_title": "Inbox (45) - bettytagele90@gmail.com - Gmail - Google Chrome",
                "event": "CLICK",
                "url": "mail.google.com/mail/u/0/#inbox",
                "date": "2026-02-23"
        },
        {
                "id_employee": "EMP-0053",
                "timestamp": "2026-02-23 09:18:02.621000+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Betelhem_EMP-0053/screenshot/Feb23/84d512a8-b386-4e3e-8103-d2bd1f75c307.webp",
                "app_name": "chrome.exe",
                "window_title": "New Tab - Google Chrome",
                "event": "APP_SWITCH",
                "url": "mail.google.com/mail/u/0/#inbox",
                "date": "2026-02-23"
        },
        {
                "id_employee": "EMP-0053",
                "timestamp": "2026-02-23 09:18:04.459553+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Betelhem_EMP-0053/screenshot/Feb23/01240e96-32cf-453c-b7d7-3a98f11998af.webp",
                "app_name": "chrome.exe",
                "window_title": "New Tab - Google Chrome",
                "event": "Custom_CLICK",
                "url": "mail.google.com/mail/u/0/",
                "date": "2026-02-23"
        },
        {
                "id_employee": "EMP-0053",
                "timestamp": "2026-02-23 09:18:05.025000+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Betelhem_EMP-0053/screenshot/Feb23/1e497378-8936-4213-8965-cfd49737fa20.webp",
                "app_name": "chrome.exe",
                "window_title": "Inbox (45) - bettytagele90@gmail.com - Gmail - Google Chrome",
                "event": "CLICK",
                "url": "mail.google.com/mail/u/0/#inbox",
                "date": "2026-02-23"
        },
        {
                "id_employee": "EMP-0053",
                "timestamp": "2026-02-23 09:18:06.251169+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Betelhem_EMP-0053/screenshot/Feb23/ecaa5f5b-aa92-4be9-83b2-a2b3b2826036.webp",
                "app_name": "chrome.exe",
                "window_title": "New Tab - Google Chrome",
                "event": "Custom_CLICK",
                "url": "mail.google.com/mail/u/0/",
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



