
import pyautogui
import time
import webbrowser
import os

# Generated Agent for Workflow: WF-351
# Employee: EMP-0028
# Pattern: Telegram.exe:Custom_CLICK->Telegram.exe:APP_SWITCH->Telegram.exe:APP_SWITCH->Telegram.exe:CLICK->Telegram.exe:Custom_CLICK


def run_agent():
    print(f"--- Start Generated Agent for WF-351 ---")
    pyautogui.PAUSE = 1.0

    steps = [
        {
                "id_employee": "EMP-0028",
                "timestamp": "2026-02-23 11:48:49.184099+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Rihana_EMP-0028/screenshot/Feb23/4cd1c815-1ccb-44d0-bfa4-9caed64c30ff.webp",
                "app_name": "Telegram.exe",
                "window_title": "\u200eHani 3 \u2013 (882607)",
                "event": "Custom_CLICK",
                "url": "",
                "date": "2026-02-23"
        },
        {
                "id_employee": "EMP-0028",
                "timestamp": "2026-02-23 11:48:50.333000+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Rihana_EMP-0028/screenshot/Feb23/3142fcf2-df59-4fab-8ba6-bf777ff4ad06.webp",
                "app_name": "Telegram.exe",
                "window_title": "\u200e\u0158\u00e8du\ud83e\udd8b \u2013 (882606)",
                "event": "APP_SWITCH",
                "url": "",
                "date": "2026-02-23"
        },
        {
                "id_employee": "EMP-0028",
                "timestamp": "2026-02-23 11:50:20.684000+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Rihana_EMP-0028/screenshot/Feb23/152a2e8f-ddf3-4ecd-bf12-220e5cfe5546.webp",
                "app_name": "Telegram.exe",
                "window_title": "\u200e\u0158\u00e8du\ud83e\udd8b \u2013 (882604)",
                "event": "APP_SWITCH",
                "url": "",
                "date": "2026-02-23"
        },
        {
                "id_employee": "EMP-0028",
                "timestamp": "2026-02-23 11:50:30.037000+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Rihana_EMP-0028/screenshot/Feb23/eff54f60-e002-4573-a43d-3f377eb3451b.webp",
                "app_name": "Telegram.exe",
                "window_title": "\u200e\u0161\u00f8\u0142\u00e2 \u2013 (882603)",
                "event": "CLICK",
                "url": "",
                "date": "2026-02-23"
        },
        {
                "id_employee": "EMP-0028",
                "timestamp": "2026-02-23 11:50:34.690925+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Rihana_EMP-0028/screenshot/Feb23/ab9bdf35-e31b-404e-ae2c-e8c32c29a801.webp",
                "app_name": "Telegram.exe",
                "window_title": "\u200e\u0158\u00e8du\ud83e\udd8b \u2013 (882604)",
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



