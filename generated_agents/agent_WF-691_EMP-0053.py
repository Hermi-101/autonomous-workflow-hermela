
import pyautogui
import time
import webbrowser
import os

# Generated Agent for Workflow: WF-691
# Employee: EMP-0053
# Pattern: chrome.exe:Custom_CLICK->chrome.exe:Custom_CLICK->chrome.exe:Custom_CLICK->chrome.exe:Custom_PASTE_ACTION->chrome.exe:Custom_CLICK


def run_agent():
    print(f"--- Start Generated Agent for WF-691 ---")
    pyautogui.PAUSE = 1.0

    steps = [
        {
                "id_employee": "EMP-0053",
                "timestamp": "2026-02-24 08:21:21.418217+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Betelhem_EMP-0053/screenshot/Feb24/15b389b5-13ef-495d-946b-bbcac646f56f.webp",
                "app_name": "chrome.exe",
                "window_title": "Reports - Google Chrome",
                "event": "Custom_CLICK",
                "url": "docs.google.com/forms/d/e/1FAIpQLSfT7yNPzJDyJvzMrd4hfKuVdH8VDYydur6r0vdGD3ES__ZExA/viewform",
                "date": "2026-02-24"
        },
        {
                "id_employee": "EMP-0053",
                "timestamp": "2026-02-24 08:21:35.342020+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Betelhem_EMP-0053/screenshot/Feb24/a134eac8-302d-4eac-8ecf-a572817f73a9.webp",
                "app_name": "chrome.exe",
                "window_title": "Reports - Google Chrome",
                "event": "Custom_CLICK",
                "url": "admin.ringcloud.et/reports",
                "date": "2026-02-24"
        },
        {
                "id_employee": "EMP-0053",
                "timestamp": "2026-02-24 08:21:35.998442+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Betelhem_EMP-0053/screenshot/Feb24/238f811e-1299-40b0-9c5e-d087fa9a7f9e.webp",
                "app_name": "chrome.exe",
                "window_title": "Reports - Google Chrome",
                "event": "Custom_CLICK",
                "url": "admin.ringcloud.et/reports",
                "date": "2026-02-24"
        },
        {
                "id_employee": "EMP-0053",
                "timestamp": "2026-02-24 08:21:42.218385+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Betelhem_EMP-0053/screenshot/Feb24/9cbfddc2-a384-49eb-b5b0-6fd07a7bbc5a.webp",
                "app_name": "chrome.exe",
                "window_title": "Call rating - Google Chrome",
                "event": "Custom_PASTE_ACTION",
                "url": "docs.google.com/forms/d/e/1FAIpQLSfT7yNPzJDyJvzMrd4hfKuVdH8VDYydur6r0vdGD3ES__ZExA/viewform",
                "date": "2026-02-24"
        },
        {
                "id_employee": "EMP-0053",
                "timestamp": "2026-02-24 08:21:47.125637+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Betelhem_EMP-0053/screenshot/Feb24/97e8d286-5cb5-4a75-a392-35ede2614411.webp",
                "app_name": "chrome.exe",
                "window_title": "Reports - Google Chrome",
                "event": "Custom_CLICK",
                "url": "docs.google.com/forms/d/e/1FAIpQLSfT7yNPzJDyJvzMrd4hfKuVdH8VDYydur6r0vdGD3ES__ZExA/viewform",
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



