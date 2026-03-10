
import pyautogui
import time
import webbrowser
import os

# Generated Agent for Workflow: WF-281
# Employee: EMP-0025
# Pattern: brave.exe:APP_SWITCH->brave.exe:CLICK->brave.exe:Custom_CLICK->brave.exe:Custom_CLICK->brave.exe:CLICK


def run_agent():
    print(f"--- Start Generated Agent for WF-281 ---")
    pyautogui.PAUSE = 1.0

    steps = [
        {
                "id_employee": "EMP-0025",
                "timestamp": "2026-02-24 07:51:24.980000+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Natnael_EMP-0025/screenshot/Feb24/83a2a27d-6472-4b09-a1df-7dcb11a14425.webp",
                "app_name": "brave.exe",
                "window_title": "Untitled - Brave",
                "event": "APP_SWITCH",
                "url": "supplystaging.chipchip.social",
                "date": "2026-02-24"
        },
        {
                "id_employee": "EMP-0025",
                "timestamp": "2026-02-24 07:51:35.014000+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Natnael_EMP-0025/screenshot/Feb24/796c91a6-f613-4b8f-8329-6760200feac0.webp",
                "app_name": "brave.exe",
                "window_title": "Superset - Brave",
                "event": "CLICK",
                "url": "64.227.129.135:8088/sqllab/",
                "date": "2026-02-24"
        },
        {
                "id_employee": "EMP-0025",
                "timestamp": "2026-02-24 07:51:37.027028+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Natnael_EMP-0025/screenshot/Feb24/f436314f-30e3-402b-a042-b58a8965753b.webp",
                "app_name": "brave.exe",
                "window_title": "ChipChip Supply - Brave",
                "event": "Custom_CLICK",
                "url": "64.227.129.135:8088/sqllab/",
                "date": "2026-02-24"
        },
        {
                "id_employee": "EMP-0025",
                "timestamp": "2026-02-24 07:51:41.993030+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Natnael_EMP-0025/screenshot/Feb24/4bab4b82-71b3-4931-9624-2678a3f78ba1.webp",
                "app_name": "brave.exe",
                "window_title": "Superset - Brave",
                "event": "Custom_CLICK",
                "url": "64.227.129.135:8088/sqllab/",
                "date": "2026-02-24"
        },
        {
                "id_employee": "EMP-0025",
                "timestamp": "2026-02-24 07:51:55.005000+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Natnael_EMP-0025/screenshot/Feb24/c88ab01f-3f9d-4469-85d2-1f97bfe9de4c.webp",
                "app_name": "brave.exe",
                "window_title": "Superset - Brave",
                "event": "CLICK",
                "url": "64.227.129.135:8088/sqllab/",
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



