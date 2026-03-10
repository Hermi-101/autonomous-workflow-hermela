
import pyautogui
import time
import webbrowser
import os

# Generated Agent for Workflow: WF-449
# Employee: EMP-0028
# Pattern: Telegram.exe:Custom_CLICK->Telegram.exe:Custom_CLICK->Telegram.exe:TYPE->Telegram.exe:TYPE->Telegram.exe:CLICK


def run_agent():
    print(f"--- Start Generated Agent for WF-449 ---")
    pyautogui.PAUSE = 1.0

    steps = [
        {
                "id_employee": "EMP-0028",
                "timestamp": "2026-02-24 08:35:07.551873+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Rihana_EMP-0028/screenshot/Feb24/ccf09bf5-5163-40bc-84e3-bde1ed25df54.webp",
                "app_name": "Telegram.exe",
                "window_title": "\u200eSiltawi \u1235\u120d\u1273\u12ca \u2013 (879438)",
                "event": "Custom_CLICK",
                "url": "",
                "date": "2026-02-24"
        },
        {
                "id_employee": "EMP-0028",
                "timestamp": "2026-02-24 08:35:09.573047+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Rihana_EMP-0028/screenshot/Feb24/d94b8511-ac7d-44ed-b500-f9bd1e095413.webp",
                "app_name": "Telegram.exe",
                "window_title": "\u200eSiltawi \u1235\u120d\u1273\u12ca \u2013 (879438)",
                "event": "Custom_CLICK",
                "url": "",
                "date": "2026-02-24"
        },
        {
                "id_employee": "EMP-0028",
                "timestamp": "2026-02-24 08:35:10.012000+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Rihana_EMP-0028/screenshot/Feb24/319017f4-a90a-4366-808d-5156bc9af32b.webp",
                "app_name": "Telegram.exe",
                "window_title": "\u200eSiltawi \u1235\u120d\u1273\u12ca \u2013 (879438)",
                "event": "TYPE",
                "url": "",
                "date": "2026-02-24"
        },
        {
                "id_employee": "EMP-0028",
                "timestamp": "2026-02-24 08:35:15.013000+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Rihana_EMP-0028/screenshot/Feb24/af771cda-bffe-41f3-ba62-4c840ca04b71.webp",
                "app_name": "Telegram.exe",
                "window_title": "\u200eSiltawi \u1235\u120d\u1273\u12ca \u2013 (879438)",
                "event": "TYPE",
                "url": "",
                "date": "2026-02-24"
        },
        {
                "id_employee": "EMP-0028",
                "timestamp": "2026-02-24 08:35:20.015000+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Rihana_EMP-0028/screenshot/Feb24/999ce73f-9962-48aa-9f10-d5f86703dc63.webp",
                "app_name": "Telegram.exe",
                "window_title": "\u200eSiltawi \u1235\u120d\u1273\u12ca \u2013 (879438)",
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



