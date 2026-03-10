
import pyautogui
import time
import webbrowser
import os

# Generated Agent for Workflow: WF-681
# Employee: EMP-0053
# Pattern: chrome.exe:APP_SWITCH->chrome.exe:MOVE->chrome.exe:Custom_CLICK->chrome.exe:Custom_CLICK->chrome.exe:CLICK


def run_agent():
    print(f"--- Start Generated Agent for WF-681 ---")
    pyautogui.PAUSE = 1.0

    steps = [
        {
                "id_employee": "EMP-0053",
                "timestamp": "2026-02-23 14:30:10.108000+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Betelhem_EMP-0053/screenshot/Feb23/b5bb047e-65e6-46d9-bad1-f2b35829bfbb.webp",
                "app_name": "chrome.exe",
                "window_title": "1771570582.217627 (2).m4a - Google Drive - Google Chrome",
                "event": "APP_SWITCH",
                "url": "drive.google.com/file/d/1ArbCO6UtJIHwUrCO9XyV1F4j1eRhWlsM/view",
                "date": "2026-02-23"
        },
        {
                "id_employee": "EMP-0053",
                "timestamp": "2026-02-23 14:30:15.008000+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Betelhem_EMP-0053/screenshot/Feb23/a520e47d-fc80-4931-a0e0-d6b5c18d3977.webp",
                "app_name": "chrome.exe",
                "window_title": "1771570582.217627 (2).m4a - Google Drive - Google Chrome",
                "event": "MOVE",
                "url": "drive.google.com/file/d/1ArbCO6UtJIHwUrCO9XyV1F4j1eRhWlsM/view",
                "date": "2026-02-23"
        },
        {
                "id_employee": "EMP-0053",
                "timestamp": "2026-02-23 14:30:41.332286+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Betelhem_EMP-0053/screenshot/Feb23/0aa1790c-1142-4ecd-9b4c-5ccaed5262e7.webp",
                "app_name": "chrome.exe",
                "window_title": "1771570582.217627 (2).m4a - Google Drive - Google Chrome",
                "event": "Custom_CLICK",
                "url": "docs.google.com/forms/d/e/1FAIpQLSfT7yNPzJDyJvzMrd4hfKuVdH8VDYydur6r0vdGD3ES__ZExA/viewform",
                "date": "2026-02-23"
        },
        {
                "id_employee": "EMP-0053",
                "timestamp": "2026-02-23 14:30:44.923678+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Betelhem_EMP-0053/screenshot/Feb23/41ad426f-70f5-4bbd-bdc5-e6ec22c62c24.webp",
                "app_name": "chrome.exe",
                "window_title": "Call rating - Google Chrome",
                "event": "Custom_CLICK",
                "url": "docs.google.com/forms/d/e/1FAIpQLSfT7yNPzJDyJvzMrd4hfKuVdH8VDYydur6r0vdGD3ES__ZExA/viewform",
                "date": "2026-02-23"
        },
        {
                "id_employee": "EMP-0053",
                "timestamp": "2026-02-23 14:30:45.016000+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Betelhem_EMP-0053/screenshot/Feb23/df61b354-542b-4a5a-bfd2-41a885a17e68.webp",
                "app_name": "chrome.exe",
                "window_title": "Call rating - Google Chrome",
                "event": "CLICK",
                "url": "docs.google.com/forms/d/e/1FAIpQLSfT7yNPzJDyJvzMrd4hfKuVdH8VDYydur6r0vdGD3ES__ZExA/viewform",
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



