
import pyautogui
import time
import webbrowser
import os

# Generated Agent for Workflow: WF-478
# Employee: EMP-0028
# Pattern: Telegram.exe:APP_SWITCH->Telegram.exe:APP_SWITCH->Telegram.exe:Custom_CLICK->Telegram.exe:APP_SWITCH->Telegram.exe:Custom_CLICK


def run_agent():
    print(f"--- Start Generated Agent for WF-478 ---")
    pyautogui.PAUSE = 1.0

    steps = [
        {
                "id_employee": "EMP-0028",
                "timestamp": "2026-02-24 09:58:02.436000+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Rihana_EMP-0028/screenshot/Feb24/558ea10f-ca30-451a-8ba8-904c68f6ecd9.webp",
                "app_name": "Telegram.exe",
                "window_title": "\u200eNati Gebeya \u2013 (879562)",
                "event": "APP_SWITCH",
                "url": "",
                "date": "2026-02-24"
        },
        {
                "id_employee": "EMP-0028",
                "timestamp": "2026-02-24 09:58:03.463000+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Rihana_EMP-0028/screenshot/Feb24/3c140b7d-2f79-41f3-a9d4-3f25b5eb0a4e.webp",
                "app_name": "Telegram.exe",
                "window_title": "\u200eNati Gebeya \u2013 (879563)",
                "event": "APP_SWITCH",
                "url": "",
                "date": "2026-02-24"
        },
        {
                "id_employee": "EMP-0028",
                "timestamp": "2026-02-24 09:58:12.751919+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Rihana_EMP-0028/screenshot/Feb24/1a99ab16-417a-4e43-90ef-73e97c1bb71a.webp",
                "app_name": "Telegram.exe",
                "window_title": "\u200eNati Gebeya \u2013 (879563)",
                "event": "Custom_CLICK",
                "url": "",
                "date": "2026-02-24"
        },
        {
                "id_employee": "EMP-0028",
                "timestamp": "2026-02-24 09:58:13.690000+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Rihana_EMP-0028/screenshot/Feb24/eea14844-bf41-4034-b3ef-69e11be8ceee.webp",
                "app_name": "Telegram.exe",
                "window_title": "Media viewer",
                "event": "APP_SWITCH",
                "url": "",
                "date": "2026-02-24"
        },
        {
                "id_employee": "EMP-0028",
                "timestamp": "2026-02-24 09:58:32.527637+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Rihana_EMP-0028/screenshot/Feb24/d346b6a1-eb9c-486a-9b04-6322a996cabf.webp",
                "app_name": "Telegram.exe",
                "window_title": "Media viewer",
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



