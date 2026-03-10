
import pyautogui
import time
import webbrowser
import os

# Generated Agent for Workflow: WF-189
# Employee: EMP-0025
# Pattern: brave.exe:CLICK->brave.exe:Custom_CLICK->brave.exe:Custom_CLICK->brave.exe:APP_SWITCH->brave.exe:APP_SWITCH


def run_agent():
    print(f"--- Start Generated Agent for WF-189 ---")
    pyautogui.PAUSE = 1.0

    steps = [
        {
                "id_employee": "EMP-0025",
                "timestamp": "2026-02-23 08:53:25.010000+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Natnael_EMP-0025/screenshot/Feb23/54a1dea8-7839-4942-b14a-9bae2a4b4fa6.webp",
                "app_name": "brave.exe",
                "window_title": "Document shared with you: \"ChipChip System Security Evaluation\" - natiassefa5@gmail.com - Gmail - Brave",
                "event": "CLICK",
                "url": "mail.google.com/mail/u/0/#inbox/FMfcgzQfBsvQmZTxMwWKdRBDphsPsQzk",
                "date": "2026-02-23"
        },
        {
                "id_employee": "EMP-0025",
                "timestamp": "2026-02-23 08:53:26.797757+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Natnael_EMP-0025/screenshot/Feb23/f5911b7a-0588-4310-a287-3764492c334a.webp",
                "app_name": "brave.exe",
                "window_title": "Fix of warehouse - Google Sheets - Brave",
                "event": "Custom_CLICK",
                "url": "",
                "date": "2026-02-23"
        },
        {
                "id_employee": "EMP-0025",
                "timestamp": "2026-02-23 08:53:28.056319+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Natnael_EMP-0025/screenshot/Feb23/d4b607e0-1db9-466a-b3fe-caecda6e89f8.webp",
                "app_name": "brave.exe",
                "window_title": "Skill Suggestions for User - Brave",
                "event": "Custom_CLICK",
                "url": "mail.google.com/mail/u/0/#inbox",
                "date": "2026-02-23"
        },
        {
                "id_employee": "EMP-0025",
                "timestamp": "2026-02-23 08:53:28.848000+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Natnael_EMP-0025/screenshot/Feb23/11738341-a3e7-4f8d-b498-ef1b628df368.webp",
                "app_name": "brave.exe",
                "window_title": "ChipChip Project ... - @amir@chipchip.social , @natiassefa5@... - natiassefa5@gmail.com - Gmail - Brave",
                "event": "APP_SWITCH",
                "url": "mail.google.com/mail/u/0/#inbox/FMfcgzQfBsvQmZTxMwWKdRBDphsPsQzk",
                "date": "2026-02-23"
        },
        {
                "id_employee": "EMP-0025",
                "timestamp": "2026-02-23 08:53:30.902000+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Natnael_EMP-0025/screenshot/Feb23/90f08c7c-d3a3-4b33-8140-fdf62737599e.webp",
                "app_name": "brave.exe",
                "window_title": "Inbox (54) - natiassefa5@gmail.com - Gmail - Brave",
                "event": "APP_SWITCH",
                "url": "mail.google.com/mail/u/0/#inbox/FMfcgzQfBsvQmZTxMwWKdRBDphsPsQzk",
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



