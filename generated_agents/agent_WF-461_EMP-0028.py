
import pyautogui
import time
import webbrowser
import os

# Generated Agent for Workflow: WF-461
# Employee: EMP-0028
# Pattern: Telegram.exe:TYPE->Telegram.exe:TYPE->Telegram.exe:TYPE->Telegram.exe:Custom_CLICK->Telegram.exe:Custom_CLICK


def run_agent():
    print(f"--- Start Generated Agent for WF-461 ---")
    pyautogui.PAUSE = 1.0

    steps = [
        {
                "id_employee": "EMP-0028",
                "timestamp": "2026-02-24 09:09:10.015000+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Rihana_EMP-0028/screenshot/Feb24/bd08af0f-d40e-4f62-ac68-9c5303bbba49.webp",
                "app_name": "Telegram.exe",
                "window_title": "\u200eRas Mtat \u2013 (879471)",
                "event": "TYPE",
                "url": "",
                "date": "2026-02-24"
        },
        {
                "id_employee": "EMP-0028",
                "timestamp": "2026-02-24 09:09:15.001000+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Rihana_EMP-0028/screenshot/Feb24/7bdf678a-3e14-4f88-93b3-a01a026240e4.webp",
                "app_name": "Telegram.exe",
                "window_title": "\u200eRas Mtat \u2013 (879471)",
                "event": "TYPE",
                "url": "",
                "date": "2026-02-24"
        },
        {
                "id_employee": "EMP-0028",
                "timestamp": "2026-02-24 09:09:25.003000+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Rihana_EMP-0028/screenshot/Feb24/91dd67d7-7923-4233-a747-3fabb45c0035.webp",
                "app_name": "Telegram.exe",
                "window_title": "\u200eRas Mtat \u2013 (879471)",
                "event": "TYPE",
                "url": "",
                "date": "2026-02-24"
        },
        {
                "id_employee": "EMP-0028",
                "timestamp": "2026-02-24 09:09:25.037130+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Rihana_EMP-0028/screenshot/Feb24/752aa36a-31aa-4be3-bc74-e1d2a180165e.webp",
                "app_name": "Telegram.exe",
                "window_title": "\u200eRas Mtat \u2013 (879471)",
                "event": "Custom_CLICK",
                "url": "",
                "date": "2026-02-24"
        },
        {
                "id_employee": "EMP-0028",
                "timestamp": "2026-02-24 09:09:28.569278+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Rihana_EMP-0028/screenshot/Feb24/a7f8e2a3-04dd-43a9-8259-c696bb98fc28.webp",
                "app_name": "Telegram.exe",
                "window_title": "\u200eRas Mtat \u2013 (879471)",
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



