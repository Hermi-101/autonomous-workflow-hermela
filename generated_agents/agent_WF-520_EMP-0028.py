
import pyautogui
import time
import webbrowser
import os

# Generated Agent for Workflow: WF-520
# Employee: EMP-0028
# Pattern: Telegram.exe:Custom_CLICK->Telegram.exe:Custom_CLICK->Telegram.exe:CLICK->Telegram.exe:CLICK->Telegram.exe:CLICK


def run_agent():
    print(f"--- Start Generated Agent for WF-520 ---")
    pyautogui.PAUSE = 1.0

    steps = [
        {
                "id_employee": "EMP-0028",
                "timestamp": "2026-02-24 13:06:40.582622+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Rihana_EMP-0028/screenshot/Feb24/f473bedd-9f8b-44d9-afae-a26fc6d22079.webp",
                "app_name": "Telegram.exe",
                "window_title": "\u200eRed Teddy \u2013 (879829)",
                "event": "Custom_CLICK",
                "url": "",
                "date": "2026-02-24"
        },
        {
                "id_employee": "EMP-0028",
                "timestamp": "2026-02-24 13:06:44.465989+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Rihana_EMP-0028/screenshot/Feb24/a7902741-d637-49f5-a48e-feaa3cfa48c6.webp",
                "app_name": "Telegram.exe",
                "window_title": "\u200eRed Teddy \u2013 (879829)",
                "event": "Custom_CLICK",
                "url": "",
                "date": "2026-02-24"
        },
        {
                "id_employee": "EMP-0028",
                "timestamp": "2026-02-24 13:06:55.011000+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Rihana_EMP-0028/screenshot/Feb24/04591648-3347-4933-92f5-8db1abf2d9ab.webp",
                "app_name": "Telegram.exe",
                "window_title": "\u200eRed Teddy \u2013 (879829)",
                "event": "CLICK",
                "url": "",
                "date": "2026-02-24"
        },
        {
                "id_employee": "EMP-0028",
                "timestamp": "2026-02-24 13:07:00.014000+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Rihana_EMP-0028/screenshot/Feb24/56923c3b-b8b4-41af-95e7-11f5fcd44687.webp",
                "app_name": "Telegram.exe",
                "window_title": "\u200eRed Teddy \u2013 (879829)",
                "event": "CLICK",
                "url": "",
                "date": "2026-02-24"
        },
        {
                "id_employee": "EMP-0028",
                "timestamp": "2026-02-24 13:08:05.015000+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Rihana_EMP-0028/screenshot/Feb24/5346f2a9-b7f0-4a28-a258-e81170e628c2.webp",
                "app_name": "Telegram.exe",
                "window_title": "\u200eMehari \u2013 (879831)",
                "event": "CLICK",
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



