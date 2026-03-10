
import pyautogui
import time
import webbrowser
import os

# Generated Agent for Workflow: WF-642
# Employee: EMP-0053
# Pattern: chrome.exe:Custom_CLICK->chrome.exe:Custom_CLICK->chrome.exe:Custom_CLICK->Telegram.exe:CLICK->Telegram.exe:Custom_CLICK


def run_agent():
    print(f"--- Start Generated Agent for WF-642 ---")
    pyautogui.PAUSE = 1.0

    steps = [
        {
                "id_employee": "EMP-0053",
                "timestamp": "2026-02-23 11:21:04.393731+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Betelhem_EMP-0053/screenshot/Feb23/538119d6-558b-4123-802c-f9f88f7c63a8.webp",
                "app_name": "chrome.exe",
                "window_title": "Inbox (46) - bettytagele90@gmail.com - Gmail - Google Chrome",
                "event": "Custom_CLICK",
                "url": "mail.google.com/mail/u/0/#inbox/FMfcgzQdzmZVqWqQWcSKlBQGgBPjcdvh",
                "date": "2026-02-23"
        },
        {
                "id_employee": "EMP-0053",
                "timestamp": "2026-02-23 11:21:11.700878+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Betelhem_EMP-0053/screenshot/Feb23/31986d16-e218-4a7a-be2d-f39e908082d2.webp",
                "app_name": "chrome.exe",
                "window_title": "Invitation: All Staff Meeting - Inperson @ Wed Dec 17, 2025 10:30am - 11am (GMT+3) (bettytagele90@gmail.com) - bettytagele90@gmail.com - Gmail - Google Chrome",
                "event": "Custom_CLICK",
                "url": "docs.google.com/spreadsheets/d/1zgiazbXFk94yiNbwCo6sGeTI6_o1bACY69-d10r1JBk/edit?gid=0#gid=0",
                "date": "2026-02-23"
        },
        {
                "id_employee": "EMP-0053",
                "timestamp": "2026-02-23 11:25:00.754706+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Betelhem_EMP-0053/screenshot/Feb23/6deb2ffb-7e07-4daa-bb46-b8fd234813e1.webp",
                "app_name": "chrome.exe",
                "window_title": "Cash back tracking system - Google Sheets - Google Chrome",
                "event": "Custom_CLICK",
                "url": "",
                "date": "2026-02-23"
        },
        {
                "id_employee": "EMP-0053",
                "timestamp": "2026-02-23 11:25:35.005000+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Betelhem_EMP-0053/screenshot/Feb23/5aaf9b1f-f93a-4feb-80c5-e133d71ef8a0.webp",
                "app_name": "Telegram.exe",
                "window_title": "\u200eCall Center (5544)",
                "event": "CLICK",
                "url": "",
                "date": "2026-02-23"
        },
        {
                "id_employee": "EMP-0053",
                "timestamp": "2026-02-23 11:25:44.018276+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Betelhem_EMP-0053/screenshot/Feb23/c2de399b-b86d-4108-ac68-da056026ab06.webp",
                "app_name": "Telegram.exe",
                "window_title": "\u200eMiss Sun @ \u200eChip Chip Social (5544)",
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



