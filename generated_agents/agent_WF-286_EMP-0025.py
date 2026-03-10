
import pyautogui
import time
import webbrowser
import os

# Generated Agent for Workflow: WF-286
# Employee: EMP-0025
# Pattern: Telegram.exe:Custom_CLICK->Telegram.exe:TYPE->Telegram.exe:TYPE->Telegram.exe:TYPE->Telegram.exe:TYPE


def run_agent():
    print(f"--- Start Generated Agent for WF-286 ---")
    pyautogui.PAUSE = 1.0

    steps = [
        {
                "id_employee": "EMP-0025",
                "timestamp": "2026-02-24 08:22:52.274972+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Natnael_EMP-0025/screenshot/Feb24/aacccc9a-1bcc-481a-927f-cfdfb13df8fa.webp",
                "app_name": "Telegram.exe",
                "window_title": "\u200eAmir @ \u200eNA (6930)",
                "event": "Custom_CLICK",
                "url": "",
                "date": "2026-02-24"
        },
        {
                "id_employee": "EMP-0025",
                "timestamp": "2026-02-24 08:23:00+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Natnael_EMP-0025/screenshot/Feb24/b82f1b6f-68fa-4a46-b2af-10c7517b3ec7.webp",
                "app_name": "Telegram.exe",
                "window_title": "\u200eBrayce Fepa @ \u200eNA (6931)",
                "event": "TYPE",
                "url": "",
                "date": "2026-02-24"
        },
        {
                "id_employee": "EMP-0025",
                "timestamp": "2026-02-24 08:23:55.012000+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Natnael_EMP-0025/screenshot/Feb24/318a35b2-608d-4313-bda1-80ce6d6f639c.webp",
                "app_name": "Telegram.exe",
                "window_title": "\u200eBrayce Fepa @ \u200eNA (6931)",
                "event": "TYPE",
                "url": "",
                "date": "2026-02-24"
        },
        {
                "id_employee": "EMP-0025",
                "timestamp": "2026-02-24 08:24:15.015000+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Natnael_EMP-0025/screenshot/Feb24/d3d7b834-adca-4f86-9d16-a26ec5f7887b.webp",
                "app_name": "Telegram.exe",
                "window_title": "\u200eBrayce Fepa @ \u200eNA (6931)",
                "event": "TYPE",
                "url": "",
                "date": "2026-02-24"
        },
        {
                "id_employee": "EMP-0025",
                "timestamp": "2026-02-24 08:24:30.015000+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Natnael_EMP-0025/screenshot/Feb24/06a1901c-08ab-4c99-9d85-b520d6e85be8.webp",
                "app_name": "Telegram.exe",
                "window_title": "\u200eBrayce Fepa @ \u200eNA (6931)",
                "event": "TYPE",
                "url": "",
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



