
import pyautogui
import time
import webbrowser
import os

# Generated Agent for Workflow: WF-337
# Employee: EMP-0028
# Pattern: Telegram.exe:APP_SWITCH->Telegram.exe:TYPE->Telegram.exe:Custom_CLICK->Telegram.exe:Custom_CLICK->Telegram.exe:CLICK


def run_agent():
    print(f"--- Start Generated Agent for WF-337 ---")
    pyautogui.PAUSE = 1.0

    steps = [
        {
                "id_employee": "EMP-0028",
                "timestamp": "2026-02-23 11:42:59.615000+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Rihana_EMP-0028/screenshot/Feb23/ad927ca4-c96f-4f0b-a561-7bdf958e8c4a.webp",
                "app_name": "Telegram.exe",
                "window_title": "\u200e\u0161\u00f8\u0142\u00e2 \u2013 (882595)",
                "event": "APP_SWITCH",
                "url": "",
                "date": "2026-02-23"
        },
        {
                "id_employee": "EMP-0028",
                "timestamp": "2026-02-23 11:43:00.078000+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Rihana_EMP-0028/screenshot/Feb23/74fe17b3-82a1-4a9a-86fc-3fb74e3ac6d0.webp",
                "app_name": "Telegram.exe",
                "window_title": "Media viewer",
                "event": "TYPE",
                "url": "",
                "date": "2026-02-23"
        },
        {
                "id_employee": "EMP-0028",
                "timestamp": "2026-02-23 11:43:00.608031+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Rihana_EMP-0028/screenshot/Feb23/f256e62a-94ba-4914-87c1-56305679ed65.webp",
                "app_name": "Telegram.exe",
                "window_title": "\u200e\u0161\u00f8\u0142\u00e2 \u2013 (882595)",
                "event": "Custom_CLICK",
                "url": "",
                "date": "2026-02-23"
        },
        {
                "id_employee": "EMP-0028",
                "timestamp": "2026-02-23 11:43:02.216325+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Rihana_EMP-0028/screenshot/Feb23/17311507-46eb-442c-a946-855798bf21fa.webp",
                "app_name": "Telegram.exe",
                "window_title": "\u200e\u0161\u00f8\u0142\u00e2 \u2013 (882595)",
                "event": "Custom_CLICK",
                "url": "",
                "date": "2026-02-23"
        },
        {
                "id_employee": "EMP-0028",
                "timestamp": "2026-02-23 11:43:15.027000+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Rihana_EMP-0028/screenshot/Feb23/6bf07146-01d5-4c17-9b19-468d478ace5b.webp",
                "app_name": "Telegram.exe",
                "window_title": "\u200e\u0161\u00f8\u0142\u00e2 \u2013 (882592)",
                "event": "CLICK",
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



