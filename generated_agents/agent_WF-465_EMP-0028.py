
import pyautogui
import time
import webbrowser
import os

# Generated Agent for Workflow: WF-465
# Employee: EMP-0028
# Pattern: Telegram.exe:APP_SWITCH->Telegram.exe:Custom_CLICK->Telegram.exe:TYPE->Telegram.exe:TYPE->Telegram.exe:TYPE


def run_agent():
    print(f"--- Start Generated Agent for WF-465 ---")
    pyautogui.PAUSE = 1.0

    steps = [
        {
                "id_employee": "EMP-0028",
                "timestamp": "2026-02-24 09:11:10.456000+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Rihana_EMP-0028/screenshot/Feb24/462f864c-1c8d-4f77-82ae-bdebe45eff4b.webp",
                "app_name": "Telegram.exe",
                "window_title": "\u200eRas Mtat \u2013 (879477)",
                "event": "APP_SWITCH",
                "url": "",
                "date": "2026-02-24"
        },
        {
                "id_employee": "EMP-0028",
                "timestamp": "2026-02-24 09:11:10.791875+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Rihana_EMP-0028/screenshot/Feb24/3e32eeeb-8f2e-4ad7-8fb3-4d27a70772fe.webp",
                "app_name": "Telegram.exe",
                "window_title": "\u200eRas Mtat \u2013 (879477)",
                "event": "Custom_CLICK",
                "url": "",
                "date": "2026-02-24"
        },
        {
                "id_employee": "EMP-0028",
                "timestamp": "2026-02-24 09:11:15.010000+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Rihana_EMP-0028/screenshot/Feb24/6450b91c-a75e-4307-a6ac-86e57e87f457.webp",
                "app_name": "Telegram.exe",
                "window_title": "\u200eRas Mtat \u2013 (879479)",
                "event": "TYPE",
                "url": "",
                "date": "2026-02-24"
        },
        {
                "id_employee": "EMP-0028",
                "timestamp": "2026-02-24 09:11:20+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Rihana_EMP-0028/screenshot/Feb24/25bb056a-9cb7-461b-a60b-e3e30fca3292.webp",
                "app_name": "Telegram.exe",
                "window_title": "\u200eRas Mtat \u2013 (879481)",
                "event": "TYPE",
                "url": "",
                "date": "2026-02-24"
        },
        {
                "id_employee": "EMP-0028",
                "timestamp": "2026-02-24 09:11:25.003000+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Rihana_EMP-0028/screenshot/Feb24/cc9f618e-7ba3-4167-8dff-78d19a6db729.webp",
                "app_name": "Telegram.exe",
                "window_title": "\u200eRas Mtat \u2013 (879481)",
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



