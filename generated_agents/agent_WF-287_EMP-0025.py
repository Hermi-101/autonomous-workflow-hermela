
import pyautogui
import time
import webbrowser
import os

# Generated Agent for Workflow: WF-287
# Employee: EMP-0025
# Pattern: Telegram.exe:TYPE->Telegram.exe:TYPE->Telegram.exe:TYPE->Telegram.exe:TYPE->Telegram.exe:Custom_CLICK


def run_agent():
    print(f"--- Start Generated Agent for WF-287 ---")
    pyautogui.PAUSE = 1.0

    steps = [
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
        },
        {
                "id_employee": "EMP-0025",
                "timestamp": "2026-02-24 08:24:45.011000+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Natnael_EMP-0025/screenshot/Feb24/72ba3b0b-6d9d-448e-9745-e96a918f2130.webp",
                "app_name": "Telegram.exe",
                "window_title": "\u200eBrayce Fepa @ \u200eNA (6931)",
                "event": "TYPE",
                "url": "",
                "date": "2026-02-24"
        },
        {
                "id_employee": "EMP-0025",
                "timestamp": "2026-02-24 08:25:00.002000+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Natnael_EMP-0025/screenshot/Feb24/ac2c2b8e-72ef-4659-9b5c-b818609937ef.webp",
                "app_name": "Telegram.exe",
                "window_title": "\u200eBrayce Fepa @ \u200eNA (6932)",
                "event": "TYPE",
                "url": "",
                "date": "2026-02-24"
        },
        {
                "id_employee": "EMP-0025",
                "timestamp": "2026-02-24 08:25:11.278240+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Natnael_EMP-0025/screenshot/Feb24/0ec661cd-bfb1-48e4-96f2-06fe37f4ad7e.webp",
                "app_name": "Telegram.exe",
                "window_title": "\u200eBrayce Fepa @ \u200eNA (6932)",
                "event": "Custom_CLICK",
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



