
import pyautogui
import time
import webbrowser
import os

# Generated Agent for Workflow: WF-275
# Employee: EMP-0025
# Pattern: brave.exe:Custom_CLICK->brave.exe:CLICK->brave.exe:Custom_CLICK->brave.exe:Custom_CLICK->brave.exe:APP_SWITCH


def run_agent():
    print(f"--- Start Generated Agent for WF-275 ---")
    pyautogui.PAUSE = 1.0

    steps = [
        {
                "id_employee": "EMP-0025",
                "timestamp": "2026-02-24 05:31:58.366218+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Natnael_EMP-0025/screenshot/Feb24/65ea7bdc-22d0-4e92-be97-c91639b0a87c.webp",
                "app_name": "brave.exe",
                "window_title": "ChipChip Supply - Brave",
                "event": "Custom_CLICK",
                "url": "supplystaging.chipchip.social/request-payment",
                "date": "2026-02-24"
        },
        {
                "id_employee": "EMP-0025",
                "timestamp": "2026-02-24 05:32:10.013000+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Natnael_EMP-0025/screenshot/Feb24/8ebe76c3-70f9-4e84-83a7-fd129b08acd7.webp",
                "app_name": "brave.exe",
                "window_title": "Account Renewal Notice! - natiassefa5@gmail.com - Gmail - Brave",
                "event": "CLICK",
                "url": "mail.google.com/mail/u/0/#inbox/FMfcgzQfBsvSLcnHCpdNpqJhhHvbkfdH",
                "date": "2026-02-24"
        },
        {
                "id_employee": "EMP-0025",
                "timestamp": "2026-02-24 05:32:10.069656+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Natnael_EMP-0025/screenshot/Feb24/84c3ef93-d403-47a0-93a9-a1fd3b07899b.webp",
                "app_name": "brave.exe",
                "window_title": "ChipChip Supply - Brave",
                "event": "Custom_CLICK",
                "url": "mail.google.com/mail/u/0/#inbox",
                "date": "2026-02-24"
        },
        {
                "id_employee": "EMP-0025",
                "timestamp": "2026-02-24 05:32:12.641413+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Natnael_EMP-0025/screenshot/Feb24/4d53bd0f-4637-4af9-b0bf-ad2ee3203cbe.webp",
                "app_name": "brave.exe",
                "window_title": "Inbox (56) - natiassefa5@gmail.com - Gmail - Brave",
                "event": "Custom_CLICK",
                "url": "mail.google.com/mail/u/0/#inbox/FMfcgzQfBsvSLcnHCpdNpqJhhHvbkfdH",
                "date": "2026-02-24"
        },
        {
                "id_employee": "EMP-0025",
                "timestamp": "2026-02-24 05:32:13.776000+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Natnael_EMP-0025/screenshot/Feb24/f41949a3-f530-4b49-8ce1-be0857b60b2d.webp",
                "app_name": "brave.exe",
                "window_title": "Account Renewal Notice! - natiassefa5@gmail.com - Gmail - Brave",
                "event": "APP_SWITCH",
                "url": "mail.google.com/mail/u/0/#inbox/FMfcgzQfBsvSLcnHCpdNpqJhhHvbkfdH",
                "date": "2026-02-24"
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



