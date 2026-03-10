
import pyautogui
import time
import webbrowser
import os

# Generated Agent for Workflow: WF-445
# Employee: EMP-0028
# Pattern: Telegram.exe:Custom_CLICK->Telegram.exe:CLICK->Telegram.exe:CLICK->Telegram.exe:Custom_CLICK->Telegram.exe:Custom_CLICK


def run_agent():
    print(f"--- Start Generated Agent for WF-445 ---")
    pyautogui.PAUSE = 1.0

    steps = [
        {
                "id_employee": "EMP-0028",
                "timestamp": "2026-02-24 08:28:55.453929+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Rihana_EMP-0028/screenshot/Feb24/816f7f20-845c-40c8-8b9a-3dab3714b30c.webp",
                "app_name": "Telegram.exe",
                "window_title": "\u200eNati Gebeya \u2013 (879410)",
                "event": "Custom_CLICK",
                "url": "",
                "date": "2026-02-24"
        },
        {
                "id_employee": "EMP-0028",
                "timestamp": "2026-02-24 08:29:00.007000+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Rihana_EMP-0028/screenshot/Feb24/03f320df-37ce-435f-ad66-6678054ec754.webp",
                "app_name": "Telegram.exe",
                "window_title": "\u200eNati Gebeya \u2013 (879410)",
                "event": "CLICK",
                "url": "",
                "date": "2026-02-24"
        },
        {
                "id_employee": "EMP-0028",
                "timestamp": "2026-02-24 08:29:10.007000+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Rihana_EMP-0028/screenshot/Feb24/2848b7cf-4691-4358-91b6-d4332e23bed4.webp",
                "app_name": "Telegram.exe",
                "window_title": "\u200eNati Gebeya \u2013 (879412)",
                "event": "CLICK",
                "url": "",
                "date": "2026-02-24"
        },
        {
                "id_employee": "EMP-0028",
                "timestamp": "2026-02-24 08:29:12.724344+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Rihana_EMP-0028/screenshot/Feb24/de395b7b-9501-4ab5-b02e-0dbfa320d365.webp",
                "app_name": "Telegram.exe",
                "window_title": "\u200eNati Gebeya \u2013 (879410)",
                "event": "Custom_CLICK",
                "url": "",
                "date": "2026-02-24"
        },
        {
                "id_employee": "EMP-0028",
                "timestamp": "2026-02-24 08:29:16.278513+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Rihana_EMP-0028/screenshot/Feb24/87263f2d-b1c1-4edc-a04a-7844d71883a9.webp",
                "app_name": "Telegram.exe",
                "window_title": "\u200eNati Gebeya \u2013 (879410)",
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



