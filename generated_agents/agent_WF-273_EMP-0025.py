
import pyautogui
import time
import webbrowser
import os

# Generated Agent for Workflow: WF-273
# Employee: EMP-0025
# Pattern: brave.exe:APP_SWITCH->brave.exe:Custom_CLICK->brave.exe:APP_SWITCH->brave.exe:CLICK->brave.exe:Custom_CLICK


def run_agent():
    print(f"--- Start Generated Agent for WF-273 ---")
    pyautogui.PAUSE = 1.0

    steps = [
        {
                "id_employee": "EMP-0025",
                "timestamp": "2026-02-24 05:25:05.800000+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Natnael_EMP-0025/screenshot/Feb24/fbfb5356-ad9d-46c0-a189-cf4943fd0db7.webp",
                "app_name": "brave.exe",
                "window_title": "Inbox (57) - natiassefa5@gmail.com - Gmail - Brave",
                "event": "APP_SWITCH",
                "url": "mail.google.com/mail/u/0/#inbox",
                "date": "2026-02-24"
        },
        {
                "id_employee": "EMP-0025",
                "timestamp": "2026-02-24 05:25:07.861467+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Natnael_EMP-0025/screenshot/Feb24/fb37c7bb-9fde-4ff4-beb1-f7300b082a24.webp",
                "app_name": "brave.exe",
                "window_title": "Inbox (57) - natiassefa5@gmail.com - Gmail - Brave",
                "event": "Custom_CLICK",
                "url": "mail.google.com/mail/u/0/#inbox/FMfcgzQfBsvQmkbTxWQsfLzJTgpkrqrQ",
                "date": "2026-02-24"
        },
        {
                "id_employee": "EMP-0025",
                "timestamp": "2026-02-24 05:25:09.926000+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Natnael_EMP-0025/screenshot/Feb24/3d780e2f-2191-402d-affa-d7db17c10157.webp",
                "app_name": "brave.exe",
                "window_title": "ChipChip Project ... - Can we get and deduct the customer's ... - natiassefa5@gmail.com - Gmail - Brave",
                "event": "APP_SWITCH",
                "url": "mail.google.com/mail/u/0/#inbox",
                "date": "2026-02-24"
        },
        {
                "id_employee": "EMP-0025",
                "timestamp": "2026-02-24 05:25:10.006000+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Natnael_EMP-0025/screenshot/Feb24/98321a64-118d-4578-9abc-d5ef5ece929f.webp",
                "app_name": "brave.exe",
                "window_title": "Account Renewal Notice! - natiassefa5@gmail.com - Gmail - Brave",
                "event": "CLICK",
                "url": "mail.google.com/mail/u/0/#inbox/FMfcgzQfBsvSLcnHCpdNpqJhhHvbkfdH",
                "date": "2026-02-24"
        },
        {
                "id_employee": "EMP-0025",
                "timestamp": "2026-02-24 05:25:11.615652+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Natnael_EMP-0025/screenshot/Feb24/17beab7a-4588-45e9-94df-47d930f8d476.webp",
                "app_name": "brave.exe",
                "window_title": "ChipChip Project ... - Can we get and deduct the customer's ... - natiassefa5@gmail.com - Gmail - Brave",
                "event": "Custom_CLICK",
                "url": "mail.google.com/mail/u/0/#inbox",
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



