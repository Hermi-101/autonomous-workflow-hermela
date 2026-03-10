
import pyautogui
import time
import webbrowser
import os

# Generated Agent for Workflow: WF-215
# Employee: EMP-0025
# Pattern: brave.exe:Custom_COPY_ACTION->brave.exe:Custom_CLICK->brave.exe:Custom_CLICK->brave.exe:Custom_CLICK->brave.exe:Custom_CLICK


def run_agent():
    print(f"--- Start Generated Agent for WF-215 ---")
    pyautogui.PAUSE = 1.0

    steps = [
        {
                "id_employee": "EMP-0025",
                "timestamp": "2026-02-23 11:48:28.972494+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Natnael_EMP-0025/screenshot/Feb23/6209f683-7350-4b4e-aed3-ea37032555f9.webp",
                "app_name": "brave.exe",
                "window_title": "Fix of warehouse - Google Sheets - Brave",
                "event": "Custom_COPY_ACTION",
                "url": "docs.google.com/spreadsheets/d/1UByYg7_GMjNIqjoXEcNezc2bNfnSVuOU8japFLXceUU/edit?gid=895107596#gid=895107596",
                "date": "2026-02-23"
        },
        {
                "id_employee": "EMP-0025",
                "timestamp": "2026-02-23 11:48:34.780315+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Natnael_EMP-0025/screenshot/Feb23/5249e46f-313a-40a4-982f-9df8ba5e5037.webp",
                "app_name": "brave.exe",
                "window_title": "Skill Suggestions for User - Brave",
                "event": "Custom_CLICK",
                "url": "mail.google.com/mail/u/0/#inbox/FMfcgzQfBsvQmZTxMwWKdRBDphsPsQzk",
                "date": "2026-02-23"
        },
        {
                "id_employee": "EMP-0025",
                "timestamp": "2026-02-23 11:48:36.304273+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Natnael_EMP-0025/screenshot/Feb23/db71b145-bec0-4ec2-8190-403a270763bb.webp",
                "app_name": "brave.exe",
                "window_title": "Document shared with you: \"ChipChip System Security Evaluation\" - natiassefa5@gmail.com - Gmail - Brave",
                "event": "Custom_CLICK",
                "url": "mail.google.com/mail/u/0/#inbox",
                "date": "2026-02-23"
        },
        {
                "id_employee": "EMP-0025",
                "timestamp": "2026-02-23 11:48:38.146668+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Natnael_EMP-0025/screenshot/Feb23/8eda3d24-ca24-4e8d-98ee-93179e1a0503.webp",
                "app_name": "brave.exe",
                "window_title": "Inbox (57) - natiassefa5@gmail.com - Gmail - Brave",
                "event": "Custom_CLICK",
                "url": "mail.google.com/mail/u/0/#inbox/FMfcgzQfBsvQwCZXxtDnxVkcMMhWqVSC",
                "date": "2026-02-23"
        },
        {
                "id_employee": "EMP-0025",
                "timestamp": "2026-02-23 11:48:43.227430+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Natnael_EMP-0025/screenshot/Feb23/5f7849f2-4ba3-4d81-95e6-fa3e1d6f1ddd.webp",
                "app_name": "brave.exe",
                "window_title": "Invitation: Pick up plan @ Mon Feb 23, 2026 3:15pm - 4:15pm (GMT+3) (natiassefa5@gmail.com) - natiassefa5@gmail.com - Gmail - Brave",
                "event": "Custom_CLICK",
                "url": "mail.google.com/mail/u/0/#inbox/FMfcgzQfBsvQwCZXxtDnxVkcMMhWqVSC",
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



