
import pyautogui
import time
import webbrowser
import os

# Generated Agent for Workflow: WF-654
# Employee: EMP-0053
# Pattern: chrome.exe:CLICK->chrome.exe:APP_SWITCH->chrome.exe:CLICK->chrome.exe:Custom_CLICK->chrome.exe:Custom_CLICK


def run_agent():
    print(f"--- Start Generated Agent for WF-654 ---")
    pyautogui.PAUSE = 1.0

    steps = [
        {
                "id_employee": "EMP-0053",
                "timestamp": "2026-02-23 12:28:20.009000+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Betelhem_EMP-0053/screenshot/Feb23/707739d6-394e-4a7d-a3d0-82549175fae0.webp",
                "app_name": "chrome.exe",
                "window_title": "1771499332.201896.m4a - Google Drive - Google Chrome",
                "event": "CLICK",
                "url": "docs.google.com/forms/d/e/1FAIpQLSfT7yNPzJDyJvzMrd4hfKuVdH8VDYydur6r0vdGD3ES__ZExA/viewform",
                "date": "2026-02-23"
        },
        {
                "id_employee": "EMP-0053",
                "timestamp": "2026-02-23 12:28:22.076000+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Betelhem_EMP-0053/screenshot/Feb23/f33e9921-a101-4763-8dd2-5aafb3bb2753.webp",
                "app_name": "chrome.exe",
                "window_title": "Untitled - Google Chrome",
                "event": "APP_SWITCH",
                "url": "drive.google.com/file/d/1u_XFhOUS5x4RISgJDgPIeKLSm5ForQX1/view",
                "date": "2026-02-23"
        },
        {
                "id_employee": "EMP-0053",
                "timestamp": "2026-02-23 12:28:25.012000+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Betelhem_EMP-0053/screenshot/Feb23/d0342b98-5877-44da-a996-2bacc78883cc.webp",
                "app_name": "chrome.exe",
                "window_title": "Call rating - Google Chrome",
                "event": "CLICK",
                "url": "docs.google.com/forms/d/e/1FAIpQLSfT7yNPzJDyJvzMrd4hfKuVdH8VDYydur6r0vdGD3ES__ZExA/viewform",
                "date": "2026-02-23"
        },
        {
                "id_employee": "EMP-0053",
                "timestamp": "2026-02-23 12:28:31.677589+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Betelhem_EMP-0053/screenshot/Feb23/ca0f38f0-d28c-41f8-819f-51937d2560df.webp",
                "app_name": "chrome.exe",
                "window_title": "1771499332.201896.m4a - Google Drive - Google Chrome",
                "event": "Custom_CLICK",
                "url": "docs.google.com/forms/d/e/1FAIpQLSfT7yNPzJDyJvzMrd4hfKuVdH8VDYydur6r0vdGD3ES__ZExA/viewform",
                "date": "2026-02-23"
        },
        {
                "id_employee": "EMP-0053",
                "timestamp": "2026-02-23 12:30:18.630650+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Betelhem_EMP-0053/screenshot/Feb23/12e520d9-813e-49f0-ad57-d1d9ef0b9053.webp",
                "app_name": "chrome.exe",
                "window_title": "Call rating - Google Chrome",
                "event": "Custom_CLICK",
                "url": "drive.google.com/file/d/1BVUSzWIk0OQ1HNfnDE61oxaISwyRl9dd/view",
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



