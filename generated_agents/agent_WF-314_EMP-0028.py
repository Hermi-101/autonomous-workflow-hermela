
import pyautogui
import time
import webbrowser
import os

# Generated Agent for Workflow: WF-314
# Employee: EMP-0028
# Pattern: flet.exe:Custom_CLICK->flet.exe:Custom_CLICK->flet.exe:Custom_CLICK->chrome.exe:Custom_CLICK->chrome.exe:Custom_CLICK


def run_agent():
    print(f"--- Start Generated Agent for WF-314 ---")
    pyautogui.PAUSE = 1.0

    steps = [
        {
                "id_employee": "EMP-0028",
                "timestamp": "2026-02-23 10:34:44.979965+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Rihana_EMP-0028/screenshot/Feb23/c1766ebb-2ec9-40b4-941c-717d22d85154.webp",
                "app_name": "flet.exe",
                "window_title": "Mate (0.0.11)",
                "event": "Custom_CLICK",
                "url": "",
                "date": "2026-02-23"
        },
        {
                "id_employee": "EMP-0028",
                "timestamp": "2026-02-23 10:34:48.388572+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Rihana_EMP-0028/screenshot/Feb23/ccba6903-857f-486f-9d98-0349d56dc1da.webp",
                "app_name": "flet.exe",
                "window_title": "Mate (0.0.11)",
                "event": "Custom_CLICK",
                "url": "",
                "date": "2026-02-23"
        },
        {
                "id_employee": "EMP-0028",
                "timestamp": "2026-02-23 10:34:53.745279+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Rihana_EMP-0028/screenshot/Feb23/b5635faf-651f-4520-ae7f-f88479edd28a.webp",
                "app_name": "flet.exe",
                "window_title": "Mate (0.0.11)",
                "event": "Custom_CLICK",
                "url": "",
                "date": "2026-02-23"
        },
        {
                "id_employee": "EMP-0028",
                "timestamp": "2026-02-23 10:35:18.471223+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Rihana_EMP-0028/screenshot/Feb23/9da12407-354f-4800-9de8-311d060e582d.webp",
                "app_name": "chrome.exe",
                "window_title": "Chipchip staff credentials - Google Sheets - Google Chrome",
                "event": "Custom_CLICK",
                "url": "64.227.129.135:8088/superset/dashboard/66/?native_filters_key=Y0a9RQKKdwtUQLVl2jmR1Z5lzml2_A7ROuAhZc7wKmFn2Inokd43s4BJzs2DlGjO",
                "date": "2026-02-23"
        },
        {
                "id_employee": "EMP-0028",
                "timestamp": "2026-02-23 10:38:13.980062+00:00",
                "image_path": "https://fra1.digitaloceanspaces.com/mgscreenshot/chipchip_data/Rihana_EMP-0028/screenshot/Feb23/1fdeeb81-e128-4296-95fa-8a813ebf69a3.webp",
                "app_name": "chrome.exe",
                "window_title": "Financial Dashbord - Google Chrome",
                "event": "Custom_CLICK",
                "url": "docs.google.com/spreadsheets/d/1xZxiemKGj4bqxG2dVb5O8tltgB5bZ_JfMn9M9MEaP7w/edit?gid=1340629039#gid=1340629039",
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



