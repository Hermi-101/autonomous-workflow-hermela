
import pyautogui
import time
import webbrowser
import os

# Generated Agent for Workflow: WF-343
# Employee: EMP-0028
# Pattern: Telegram.exe:Custom_CLICK->Telegram.exe:CLICK->Telegram.exe:Custom_CLICK->Telegram.exe:Custom_CLICK->Telegram.exe:Custom_CLICK


def run_agent():
    print(f"--- Start Generated Agent for WF-343 ---")
    pyautogui.PAUSE = 1.0

    steps = [
        {
                "id_employee": "EMP-0028",
                "timestamp": "2026-02-23 11:43:34.375025+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Rihana_EMP-0028/screenshot/Feb23/5545b76d-f84f-4c58-8e3e-e30f24da90f8.webp",
                "app_name": "Telegram.exe",
                "window_title": "\u200e\u0161\u00f8\u0142\u00e2 \u2013 (882592)",
                "event": "Custom_CLICK",
                "url": "",
                "date": "2026-02-23"
        },
        {
                "id_employee": "EMP-0028",
                "timestamp": "2026-02-23 11:43:35.022000+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Rihana_EMP-0028/screenshot/Feb23/68534b5f-fb02-4e9e-aa57-eaf28d1d3da2.webp",
                "app_name": "Telegram.exe",
                "window_title": "\u200e\u0161\u00f8\u0142\u00e2 \u2013 (882592)",
                "event": "CLICK",
                "url": "",
                "date": "2026-02-23"
        },
        {
                "id_employee": "EMP-0028",
                "timestamp": "2026-02-23 11:43:38.880973+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Rihana_EMP-0028/screenshot/Feb23/1c5234d7-1b7f-4637-ba95-58fc8a029a1b.webp",
                "app_name": "Telegram.exe",
                "window_title": "\u200e\u0161\u00f8\u0142\u00e2 \u2013 (882592)",
                "event": "Custom_CLICK",
                "url": "",
                "date": "2026-02-23"
        },
        {
                "id_employee": "EMP-0028",
                "timestamp": "2026-02-23 11:43:50.543782+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Rihana_EMP-0028/screenshot/Feb23/ee45b1db-0947-41fb-8c6f-374f9d368403.webp",
                "app_name": "Telegram.exe",
                "window_title": "\u200e\u0161\u00f8\u0142\u00e2 \u2013 (882592)",
                "event": "Custom_CLICK",
                "url": "",
                "date": "2026-02-23"
        },
        {
                "id_employee": "EMP-0028",
                "timestamp": "2026-02-23 11:43:51.763935+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Rihana_EMP-0028/screenshot/Feb23/05c6f760-9e30-45d6-b375-1f7afbe3a07c.webp",
                "app_name": "Telegram.exe",
                "window_title": "TelegramDesktop",
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



