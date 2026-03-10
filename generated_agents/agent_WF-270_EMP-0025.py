
import pyautogui
import time
import webbrowser
import os

# Generated Agent for Workflow: WF-270
# Employee: EMP-0025
# Pattern: Telegram.exe:APP_SWITCH->brave.exe:CLICK->Telegram.exe:Custom_CLICK->brave.exe:APP_SWITCH->brave.exe:Custom_CLICK


def run_agent():
    print(f"--- Start Generated Agent for WF-270 ---")
    pyautogui.PAUSE = 1.0

    steps = [
        {
                "id_employee": "EMP-0025",
                "timestamp": "2026-02-24 05:24:23.710000+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Natnael_EMP-0025/screenshot/Feb24/a4a7e0d7-3a19-4468-8f33-c38ac3957f56.webp",
                "app_name": "Telegram.exe",
                "window_title": "TelegramDesktop",
                "event": "APP_SWITCH",
                "url": "",
                "date": "2026-02-24"
        },
        {
                "id_employee": "EMP-0025",
                "timestamp": "2026-02-24 05:24:45.005000+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Natnael_EMP-0025/screenshot/Feb24/d3d2e429-9121-4829-b3ab-e7df4fc58a62.webp",
                "app_name": "brave.exe",
                "window_title": "Inbox (92) - natiassefa5@gmail.com - Gmail - Brave",
                "event": "CLICK",
                "url": "mail.google.com/mail/u/0/#inbox/FMfcgzQfBsvSLcnHCpdNpqJhhHvbkfdH",
                "date": "2026-02-24"
        },
        {
                "id_employee": "EMP-0025",
                "timestamp": "2026-02-24 05:24:46.414367+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Natnael_EMP-0025/screenshot/Feb24/64b3100a-1630-45a0-9a4c-989da625c6af.webp",
                "app_name": "Telegram.exe",
                "window_title": "\u200eOperations Leads @ \u200eNA (6896)",
                "event": "Custom_CLICK",
                "url": "mail.google.com/mail/u/0/#inbox/FMfcgzQfBsqpWWNNbHjfTgMzqJFzlxWT",
                "date": "2026-02-24"
        },
        {
                "id_employee": "EMP-0025",
                "timestamp": "2026-02-24 05:24:47.346000+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Natnael_EMP-0025/screenshot/Feb24/335d4eed-3a06-40ba-a18c-08526771d023.webp",
                "app_name": "brave.exe",
                "window_title": "Next Step for Your Application - Typing Test - 1709549 - natiassefa5@gmail.com - Gmail - Brave",
                "event": "APP_SWITCH",
                "url": "mail.google.com/mail/u/0/#inbox",
                "date": "2026-02-24"
        },
        {
                "id_employee": "EMP-0025",
                "timestamp": "2026-02-24 05:24:52.394994+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Natnael_EMP-0025/screenshot/Feb24/4cc0f5b0-1f0b-417f-aab4-5ffdbe27edd5.webp",
                "app_name": "brave.exe",
                "window_title": "Next Step for Your Application - Typing Test - 1709549 - natiassefa5@gmail.com - Gmail - Brave",
                "event": "Custom_CLICK",
                "url": "mail.google.com/mail/u/0/#inbox/FMfcgzQfBsqpWWNNbHjfTgMzqJFzlxWT",
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



