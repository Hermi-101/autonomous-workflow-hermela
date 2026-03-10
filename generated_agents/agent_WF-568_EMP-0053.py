
import pyautogui
import time
import webbrowser
import os

# Generated Agent for Workflow: WF-568
# Employee: EMP-0053
# Pattern: chrome.exe:Custom_CLICK->chrome.exe:MOVE->chrome.exe:CLICK->chrome.exe:Custom_CLICK->chrome.exe:APP_SWITCH


def run_agent():
    print(f"--- Start Generated Agent for WF-568 ---")
    pyautogui.PAUSE = 1.0

    steps = [
        {
                "id_employee": "EMP-0053",
                "timestamp": "2026-02-23 08:15:24.882182+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Betelhem_EMP-0053/screenshot/Feb23/faa40dc9-57a3-48c5-8f06-346b8c0e2d18.webp",
                "app_name": "chrome.exe",
                "window_title": "ChipChip CMS - Google Chrome",
                "event": "Custom_CLICK",
                "url": "chipchipadmindec.chipchip.social/cmsdash/dashboard/finance",
                "date": "2026-02-23"
        },
        {
                "id_employee": "EMP-0053",
                "timestamp": "2026-02-23 08:15:25.008000+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Betelhem_EMP-0053/screenshot/Feb23/f4690e78-ccbd-432e-8451-6d83154fe207.webp",
                "app_name": "chrome.exe",
                "window_title": "CHIPCHIP OVERVIEW \u00b7 Metabase - Google Chrome",
                "event": "MOVE",
                "url": "207.154.221.209:9903/public/dashboard/63be66c0-d506-4696-bf84-3d2c9b48c8b7?tab=1-daily-overview",
                "date": "2026-02-23"
        },
        {
                "id_employee": "EMP-0053",
                "timestamp": "2026-02-23 08:15:30.014000+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Betelhem_EMP-0053/screenshot/Feb23/726823d8-ab7f-45e7-8cc0-db4f5a2db4d2.webp",
                "app_name": "chrome.exe",
                "window_title": "CHIPCHIP OVERVIEW \u00b7 Metabase - Google Chrome",
                "event": "CLICK",
                "url": "207.154.221.209:9903/public/dashboard/63be66c0-d506-4696-bf84-3d2c9b48c8b7?tab=1-daily-overview",
                "date": "2026-02-23"
        },
        {
                "id_employee": "EMP-0053",
                "timestamp": "2026-02-23 08:15:32.228440+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Betelhem_EMP-0053/screenshot/Feb23/6423c85e-2224-464e-986a-73f64bf6782a.webp",
                "app_name": "chrome.exe",
                "window_title": "ChipChip CMS - Google Chrome",
                "event": "Custom_CLICK",
                "url": "207.154.221.209:9903/public/dashboard/63be66c0-d506-4696-bf84-3d2c9b48c8b7?tab=1-daily-overview",
                "date": "2026-02-23"
        },
        {
                "id_employee": "EMP-0053",
                "timestamp": "2026-02-23 08:15:33.159000+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Betelhem_EMP-0053/screenshot/Feb23/9ea98807-b1e6-466e-8bb7-fcb4fe323c1c.webp",
                "app_name": "chrome.exe",
                "window_title": "CHIPCHIP OVERVIEW \u00b7 Metabase - Google Chrome",
                "event": "APP_SWITCH",
                "url": "207.154.221.209:9903/public/dashboard/63be66c0-d506-4696-bf84-3d2c9b48c8b7?tab=1-daily-overview",
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



