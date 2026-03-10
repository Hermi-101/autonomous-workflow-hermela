
import pyautogui
import time
import webbrowser
import os

# Generated Agent for Workflow: WF-306
# Employee: EMP-0025
# Pattern: Telegram.exe:TYPE->Telegram.exe:TYPE->Telegram.exe:TYPE->Telegram.exe:TYPE->brave.exe:TYPE


def run_agent():
    print(f"--- Start Generated Agent for WF-306 ---")
    pyautogui.PAUSE = 1.0

    steps = [
        {
                "id_employee": "EMP-0025",
                "timestamp": "2026-02-24 09:57:40.003000+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Natnael_EMP-0025/screenshot/Feb24/8bffdced-948a-4eac-a4a9-0a458a990f68.webp",
                "app_name": "Telegram.exe",
                "window_title": "(1) \u200eRihanna @ \u200eNA (6969)",
                "event": "TYPE",
                "url": "",
                "date": "2026-02-24"
        },
        {
                "id_employee": "EMP-0025",
                "timestamp": "2026-02-24 09:57:45.011000+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Natnael_EMP-0025/screenshot/Feb24/81082af9-d659-43ac-8e9e-69b99b2a7871.webp",
                "app_name": "Telegram.exe",
                "window_title": "(1) \u200eRihanna @ \u200eNA (6969)",
                "event": "TYPE",
                "url": "",
                "date": "2026-02-24"
        },
        {
                "id_employee": "EMP-0025",
                "timestamp": "2026-02-24 09:57:50.010000+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Natnael_EMP-0025/screenshot/Feb24/c01fc55c-50a6-4df9-98af-b7f6f78f10e6.webp",
                "app_name": "Telegram.exe",
                "window_title": "(1) \u200eRihanna @ \u200eNA (6969)",
                "event": "TYPE",
                "url": "",
                "date": "2026-02-24"
        },
        {
                "id_employee": "EMP-0025",
                "timestamp": "2026-02-24 09:57:55.002000+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Natnael_EMP-0025/screenshot/Feb24/2721822a-eb44-44f3-b9a8-a95abcfc61f1.webp",
                "app_name": "Telegram.exe",
                "window_title": "\u200eRihanna @ \u200eNA (6968)",
                "event": "TYPE",
                "url": "",
                "date": "2026-02-24"
        },
        {
                "id_employee": "EMP-0025",
                "timestamp": "2026-02-24 09:58:00.014000+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Natnael_EMP-0025/screenshot/Feb24/c44d49d2-abd8-4f00-8914-d4ded2c40d1e.webp",
                "app_name": "brave.exe",
                "window_title": "chipchipadmindec.chipchip.social/dashboard/warehouse - Brave",
                "event": "TYPE",
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



