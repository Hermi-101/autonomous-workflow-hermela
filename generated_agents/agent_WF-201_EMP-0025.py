
import pyautogui
import time
import webbrowser
import os

# Generated Agent for Workflow: WF-201
# Employee: EMP-0025
# Pattern: chrome.exe:Custom_CLICK->chrome.exe:Custom_CLICK->chrome.exe:Custom_CLICK->chrome.exe:Custom_CLICK->chrome.exe:Custom_CLICK


def run_agent():
    print(f"--- Start Generated Agent for WF-201 ---")
    pyautogui.PAUSE = 1.0

    steps = [
        {
                "id_employee": "EMP-0025",
                "timestamp": "2026-02-23 10:15:08.266006+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Natnael_EMP-0025/screenshot/Feb23/41003f36-f9d0-44b5-af2c-d817b7fed99c.webp",
                "app_name": "chrome.exe",
                "window_title": "Google Meet - Meet - Review Planning on ChipChip360",
                "event": "Custom_CLICK",
                "url": "meet.google.com/jvf-hihx-opj?lfhs=2",
                "date": "2026-02-23"
        },
        {
                "id_employee": "EMP-0025",
                "timestamp": "2026-02-23 10:15:22.096479+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Natnael_EMP-0025/screenshot/Feb23/0adb77b6-ca75-40e7-821d-86fcea4f20f7.webp",
                "app_name": "chrome.exe",
                "window_title": "Google Meet - Meet - Review Planning on ChipChip360",
                "event": "Custom_CLICK",
                "url": "meet.google.com/jvf-hihx-opj?lfhs=2",
                "date": "2026-02-23"
        },
        {
                "id_employee": "EMP-0025",
                "timestamp": "2026-02-23 10:15:27.519540+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Natnael_EMP-0025/screenshot/Feb23/ff9825f1-50e5-4b62-ae9d-6bc149561920.webp",
                "app_name": "chrome.exe",
                "window_title": "Google Meet - Meet - Review Planning on ChipChip360",
                "event": "Custom_CLICK",
                "url": "meet.google.com/jvf-hihx-opj?lfhs=2",
                "date": "2026-02-23"
        },
        {
                "id_employee": "EMP-0025",
                "timestamp": "2026-02-23 10:15:32.911408+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Natnael_EMP-0025/screenshot/Feb23/a6e1654f-436d-4ae3-8d7c-3ae4e45ec892.webp",
                "app_name": "chrome.exe",
                "window_title": "Google Meet - Meet - Review Planning on ChipChip360",
                "event": "Custom_CLICK",
                "url": "meet.google.com/jvf-hihx-opj?lfhs=2",
                "date": "2026-02-23"
        },
        {
                "id_employee": "EMP-0025",
                "timestamp": "2026-02-23 10:16:10.936145+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Natnael_EMP-0025/screenshot/Feb23/c01e33fd-87b8-4d05-abab-4eebc7cc95f5.webp",
                "app_name": "chrome.exe",
                "window_title": "Google Meet - Meet - Review Planning on ChipChip360",
                "event": "Custom_CLICK",
                "url": "meet.google.com/jvf-hihx-opj?lfhs=2",
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



