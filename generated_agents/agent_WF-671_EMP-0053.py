
import pyautogui
import time
import webbrowser
import os

# Generated Agent for Workflow: WF-671
# Employee: EMP-0053
# Pattern: chrome.exe:Custom_CLICK->chrome.exe:CLICK->chrome.exe:Custom_CLICK->chrome.exe:TYPE->chrome.exe:Custom_CLICK


def run_agent():
    print(f"--- Start Generated Agent for WF-671 ---")
    pyautogui.PAUSE = 1.0

    steps = [
        {
                "id_employee": "EMP-0053",
                "timestamp": "2026-02-23 12:52:52.243258+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Betelhem_EMP-0053/screenshot/Feb23/fad398ce-99c0-4e93-bdd6-162535ae012a.webp",
                "app_name": "chrome.exe",
                "window_title": "chipchipadmindec.chipchip.social/dashboard/users/userdetails?id=31f1ceb3-2014-445f-b472-49fd99827b2a - Google Chrome",
                "event": "Custom_CLICK",
                "url": "chipchipadmindec.chipchip.social/dashboard/users/userdetails?id=31f1ceb3-2014-445f-b472-49fd99827b2a",
                "date": "2026-02-23"
        },
        {
                "id_employee": "EMP-0053",
                "timestamp": "2026-02-23 12:59:25.013000+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Betelhem_EMP-0053/screenshot/Feb23/833d156d-41b0-4de6-a3a1-050ce0914c1b.webp",
                "app_name": "chrome.exe",
                "window_title": "Invitation: All Staff Meeting - Inperson @ Wed Dec 17, 2025 10:30am - 11am (GMT+3) (bettytagele90@gmail.com) - bettytagele90@gmail.com - Gmail - Google Chrome",
                "event": "CLICK",
                "url": "mail.google.com/mail/u/0/#inbox/FMfcgzQdzmZVqWqQWcSKlBQGgBPjcdvh",
                "date": "2026-02-23"
        },
        {
                "id_employee": "EMP-0053",
                "timestamp": "2026-02-23 12:59:26.978014+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Betelhem_EMP-0053/screenshot/Feb23/6000e6ec-e9fe-4802-a7e2-5e009c201243.webp",
                "app_name": "chrome.exe",
                "window_title": "chipchipadmindec.chipchip.social/dashboard/users/userdetails?id=31f1ceb3-2014-445f-b472-49fd99827b2a - Google Chrome",
                "event": "Custom_CLICK",
                "url": "mail.google.com/mail/u/0/#inbox/FMfcgzQdzmZVqWqQWcSKlBQGgBPjcdvh",
                "date": "2026-02-23"
        },
        {
                "id_employee": "EMP-0053",
                "timestamp": "2026-02-23 12:59:40.001000+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Betelhem_EMP-0053/screenshot/Feb23/fa87f688-3bf2-42e4-bb4d-a49c9a95e2f3.webp",
                "app_name": "chrome.exe",
                "window_title": "Call rating - Google Chrome",
                "event": "TYPE",
                "url": "docs.google.com/spreadsheets/d/1gpRHDsp_7PZGnttYRRnJgLjzD2y4i4u0jXX44ZzslTo/edit?resourcekey=&gid=565539917#gid=565539917",
                "date": "2026-02-23"
        },
        {
                "id_employee": "EMP-0053",
                "timestamp": "2026-02-23 12:59:47.490586+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Betelhem_EMP-0053/screenshot/Feb23/c1e6150e-34cf-43e1-a8ad-0e83dd1b15ca.webp",
                "app_name": "chrome.exe",
                "window_title": "Invitation: All Staff Meeting - Inperson @ Wed Dec 17, 2025 10:30am - 11am (GMT+3) (bettytagele90@gmail.com) - bettytagele90@gmail.com - Gmail - Google Chrome",
                "event": "Custom_CLICK",
                "url": "docs.google.com/forms/u/0/d/e/1FAIpQLSfT7yNPzJDyJvzMrd4hfKuVdH8VDYydur6r0vdGD3ES__ZExA/formResponse",
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



