
import pyautogui
import time
import webbrowser
import os

# Generated Agent for Workflow: WF-206
# Employee: EMP-0025
# Pattern: brave.exe:Custom_CLICK->brave.exe:Custom_CLICK->brave.exe:Custom_CLICK->chrome.exe:Custom_CLICK->chrome.exe:Custom_CLICK


def run_agent():
    print(f"--- Start Generated Agent for WF-206 ---")
    pyautogui.PAUSE = 1.0

    steps = [
        {
                "id_employee": "EMP-0025",
                "timestamp": "2026-02-23 10:17:43.765203+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Natnael_EMP-0025/screenshot/Feb23/b3a898bd-7e28-4818-8d3f-b7b0bc52f9f5.webp",
                "app_name": "brave.exe",
                "window_title": "Google Calendar - February 2026 - Brave",
                "event": "Custom_CLICK",
                "url": "calendar.google.com/calendar/u/0/r/month",
                "date": "2026-02-23"
        },
        {
                "id_employee": "EMP-0025",
                "timestamp": "2026-02-23 10:17:48.542902+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Natnael_EMP-0025/screenshot/Feb23/31f0e5e4-0513-4c28-b85a-df8a2aceec9d.webp",
                "app_name": "brave.exe",
                "window_title": "Google Calendar - February 2026 - Brave",
                "event": "Custom_CLICK",
                "url": "calendar.google.com/calendar/u/0/r/month",
                "date": "2026-02-23"
        },
        {
                "id_employee": "EMP-0025",
                "timestamp": "2026-02-23 10:17:54.695006+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Natnael_EMP-0025/screenshot/Feb23/5fb8f6fe-a5ec-4061-9d24-75caab327a5a.webp",
                "app_name": "brave.exe",
                "window_title": "Somewhere Typing Test - Brave",
                "event": "Custom_CLICK",
                "url": "",
                "date": "2026-02-23"
        },
        {
                "id_employee": "EMP-0025",
                "timestamp": "2026-02-23 10:17:59.833786+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Natnael_EMP-0025/screenshot/Feb23/dd616880-8039-4095-b9f6-e544e3da5a98.webp",
                "app_name": "chrome.exe",
                "window_title": "Google Meet - Meet - Review Planning on ChipChip360",
                "event": "Custom_CLICK",
                "url": "meet.google.com/jvf-hihx-opj?lfhs=2",
                "date": "2026-02-23"
        },
        {
                "id_employee": "EMP-0025",
                "timestamp": "2026-02-23 10:18:01.689598+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Natnael_EMP-0025/screenshot/Feb23/728ff421-e84c-420a-b069-46cdca65ca9b.webp",
                "app_name": "chrome.exe",
                "window_title": "Google Meet - Meet - Review Planning on ChipChip360",
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



