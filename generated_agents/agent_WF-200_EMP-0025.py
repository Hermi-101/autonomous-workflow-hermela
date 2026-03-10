
import pyautogui
import time
import webbrowser
import os

# Generated Agent for Workflow: WF-200
# Employee: EMP-0025
# Pattern: brave.exe:Custom_CLICK->brave.exe:Custom_CLICK->brave.exe:Custom_CLICK->chrome.exe:Custom_CLICK->brave.exe:Custom_CLICK


def run_agent():
    print(f"--- Start Generated Agent for WF-200 ---")
    pyautogui.PAUSE = 1.0

    steps = [
        {
                "id_employee": "EMP-0025",
                "timestamp": "2026-02-23 09:36:14.691828+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Natnael_EMP-0025/screenshot/Feb23/840ce1cb-94e9-44d2-be4c-36ae8924ba43.webp",
                "app_name": "brave.exe",
                "window_title": "Discussion Points - Google Sheets - Brave",
                "event": "Custom_CLICK",
                "url": "docs.google.com/spreadsheets/d/1-Xd4t8_5INQWN3KuJS-wlKGJszyjwlFru_Lf3c69Zj4/edit?gid=0#gid=0",
                "date": "2026-02-23"
        },
        {
                "id_employee": "EMP-0025",
                "timestamp": "2026-02-23 09:37:15.346248+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Natnael_EMP-0025/screenshot/Feb23/568b3c48-cce4-49b3-8a1c-f0a33f5125a4.webp",
                "app_name": "brave.exe",
                "window_title": "Discussion Points - Google Sheets - Brave",
                "event": "Custom_CLICK",
                "url": "docs.google.com/spreadsheets/d/1-Xd4t8_5INQWN3KuJS-wlKGJszyjwlFru_Lf3c69Zj4/edit?gid=0#gid=0",
                "date": "2026-02-23"
        },
        {
                "id_employee": "EMP-0025",
                "timestamp": "2026-02-23 09:37:39.109063+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Natnael_EMP-0025/screenshot/Feb23/f38cdf22-cbcf-4cc0-80f3-abcdcef5d6d9.webp",
                "app_name": "brave.exe",
                "window_title": "ChipChip Project Report Week 08, 2026 (Feb 16 - Feb 22) - Google Slides - Brave",
                "event": "Custom_CLICK",
                "url": "",
                "date": "2026-02-23"
        },
        {
                "id_employee": "EMP-0025",
                "timestamp": "2026-02-23 09:37:48.086285+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Natnael_EMP-0025/screenshot/Feb23/8b62ce49-d3b8-44c3-8cfe-9313ac57fb1b.webp",
                "app_name": "chrome.exe",
                "window_title": "Google Meet - Meet - Review Planning on ChipChip360",
                "event": "Custom_CLICK",
                "url": "meet.google.com/jvf-hihx-opj?lfhs=2",
                "date": "2026-02-23"
        },
        {
                "id_employee": "EMP-0025",
                "timestamp": "2026-02-23 09:40:56.163925+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Natnael_EMP-0025/screenshot/Feb23/bab3e6e5-7b5e-42d3-bc2c-7be4cf955469.webp",
                "app_name": "brave.exe",
                "window_title": "Discussion Points - Google Sheets - Brave",
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



